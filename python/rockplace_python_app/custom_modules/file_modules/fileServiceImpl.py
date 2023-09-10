import os
import json
from datetime import datetime

from custom_modules.file_modules.readSettingFile import ReadSettingFile
from custom_modules.file_modules.readDataFile import ReadDataFile

class FileServiceImpl():    
    
    @staticmethod
    def start():
        try:
            read_file = ReadSettingFile()
            data_file = ReadDataFile()
            
            txt_path = read_file.getSettingFilePath()
            
            jsonPath , savePath = data_file.getJsonPath(txt_path)
            host_data = data_file.readFile(jsonPath)
            
            if len(host_data) != 0:
                return host_data, savePath
            
        except Exception as e: 
            print("FileServiceImpl : start >> {}".format(e) )
        
        
    