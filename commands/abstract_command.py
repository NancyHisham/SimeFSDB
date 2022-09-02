from abc import ABCMeta, abstractstaticmethod
# this method is used for creating the ICommand as an abstract class

class ICommand(metaclass=ABCMeta):
<<<<<<< Updated upstream:commands/abstract_command.py
    
=======
     
>>>>>>> Stashed changes:ICommand.py
    @abstractstaticmethod
    def excute(self):
        """The interface of ICommand"""