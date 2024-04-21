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

    def change_color(self):
        self.color = input("Enter the color: ")

car = Car("Red", "GT321", "Diesel", 2024, "Mercedez_Benz")
print(car.color, car.model, car.engine_type, car.year_built, car.brand_name)
car.acceleration()
car.brakes()
print()

#Inheritance
class suv(Car):
    def __init__(self, color, model, engine_type, year_built, brand_name, Transmission):
        Car.__init__(self, color, model, engine_type, year_built, brand_name)
        self.Transmission = Transmission

cars = suv("Blue", "GT321", "Petrol", 2022, "Honda_Civic", "Automatic")
cars.acceleration()
cars.change_color()