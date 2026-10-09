"""
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes
"""

# Base class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"


# Derived class
class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        # เรียกใช้งาน __init__ ของ Vehicle (Base class)
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        # เรียก get_info() ของ Vehicle และเพิ่มข้อมูล number_of_doors
        base_info = super().get_info()
        return f"{base_info}, Doors: {self.number_of_doors}"

if __name__ == "__main__":
    # สร้าง object จากคลาส Vehicle
    v1 = Vehicle("Toyota", "Corolla", 2020)
    print("Vehicle Info:", v1.get_info())

    # สร้าง object จากคลาส Car
    c1 = Car("Honda", "Civic", 2022, 4)
    print("Car Info:", c1.get_info())