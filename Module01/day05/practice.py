from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def describe(self):
        print(f"Vehicle: {self.make} {self.model}")

    # 5. Abstract method that subclasses must implement
    @abstractmethod
    def wheels(self) -> int:
        pass


# 1. Car Subclass
class Car(Vehicle):
    # 5. Implementing the abstract wheels method
    def wheels(self) -> int:
        return 4


# 1, 2 & 3. Truck Subclass extending Vehicle
class Truck(Vehicle):
    # 2. Using super().__init__() and adding a new attribute
    def __init__(self, make: str, model: str, capacity: float):
        super().__init__(make, model)
        self.capacity = capacity  # In tons

    # 3. Overriding the describe() method
    def describe(self):
        print(f"Truck: {self.make} {self.model} with a hauling capacity of {self.capacity} tons")

    # 5. Implementing the abstract wheels method
    def wheels(self) -> int:
        return 6


# --- Running and verifying the code ---
if __name__ == "__main__":
    
    # 4. Polymorphism: Create a list containing different vehicle types
    fleet = [
        Car("Toyota", "Corolla"),
        Truck("Isuzu", "FSR", 8.5),
        Car("Hyundai", "Atos"),
        Truck("Volvo", "FH16", 25.0)
    ]

    print("--- 4. Testing Polymorphism (describe method) ---")
    # Loop over the vehicles and call describe() on each
    for vehicle in fleet:
        vehicle.describe()

    print("\n--- 5. Testing Abstract Method (wheels method) ---")
    # Loop over the vehicles and call wheels() on each
    for vehicle in fleet:
        print(f"{vehicle.make} {vehicle.model} has {vehicle.wheels()} wheels.")
