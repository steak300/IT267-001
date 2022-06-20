class Student:
    def __init__(self,id:str,name:str,major:str = "IT") -> None:
        #instance variables
        self.id = id
        self.name = name
        self.major = major
    
    def display_detail(self):
        print(f"***********")
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"major: {self.major}")
        
    def __del__(self):
        print(f'Object was destoryed')

if __name__ == "__main__":        
    Jessica = Student(111,"Jessica","IT")
    John = Student(112,"John","MKT")
    amy = Student("113","Amy")
    
    Jessica.display_detail()
    John.display_detail()
    amy.display_detail()
    
