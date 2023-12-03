import subprocess

af = subprocess.run("ls",capture_output=True,shell=True)
print(f"{af}")
