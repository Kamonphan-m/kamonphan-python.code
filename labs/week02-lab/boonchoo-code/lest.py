print("Now try these exercises:") #ข้อที่1
print()
print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

PI = 3.14159
 number (float)
radius = float(input("Please enter the radius of the circle: "))

area = PI * (radius ** 2)
circumference = 2 * PI * radius

print("--- Calculation Results ---")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")


