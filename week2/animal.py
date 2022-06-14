class Animal:
    #class variable
    animal = "CAT"
    
    def new_animal(self,name:str,breed,colour,age:int):
        #instance variable
        self.name = name
        self.breed = breed
        self.colour = colour
        self.age = age
        
    def print_detail(self):
        print(f"***********")
        print(f"Name: {self.name}")
        print(f"Animal: {self.animal}")
        print(f"Breed: {self.breed}")
        print(f"Colour: {self.colour}")
        print(f"Age: {self.age}")
        
    def __del__(self):
        print(f'Object was destoryed')
#create object
if __name__ == "__main__":
    Animal.animal = "Fish"
    ula = Animal()
    ula.animal = "DOG"
    ula.new_animal("Ula","Scottish","White",1)
    ula.print_detail()
    
    drac = Animal()
    drac.new_animal("Drac","Scottish","White",1)
    drac.print_detail()
    drac.breed = "Catfish"
    drac.print_detail()
    
    Animal.print_detail(ula)#ula.print_detail()
    
    #เรียกดู class variableทั้งหมด
    print(f'{Animal.__dict__}')
    
    print(f'{ula.__dict__}')
    
    peter = Animal()
    peter.new_animal("Peter","Parrot","Green Yellow Red",2)
    #add new  
    peter.legs = 2
    print(f'{peter.__dict__}')