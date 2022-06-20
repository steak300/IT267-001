class Person:
    country = "Thailand" #class variabe
    def __init__(self,name,gender,profession,hours) -> None:
        #instance variables
        self.name = name
        self.gender = gender
        self.profession = profession
        self.hours = hours
    
    def work(self):
        print(f"{self.name} is working as a {self.profession}")
    
    def study(self):
        print(f"{self.name} studie for {self.hours} hour(s)")
        
    def show(self):
        print(f"Name: {self.name} Gender: {self.gender} Profession: {self.profession} Study: {self.hours}")
        
    
jessa = Person("Jessa","Male","Software Engineer",10)
jon = Person("Jon","Male","Doctor",15)
Lalisa =Person("Lalisa","Female","Korean Singer",13)

Lalisa.work()
print(f"class Variabe: {Person.country}")
print(f"Instance Variable: {Lalisa.country}")

#assign value
Lalisa.country = "Korea"
print(f"class Variabe: {Person.country}")
print(f"Instance Variable: {Lalisa.country}")
print(f"Instance Variable: {jon.country}")

#assign class variable
Person.country = "England"
print(f"class Variabe: {Person.country}")
print(f"Instance Variable: {Lalisa.country}")
print(f"Instance Variable: {jon.country}")