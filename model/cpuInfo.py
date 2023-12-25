
import subprocess
from lumus_class import cpuInfo
from time import sleep
from lumus_functions import Converter_dicts

class cpuINIT(cpuInfo): 
    
    def __init__(self,cores,arch,threads,model) -> None:
         super().__init__()
         self.cores, self.arch, self.threads, self.model = cores,arch,threads,model
         return None
    
    def INFOCPU(self) -> str:
        command = "Get-CimInstance -ClassName Win32_Processor | Select-Object * "
        mount_result = Converter_dicts(command)
        name_cpu, threads, description, l3_chache = (mount_result["Name"], mount_result["ThreadCount"], mount_result["Description"], mount_result["L3CacheSize"])
        l2_chache, MaxClockSpeed, cores, enable_cores = (mount_result["L2CacheSize"], mount_result["MaxClockSpeed"], mount_result["NumberOfCores"], mount_result["NumberOfEnabledCore"])
        result = (f" Numero de cores: {cores}\n Numero de threads: {threads}\n Numero de cores ativos: {enable_cores}\n Numero maximo de clockSpeed: {MaxClockSpeed}\n Cache L3: {l3_chache}\n Cache l2: {l2_chache}\n CPU: {name_cpu}\n Descricao: {description}")
        return result
    
    def INFOCPU_THREADS(self) -> int:
        command = "Get-CimInstance -ClassName Win32_Processor | Select-Object * "
        mount_result = Converter_dicts(command)
        self.threads = mount_result["ThreadCount"]
        return int(self.threads)
        
    def INFOCPU_MODEL(self) -> str:
        command = "Get-CimInstance -ClassName Win32_Processor | Select-Object * "
        mount_result = Converter_dicts(command)
        model_cpu,name_cpu = mount_result["Description"], mount_result["Name"]
        self.model =  f" Model: {model_cpu}\n {name_cpu}"
        return self.model
    
    def INFOCPU_ARCH(self) -> str:
        command = "Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -Property SystemType"
        try:
                result = subprocess.run(['powershell', '-Command', command], shell=True, capture_output=True, text=True)
                self.arch = result.stdout
                return self.arch
        except:
            confirm_error = result.stderr
            print(f"Erro na execucao do comando,\n{confirm_error} ")
    
    def INFOCPU_CORES(self) -> str:
        command = "Get-CimInstance -ClassName Win32_Processor | Select-Object * "
        mount_result = Converter_dicts(command)
        enable_cores,max_cores = mount_result["NumberOfEnabledCore"], mount_result["NumberOfCores"]
        self.cores =  f" Enable cores: {enable_cores}\n Cores: {max_cores}"
        return self.cores




