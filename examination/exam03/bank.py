#vehicle_abstract.py
#ต้อง import แบบนี้เสมอสำหรับ abstract class
from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self,bankname:str) -> None:
        self.bankname = bankname


    @abstractmethod
    def flat_rate(self):
        pass