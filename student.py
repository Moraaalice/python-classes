class Student:
    def __init__( self,first_name,last_name,age,nationality):
       self.firstname = first_name
       self.lastName = last_name 
       self.age = age
       self.nationality = nationality
    
    def full_name(self):
        return f"My name is {self.first_name} {self.last_name}" 
    
    def year_of_birth(self):
        year_of_birth = 2023 - {self.age}
        return f"My year of birth is {year_of_birth}"
       

