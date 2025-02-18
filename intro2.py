class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am studying {self.course}.")

# Creating three student objects
student1 = Student("Jude Franz Casilagan", 19, "Criminology")
student2 = Student("Jedidiah Dave Eco", 19, "Computer Studies")
student3 = Student("Lance Patrick Canaber", 19, "tourism")

# Calling the introduce method for each student
student1.introduce()
student2.introduce()
student3.introduce()