from geographic import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    def __init__(self,name,area,pop) -> None:
        self.name = name
        self.area = area
        self.poppulation = pop
        
    def getpoppulationdensity(self):
        return self.poppulation / self.area
    
    def showdetail(self):
        print(f'Country: {self.name}')
        print(f'Location:{self.getcordinate()}')
        print(f'Population: {self.poppulation:,d}')
        print(f'Area:{self.area:,.2f}')
        print(f'Density: {self.getpoppulationdensity():,.2f}')
        
        print(f'Time Zone: {self.gettimezone()}')
        print(f'Climate: {self.getclimate()}')
        print(f'Temperture(C): {self.getcelcius()}')
        print(f'Temperature(F): {self.getfahrenheit()}')
        print(f'Weather: {self.getweather()}')
        
        print('*******************')
        