from custom_modules.file_modules.fileServiceImpl import FileServiceImpl
from custom_modules.parsing_modules.parsingServiceimpl import ParsingServiceImpl
from custom_modules.excel_modules.excelServiceImpl import ExcelServiceImpl

if __name__=="__main__":
    # 퍼일 인스턴스 생성
    host_data, savePath = FileServiceImpl.start()

    # 파싱
    parsing_list = ParsingServiceImpl.parsing(host_data)
    
    # 엑셀
    ExcelServiceImpl.excel(parsing_list, savePath)