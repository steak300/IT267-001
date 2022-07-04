from animal import Animal

class Dog(Animal):
    def info(self):
        #super().info()
        Animal.info(self)
        print('I am a dog.')
        print(f'My name is {self.name}')
        print(f'I am {self.age} years old.')

class Cat(Animal):
    pass

class Cow(Animal):
    pass