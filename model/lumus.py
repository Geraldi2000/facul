import subprocess
from abc import ABC, abstractmethod

class cpuInfo(ABC):
    def __init__(self, data) -> None:
        super().__init__()
        self.data = data
    
    @abstractmethod
    def INFOCPU(self) -> str:
        return 


    # @abstractmethod
    # def INFOCPU_THREADS(self) -> int:
    #     return 


    # @abstractmethod
    # def INFOCPU_PROC_MAIOR_USO(self) -> str:
    #     return 


    # @abstractmethod
    # def INFOCPU_MODEL(self) -> str:
    #     return 


    # @abstractmethod
    # def INFOCPU_ARCH(self) -> str:
    #     return 


    # @abstractmethod
    # def INFOCPU_ANO(self) -> str:
    #     return 


    # @abstractmethod
    # def INFOCPU_MODEL(self) -> str:
    #     return 


    # @abstractmethod
    # def INFOCPU_CONSUMO_MEDIO(self) -> str:
    #     return 


    # @abstractmethod
    # def INFOCPU_CONSUMO_ATUAL(self) -> str:
    #     return 


    # @abstractmethod
    # def INFOCPU_CORES(self) -> int:
    #     return 



# class ramInfo(ABC):
#     def __init__(self, data_archive) -> None:
#         super().__init__()
#         self.data = data_archive
    
#     @abstractmethod
#     def ramINFO(self) -> str:
#         return 


#     @abstractmethod
#     def ramINFO_MAX(self) -> int:
#         return 


#     @abstractmethod
#     def ramINFO_PROC_MAIOR_USO(self) -> str:
#         return 


#     @abstractmethod
#     def ramINFO_MODEL(self) -> str:
#         return 


#     @abstractmethod
#     def ramINFO_ARCH(self) -> str:
#         return 


#     @abstractmethod
#     def ramINFO_DDR(self) -> str:
#         return 


#     @abstractmethod
#     def ramINFO_MODEL(self) -> str:
#         return 


#     @abstractmethod
#     def ramINFO_CONSUMO_MEDIO(self) -> str:
#         return 


#     @abstractmethod
#     def ramINFO_CONSUMO_ATUAL(self) -> str:
#         return 


#     @abstractmethod
#     def ramINFO_SWAP(self) -> str:
#         return 



