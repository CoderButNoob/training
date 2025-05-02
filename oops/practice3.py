class Dog :
    species = "Pug"
    count = 0

    def __init__(self , name, age):
        self.name = name 
        self.age = age 
        Dog.count += 1
    
    def speak(self):
        print(f"{self.name} says hello")
        
    
    @classmethod
    def change_species(slef,new_species):
        Dog.species = new_species

    @staticmethod
    def general_info():
        print("Dogs are good")

print(Dog.species)
Dog.general_info()
Dog.change_species("Gali ka Kutta")
print(Dog.species)
dog1 = Dog("Lucy" ,3)
dog2 = Dog("Bubble" , 4)

dog1.speak()
dog2.speak()
print("Total Count" , Dog.count)