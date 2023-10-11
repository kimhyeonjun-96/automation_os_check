import os
import json
from datetime import datetime

from custom_modules.file_modules.service.fileService import FileService

class ReadSettingFile(FileService):
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "_init"):
            cls._init = True
    
    def getSettingFilePath(self):
        try:
            dir = os.path.realpath(os.path.join(os.path.join(os.path.dirname(__file__), os.pardir),"file_path.yaml"))
            return  dir
        except Exception as e: 
            print("ReadSettingFile : getTextPath >> {}".format(e) )
            return 0

    def getJsonPath(self):
        pass
    def readFile(self,jsonPath):
        pass
    
