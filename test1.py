import sys
import time

from threading import Thread

from petersons import Component

'''
In this test case, we have three components, 
each trying to get access to a critical section to 
change the value of a variable.

Safety and Liveness are guaranteed but no 
guarantee is made about the order of access.
'''


class ChangeVariable(Component):
    
    critical_value = 0

    def __init__(self, name, funct):
        super(ChangeVariable, self).__init__(name)
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

        ChangeVariable.critical_value = self.funct(ChangeVariable.critical_value)
        # Re assigning a new value to the shared variable

        print("*********** critical: {} *************\nshared-variable: {: ^9}\nflags: {}"
              "\ndisjunct: {}\n=====================================\n"
              .format(self.name, ChangeVariable.critical_value,
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


if __name__ == '__main__':
    s = ChangeVariable('S', lambda x: x + 100)  # Add
    p = ChangeVariable('P', lambda x: x - 50)  # Subtract
    q = ChangeVariable('Q', lambda x: x - 50)  # Subtract

    p1 = Thread(target=s.peterson)
    p2 = Thread(target=p.peterson)
    p3 = Thread(target=q.peterson)
    #
    sys.setswitchinterval(0.4) # Time interval to switch threads.

    p1.start()
    p2.start()
    p3.start()
# Note: Order of execution is not guarenteed