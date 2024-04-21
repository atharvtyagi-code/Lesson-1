class Car():
    #Constructor holds physical attributes
    def __init__(self, color, model, engine_type, year_built, brand_name):
        self.color = color
        self.model = model
        self.engine_type = engine_type
        self.year_built = year_built
        self.brand_name = brand_name
        self.velocity = 1

    def acceleration(self):
        self.velocity += 5
        print("Velocity increased")

    def brakes(self):
        self.velocity -= 2
        print("Velocity decreased")

car = Car("Red", "GT321", "Diesel", 2024, "Mercedez_Benz")
print(car.color)
car.acceleration()
car.brakes()
print()



class students():
    def __init__(self, name, age, gender, birth_date, grade):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_date = birth_date
        self.grade = grade

    def load(self):
        print("Retrieving information...")

print()
Student = students("Luke", 14, "Male", "June 8th 2010", "8th grade")
Student.load()
print()
print("Information retrieved:")
print(Student.name)
print(Student.age)
print(Student.gender)
print(Student.birth_date)
print(Student.grade)
