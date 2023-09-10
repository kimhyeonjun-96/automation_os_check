import os
import json
from datetime import datetime

from custom_modules.parsing_modules.jsonParsingService import JsonParsingService

class ParsingServiceImpl():
    
    @staticmethod
    def parsing(data):
        try:
            parsing = JsonParsingService(data)
            return parsing.start_parsing()
        except Exception as e: 
            print("ParsingServiceImpl : parsing >> {}".format(e) )