from person import Person

class Student(Person):
    def __init__(self,name,facuity,major,year) -> None:
        super().__init__(name)
        self.faculty = facuity
        self.major = major
        self.year = year
        
    def welcome(self):
        super().welcome()
        print(f'Welcome to {self.faculty} major{self.major} in {self.year}')
