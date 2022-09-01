from abc import ABCMeta, abstractstaticmethod
# this method is used for creating the ICommand as an abstract class
class ICommand(metaclass=ABCMeta):
    @abstractstaticmethod
    def execute(self):
        """The interface of ICommand"""