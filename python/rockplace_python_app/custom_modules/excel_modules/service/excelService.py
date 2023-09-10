from abc import *

class ExcelService(ABC):
    """ 엑셀 작성 """
    
    """ 공통 """
    # 엑셀 생성
    @abstractmethod
    def createExcel(self):
        pass
    # 서명 시트
    @abstractmethod
    def createSignSheet(self):
        pass
    # 점검 항목 리스트
    @abstractmethod
    def createCheckItemSheet(self):
        pass
    # 서버 점검 내용 시트
    @abstractmethod
    def createCheckSheet(self):
        pass
    # 저장
    @abstractmethod
    def saveExcel(self):
        pass
    # 리소스 사용률 기준치 이상 체크
    @abstractmethod
    def checkResource(self):
        pass
    
    """ 고객사 점검 리스트 시트 생성"""
    @abstractmethod
    def createCustomSheet(self):
        pass

    """ 고객사 데이터 작성 """
    # 데이터 삽입
    @abstractmethod
    def writeData(self):
        pass
    # 스타일
    @abstractmethod 
    def dataStyle(self):
        pass
    
    
    """ start """
    @abstractmethod
    def excel_start(self):
        pass