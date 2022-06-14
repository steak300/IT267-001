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
        
#create object
ula = Animal()
ula.new_animal