from abc import ABCMeta, abstractmethod

'''
An abstract class for a Component
participating to get access the critical section.

We specify the methods each
sub class needs to implement.
'''


class Component(metaclass=ABCMeta):
    second_check = None
    allComponents = []
    critical_value = NotImplemented

    def __init__(self, name):
        self.name = name
        self.flag = False
        Component.allComponents.append(self)

    @abstractmethod
    def non_critical_section(self):
        pass

    @abstractmethod
    def critical_section(self):
        pass

    @abstractmethod
    def _precondition(self):
        return

    def _cs_condition(self):
        return

    @abstractmethod
    def peterson(self):
        pass
