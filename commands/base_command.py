from abc import ABC, abstractmethod

class BaseCommand(ABC):
    """
    Classe abstrata que define a interface padrão para todos os comandos.
    Todos os comandos concretos devem herdar desta classe.
    """
    
    @abstractmethod
    def execute(self):
        """
        Método abstrato que deve ser implementado por todas as subclasses.
        Contém a lógica específica de cada comando.
        """
        pass