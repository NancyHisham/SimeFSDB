from abc import ABCMeta, abstractstaticmethod
# this method is used for creating the ICommand as an abstract class

class AbstractCommand(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def excute(self):
        """The interface of ICommand"""