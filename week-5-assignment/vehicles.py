class Vehicle:
    def move(self):
        pass  # Base method (to be overridden)

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Create objects
vehicles = [Car(), Plane(), Boat()]

# Polymorphism in action
for v in vehicles:
    v.move()
