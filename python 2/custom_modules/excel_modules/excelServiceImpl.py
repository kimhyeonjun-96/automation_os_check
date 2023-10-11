import os
import json
from datetime import datetime

from custom_modules.excel_modules.hyudaiExcelServiceImpl import HyudaiExcelServiceImpl

class ExcelServiceImpl():
    
    @staticmethod
    def excel(host_list, savePath):
        host_excel = HyudaiExcelServiceImpl(savePath)
        host_excel.excel_start(host_list)