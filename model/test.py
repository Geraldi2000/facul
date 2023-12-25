
import subprocess
from lumus import cpuInfo

def Converter_dicts(command_exec):
            try:
                result = subprocess.run(['powershell', '-Command', command_exec], shell=True, capture_output=True, text=True)
                lines = result.stdout.splitlines()
                info_dict = {}
                for line in lines:
                    if ':' not in line: continue
                    key, value = map(str.strip, line.split(':', 1))
                    info_dict[key] = value
                return info_dict
            except:
                confirm_error = result.stderr
                print(f"Erro na execucao do comando,\n class: cpuINIT: METH :INFOCPU \n {confirm_error} ")

class cpuINIT(cpuInfo): 
    def __init__(self, data) -> None:
        super().__init__(data)

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
        threads = mount_result["ThreadCount"]
        return int(threads)
        
    
    def INFOCPU_MODEL(self) -> str:
        command = "Get-CimInstance -ClassName Win32_Processor | Select-Object * "
        mount_result = Converter_dicts(command)
        model_cpu,name_cpu = mount_result["Description"], mount_result["Name"]
        return f" Model: {model_cpu}\n {name_cpu}"
    
    def INFOCPU_ARCH(self) -> str:
        command = "Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -Property SystemType"
        try:
                result = subprocess.run(['powershell', '-Command', command], shell=True, capture_output=True, text=True)
                output = result.stdout
                return output
        except:
            confirm_error = result.stderr
            print(f"Erro na execucao do comando,\n{confirm_error} ")
    
    def INFOCPU_CORES(self) -> str:
        command = "Get-CimInstance -ClassName Win32_Processor | Select-Object * "
        mount_result = Converter_dicts(command)
        enable_cores,max_cores = mount_result["NumberOfEnabledCore"], mount_result["NumberOfCores"]
        return f" Enable cores: {enable_cores}\n Cores: {max_cores}"


a = "10" # argumento qualquer 
instancia_cpuINIT = cpuINIT(a)
resultado = instancia_cpuINIT.INFOCPU()
resultado2 = instancia_cpuINIT.INFOCPU_CORES()
print(resultado2)

