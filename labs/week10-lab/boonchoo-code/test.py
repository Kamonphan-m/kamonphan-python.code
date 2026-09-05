# รับค่า text จากผู้ใช้
text = input("Insert your text: ")

# รับตัวอักษรที่ต้องการค้นหา
character = input("Character to find: ")

# นับจำนวนตัวอักษรที่ค้นหา
count = text.lower().count(character.lower())

# แสดงผลลัพธ์
print(f"{count} letters '{character}' found in '{text}'")

print("\n=== TRAVERSING STRINGS ===")

message = "Kamonphan"

index = 0

print("\nMethod 1: Using for loop with enumerate()")
for i, char in enumerate(message):
    print(f"message[{i}] = {char}")

print("\nMethod 2: Manual indexing")
index = 0

for char in message:
    print(f"message[{index}] = {char}")
    index += 1