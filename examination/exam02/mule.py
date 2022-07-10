from horse import Horse
from donkey import Donkey
class Mule(Horse,Donkey):
    def run(self):
        print(f'Mule is running')
    
    def show_info(self):
        print('a3')
        print(f'Name: {self.show_info}\nColor: {self.color}\nMax Height: {self.max_height}\nAge:{self.age}\nWeight:{self.weight}')

mule1 = Horse("Mumu","Blue-eyed cream")
mule1 = Donkey(3,200)
mule1.show_info()

mule2 = Horse('Meme','Palomino')
mule2 = Donkey(1,120.7)
mule2.sound()
mule2.show_info()
#แสดงได้2หัวข้อครับ
