class Vehicle:
    def __init__(self,name,wheels,max_speed,vin) -> None:
        
        self.name = name
        self.wheels = wheels
        self._max_speed = max_speed
        self.__vin = vin
    def Bus(self,color,capacity):
        self.color = color
        self.capacity = capacity
        
    def set_vin(self,vin):
        self.__vin = vin
        
    def v_detail(self):
        print('==============')
        print(f'name: {self.name}')
        print('==============')
        print(f'wheels:{self.wheels}')
        print(f'max_speed: {self._max_speed}')
        print(f'vin:{self.__vin}')



        