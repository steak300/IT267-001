class Customer:
    def __init__(self) -> None:
        self.name = ''
        self.address = ''
        self.phone = ''
        
    def new_customer(self):
        self.name = input('Enter customer name: ')
        self.address = input('Ennter customer adress: ')
        self.phone = input('Enter customer phone: ')
    
    def cus_info(self):
        return f'name: {self.name}\naddress: {self.address}\nphone: {self.phone}'