#vehicle_subclass.py
from  bank import Bank
class Abank(Bank):
    total = 0
    def __init__(self, bankname: str,interest:float ,monthlypay:float) -> None:
        super().__init__(bankname)
        self.__loanamount = 0 
        self.__loanyear = 0
        self.__loanrate = 0 
        self.interest = interest
        self.monthlypay = monthlypay
    
    @property
    def loanamount(self):
        return self.__loanamount
    @loanamount.setter
    def loanamount(self,value):
        self.__loanamount = value

        
    @property
    def loanyear(self):
        return self.__loanyear
    @loanyear.setter
    def loanyear(self,value):
        self.__loanyear = value
        
    @property
    def loanrate(self):
        return self.__loanrate
    @loanrate.setter
    def loanrate(self,value):
        self.__loanrate = value
        
    
    def flat_rate(self):
        pass
    
#ทำได้เท่านี้ครับ
