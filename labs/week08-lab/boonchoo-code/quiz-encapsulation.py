"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle:
    def __init__(self, length, width):
        # Private attributes (ขึ้นต้นด้วย __)
        self.__length = length
        self.__width = width

    # Method คำนวณพื้นที่ (กว้าง x ยาว)
    def getArea(self):
        return self.__length * self.__width

    # Method คำนวณความยาวรอบรูป (2 x (กว้าง + ยาว))
    def getPerimeter(self):
        return 2 * (self.__length + self.__width)

    # Method เช็คว่าเป็นสี่เหลี่ยมจัตุรัสหรือไม่ (ความยาวเท่ากับความกว้าง)
    def isSquare(self):
        return self.__length == self.__width


# --- ตัวอย่างการทดสอบใช้งาน ---
if __name__ == "__main__":
    rect1 = Rectangle(5, 5)
    print("Area:", rect1.getArea())            # Outputs: 25
    print("Perimeter:", rect1.getPerimeter())  # Outputs: 20
    print("Is Square?:", rect1.isSquare())      # Outputs: True

    print("-" * 20)

    rect2 = Rectangle(4, 8)
    print("Area:", rect2.getArea())            # Outputs: 32
    print("Perimeter:", rect2.getPerimeter())  # Outputs: 24
    print("Is Square?:", rect2.isSquare())      # Outputs: False