import subprocess
from abc import ABC, abstractmethod
from time import sleep

class cpuInfo(ABC):
    
    @abstractmethod
    def INFOCPU(self) -> str:
        return 


    @abstractmethod
    def INFOCPU_THREADS(self) -> int:
        return 


    @abstractmethod
    def INFOCPU_MODEL(self) -> str:
        return 


    @abstractmethod
    def INFOCPU_ARCH(self) -> str:
        return 


    @abstractmethod
    def INFOCPU_CORES(self) -> int:
        return 



class ramInfo(ABC):
    
    @abstractmethod
    def ramINFO(self) -> str:
        return 


    @abstractmethod
    def ramINFO_MAX(self) -> int:
        return 

    @abstractmethod
    def ramINFO_MODEL(self) -> str:
        return 


    @abstractmethod
    def ramINFO_ARCH(self) -> str:
        return 


    @abstractmethod
    def ramINFO_DDR(self) -> str:
        return 


    @abstractmethod
    def ramINFO_CACHE(self) -> str:
        return 



class procInfo(ABC):
    
    @abstractmethod
    def procINFO(self) -> str:
        return 


    @abstractmethod
    def procINFO_MAX(self) -> int:
        return 

    @abstractmethod
    def procINFO_MODEL(self) -> str:
        return 


    @abstractmethod
    def procINFO_ARCH(self) -> str:
        return 


    @abstractmethod
    def procINFO_DDR(self) -> str:
        return 


    @abstractmethod
    def procINFO_CACHE(self) -> str:
        return 

