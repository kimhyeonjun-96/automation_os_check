import os
import json
from datetime import datetime

from custom_modules.parsing_modules.service.parsingService import ParsingService
from custom_modules.parsing_modules.host import Host

class JsonParsingService(ParsingService):
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self,data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            cls._init = True
            self.dataList = data
            self.hostList = []
    
    def start_parsing(self):
        for data in self.dataList:
            host = Host()
            if 'check_ssh' in data['hostinfo']:
                # print("connect success : {} , {}".format(data['hostinfo']['ansible_fqdn'], data['hostinfo']['ansible_facts']['default_ipv4']))
                host.setHostname(data['hostinfo']['ansible_fqdn'])
                host.setVersion(data['hostinfo']['ansible_distribution']+ '-' + data['hostinfo']['ansible_distribution_version'])
                host.setKernel(data['hostinfo']['ansible_kernel'])
                #host.setUptime(datetime.fromtimestamp(data['hostinfo']['ansible_uptime_seconds']).strftime("%d")+' days')
                host.setUptime(data['hostinfo']['uptime']['msg'])
                host.setUseCpu(data['hostinfo']['cpu']['stdout'])
                host.setUseRealMem(data['hostinfo']['memory']['stdout'])
                host.setUseSwapMem(data['hostinfo']['ansible_memory_mb']['swap'])
                host.setUseDisk(data['hostinfo']['ansible_facts']['mounts'])
                host.setNetwork(data['hostinfo']['downNetwork'])
                host.setZom(data['hostinfo']['zombie'])
                host.setNtp(data['hostinfo'])
                host.setLog(data['hostinfo'])
            
            else:
                host.setHostname(data['hostinfo']['inventory_hostname'])
                host.setSshMsg("{} : Failed to connect to the host via ssh ".format(data['hostinfo']['inventory_hostname']))
                
            self.hostList.append(host)
        
        return self.hostList
        
