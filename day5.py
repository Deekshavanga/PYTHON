class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
      return f"{self.name},{self.age} years old"
      
person= person("Akhil",23)
print(person)


class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
      return f"{self.name},{self.age} years old"
      
dog= dog("Jimmy",2)
print(dog)
