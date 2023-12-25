from time import sleep
import subprocess


def Converter_dicts(command_exec):
            try:
                sleep(1.5)
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
            return True