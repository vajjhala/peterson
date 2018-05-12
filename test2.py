import sys
import time

from threading import Thread

from petersons import Component

'''
In this test case 3 components try to mutate
a list. 
Again only safety and liveness are guaranteed.
'''


class MutateDataStruct(Component):

    critical_value = []

    def __init__(self, name, funct):
        super(MutateDataStruct, self).__init__(name)
        self.funct = funct

    def non_critical_section(self):
        print("Non-Critical: {}".format(self.name))

    def _precondition(self):
        # Invariant Condition for the Peterson's Algorithm

        all_comps = Component.allComponents

        # {P} do true -> S od {P}

        while True:
            check_list = [x.flag for x in all_comps]
            if True in check_list:
                continue
            else:
                break
        return

    def _cs_condition(self):
        # Condition to enter the critical section

        other_comps = []
        for elem in Component.allComponents:
            if elem != self:
                other_comps.append(elem)

        #  if {} -> skip fi
        while True:
            check_list = [x.flag for x in other_comps]
            if (True not in check_list) or (Component.second_check != self):
                break
        return

    def critical_section(self):

        self.funct(MutateDataStruct.critical_value)
        # Mutating the list

        print("*********** critical: {} *************\nmutable-list: {}\nflags: {}"
              "\ndisjunct: {}\n=====================================\n"
              .format(self.name, MutateDataStruct.critical_value,
                      {x.name: x.flag for x in Component.allComponents if x != self},
                      Component.second_check.name))
        time.sleep(1)

    def peterson(self):
        print('Started Peterson for: ', self.name)
        self._precondition()  # Pre-condition
        while True:  # do true -> S od
            self.non_critical_section()
            self.flag = True
            Component.second_check = self
            self._cs_condition()
            self.critical_section()
            self.flag = False


def natural_numbers():
    num = 0
    while True:
        yield num
        num = num + 1


def pop_if_not_empty(x):
    if len(x) == 0:
        pass
    else:
        x.pop()


if __name__ == '__main__':
    natural_number_generator = natural_numbers()
    s = MutateDataStruct('S', lambda x: x.append(next(natural_number_generator)))  # Credit
    p = MutateDataStruct('P', pop_if_not_empty )  # Debit 1
    q = MutateDataStruct('Q', lambda x: x.append("Q"))  # Debit 2

    p1 = Thread(target=s.peterson)
    p2 = Thread(target=p.peterson)
    p3 = Thread(target=q.peterson)
    #
    # sys.setswitchinterval(1)

    p1.start()
    p2.start()
    p3.start()
