class Host:
    __hostname = ''
    __version = ''
    __kernel = ''
    __uptime = ''
    __use_cpu = ''
    __real_mem = ''
    __swap_mem = ''
    __use_disk = ''
    __network = ''
    __top5 = ''
    __zom = ''
    __ntp = ''
    __log = ''
    __ssh_msg = ''
        
    def setHostname(self, hostname):
        self.__hostname = hostname
    
    def setVersion(self, version):
        self.__version = version
        
    def setKernel(self, kernel):
        self.__kernel = kernel
        
    def setUptime(self, uptime):
        self.__uptime = uptime
        
    def setUseCpu(self, cpu):
        self.__use_cpu = cpu+'%'
        
    def setUseRealMem(self, real_mem):
        try:
            self.__real_mem = str(round((real_mem['used']/real_mem['total'])*100,1))+'%'
        except Exception as e:
            print("host : setUseRealMem >> {}".format(e))
            self.__real_mem = 'fail'

    def setUseSwapMem(self, swap_mem):
        try:
            self.__swap_mem = str(round((swap_mem['used']/swap_mem['total'])*100))+'%'
        except Exception as e:
            print("host : setUseSwapMem >> {}".format(e))
            self.__swap_mem = 'fail'
            
    def setUseDisk(self, use_disk):
        try:
            disk_list = []
            disk_str = ''
            for disk in use_disk:
                if "note" not in disk and disk['uuid'] != 'N/A' and disk['fstype'] not in 'nfs' :
                    use = round((disk['block_used']/disk['block_total'])* 100)
                    if use >= 10 and "note" not in disk:
                        disk_list.append(str(disk['mount'])+" : "+str(round((disk['block_used']/disk['block_total'])* 100))+"%")
            
            if len(disk_list) != 0:
                for disk in disk_list:
                    disk_str += disk+'\n'
                self.__use_disk = disk_str
            else:
                self.__use_disk = 'pass'
        except Exception as e:
            print("host : setUseDisk >> {}".format(e))
            self.__use_disk = 'fail'  
        
    def setNetwork(self, network):
        net_str = ''
        if network['stdout'] == '':
            self.__network = 'pass' 
        else:  
            for net in network['stdout'].translate({ord(':'):None}).split(' '):
                net_str += net + ' is down' + '\n'
                
            self.__network = net_str
        
    def setZom(self, zombies): 
        if zombies['stdout'] != '':
            count =  0
            for i in zombies['stdout'].split('>'):
                count +=1
            self.__zom = str(count)
        else:
            self.__zom = '0'
        
    def setNtp(self, ntp):
        check_ntp = "pass"
        try:
            if 'ntp_sync' in ntp:
                ntp_sync = ntp['ntp_sync']
                if "ntpq -p" in ntp_sync['cmd'] and ntp_sync['stdout'] != '*':
                    check_ntp = "fail : ntp sync fail"
                elif "ntpq -p" in ntp_sync['cmd'] and ntp_sync['stdout'] == '*':
                    check_ntp = "pass"
            elif 'chrony_sync' in ntp:
                chrony_sync = ntp['chrony_sync']
                if "chronyc sources" in chrony_sync['cmd'] and "*" not in chrony_sync['stdout']:
                    check_ntp = "fail : chronyc sync fail"
                elif "chronyc sources" in chrony_sync['cmd'] and "*" in chrony_sync['stdout']:
                    check_ntp = "pass"
            else:
                check_ntp = "fail : check the daemon"
                
            self.__ntp = check_ntp
        except Exception as e:
            print("host : setNtp >> {}".format(e))
            
    def setLog(self, log):
        if int(log['log']['stdout']) != 0:
            self.__log = 'fail'
        else:
            self.__log = 'pass'
        
    def setSshMsg(self, ssh):
        self.__ssh_msg = ssh
    
    def getHostname(self):
        return self.__hostname
    
    def getVersion(self):
        return self.__version
        
    def getKernel(self):
        return self.__kernel
        
    def getUptime(self):
        return self.__uptime
        
    def getUseCpu(self):
        return self.__use_cpu
        
    def getUseRealMem(self):
        return self.__real_mem
        
    def getUseSwapMem(self):
        return self.__swap_mem
        
    def getUseDisk(self):
        return self.__use_disk
        
    def getNetwork(self):
        return self.__network
        
    def getZom(self):
        return self.__zom
        
    def getNtp(self):
        return self.__ntp
        
    def getLog(self):
        return self.__log
        
    def getSshMsg(self):
        return self.__ssh_msg
    
    def toString(self):
        print("hostname : {}\nos-version : {}\nkernel : {}\nuptime : {}\nuse_cpu : {}\nreal_mem : {}\nswap_mem : {}\nuse_disk : {}\nnetwork : {}\nzom : {}\nntp : {}\nlog : {}\n".format(self.getHostname(),self.getVersion(),self.getKernel(),self.getUptime(),self.getUseCpu(),self.getUseRealMem(),self.getUseSwapMem(),self.getUseDisk(),self.getNetwork(),self.getZom(),self.getNtp(),self.getLog()))
    
    def sshToString(self):
        print("hostname : {}\nssh : {}\n".format(self.getHostname(), self.getSshMsg()))