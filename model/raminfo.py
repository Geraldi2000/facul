import subprocess
from lumus_class import ramInfo
from time import sleep
from lumus_functions import Converter_dicts


class ramINIT():
    
    def get_ramINFO(self) -> str:
        command = 'Get-CimInstance -Class CIM_PhysicalMemory | Select-Object *'
        try:
            sleep(0.5)
            result = subprocess.run(['powershell', '-Command', command], shell=True, capture_output=True, text=True)
            return result.stdout
        except:
            print("ERRO get_ramINFO")
            print(result.stderr)
        return False

        
    def get_ramINFO_MAX(self) -> int:
        command = 'Get-WmiObject Win32_PhysicalMemory | Select-Object @{Name = "GB"; Expression = {$_.Capacity / 1GB}}'
        try:
            sleep(0.5)
            result = subprocess.run(['powershell', '-Command', command], shell=True, capture_output=True, text=True)
            result = (result.stdout.split())
            return f"{result[2]}GB"
        except:
            print("ERRO get_ramINFO")
        return False
        

    def get_ramINFO_MODEL(self) -> str:
        command = "Get-CimInstance -Class CIM_PhysicalMemory | Select-Object"
        mount_result = Converter_dicts(command)
        self.model = mount_result["Model"]
        return self.model 

    
teste = ramINIT()
print(teste.get_ramINFO_MODEL())