class student:
    def __init__(self,id:str,name:str,major:str) -> None:
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
    Jessica = student(111,"Jessica","IT")
    John = student(112,"John","MKT")

    Jessica.display_detail()
    John.display_detail()
