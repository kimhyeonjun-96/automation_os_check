from abc import *

class FileService(ABC):
    """ 앤서블 & 파이썬 공통 설정파일을 읽기 """
    @abstractmethod
    def getSettingFilePath(self):
        pass

    """ 앤서블을 통해 수집된 데이터 파일 (JSON)을 읽어들이고 반환 """
    @abstractmethod
    def getJsonPath(self):
        pass

    @abstractmethod
    def readFile(self, jsonPath):
        pass

    