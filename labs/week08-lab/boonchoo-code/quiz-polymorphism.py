"""
Demonstrate polymorphism by creating:

    A base class Animal with method move()
    Three derived classes: Fish, Bird, Dog with different implementations of move()
        fish swims, bird flies, dog runs
    A function that takes any animal and calls its move() method
"""
# Base class
class Animal:
    def move(self):
        pass

# Derived classes
class Fish(Animal):
    def move(self):
        print("Fish swims")

class Bird(Animal):
    def move(self):
        print("Bird flies")

class Dog(Animal):
    def move(self):
        print("Dog runs")

# Function Demonstrating Polymorphism
def make_animal_move(animal):
    animal.move()

# --- ตัวอย่างการทดสอบใช้งาน ---
if __name__ == "__main__":
    fish = Fish()
    bird = Bird()
    dog = Dog()
    
    # เรียกใช้ฟังก์ชันเดียวกับ object ต่างชนิดกัน
    make_animal_move(fish)  # Prints: Fish swims
    make_animal_move(bird)  # Prints: Bird flies
    make_animal_move(dog)   # Prints: Dog runs