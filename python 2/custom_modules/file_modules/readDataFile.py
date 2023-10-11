import os
import json
from datetime import datetime

from custom_modules.file_modules.service.fileService import FileService

class ReadDataFile(FileService):
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.json_data = ""
            cls._init = True
    
    def getSettingFilePath(self):
        pass

    def getJsonPath(self, path):
        try:
            txt_path = path
            f = open(txt_path, 'r')
            lines = f.readlines()
            f.close
            self.path = lines[-1].split(': ')[1].replace("\n", "")
            return lines[-1].split(': ')[1].replace("\n", "") + "/check_result.json", self.path
        except Exception as e: 
            print("ReadDataFile : getJsonPath >> {}".format(e) )
            return 0

    def readFile(self,jsonPath):
        try:
            with open(jsonPath, 'r', encoding="utf-8") as f:
                self.json_data = json.load(f)
                host_data = self.json_data['hosts']    
            return host_data
        except Exception as e: 
            print("ReadDataFile : readFile >> {}".format(e) )
    