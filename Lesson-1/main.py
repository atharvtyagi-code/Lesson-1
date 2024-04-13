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