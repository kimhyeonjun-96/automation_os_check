from abc import *

class ParsingService(ABC):
    """ 데이터 가공 """
    @abstractmethod
    def start_parsing(self):
        pass
    