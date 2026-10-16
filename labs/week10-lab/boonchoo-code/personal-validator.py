"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210
"""

# === PERSONAL INFORMATION VALIDATOR ===

print("=== PERSONAL INFORMATION VALIDATOR ===")

# 1. รับค่าข้อมูลจากผู้ใช้
name = input("Enter your name: ")
age_str = input("Enter your age: ")
phone = input("Enter your phone number: ")

# 2. ตรวจสอบชื่อ (ต้องเป็นตัวอักษรและเว้นวรรคเท่านั้น โดยใช้ isalpha())
# ใช้ replace เพื่อเอาช่องว่างออกก่อนเช็ค isalpha()
name_check = name.replace(" ", "")
if len(name) > 0 and name_check.isalpha():
    name_status = "Valid (contains only letters and spaces)"
else:
    name_status = "Invalid"

# 3. แปลงอายุเป็น int และตรวจสอบช่วง 18-65 (โดยใช้ isdigit())
if age_str.isdigit():
    age = int(age_str)
    if 18 <= age <= 65:
        age_status = "Valid ({} years old)".format(age)
    else:
        age_status = "Invalid (Age must be between 18-65)"
else:
    age = 0
    age_status = "Invalid (Must be numbers)"

# 4. ตรวจสอบเบอร์โทรศัพท์ (ต้องเป็นตัวเลข 10 หลัก โดยใช้ isdigit())
if phone.isdigit() and len(phone) == 10:
    phone_status = "Valid (10-digit number)"
else:
    phone_status = "Invalid"

# 5. แสดงผลลัพธ์การตรวจสอบ
print("\nValidation Results:")
print("Name: {}".format(name_status))
print("Age: {}".format(age_status))
print("Phone: {}".format(phone_status))

# 6. แสดงข้อมูลที่จัดรูปแบบแล้ว (ใช้ upper() และ .format())
print("\nFormatted Information:")
print("Name: {}".format(name.upper()))

# กำหนดกลุ่มอายุตามช่วง
if 18 <= age <= 30:
    age_group = "Young Adult (18-30)"
elif 31 <= age <= 65:
    age_group = "Adult (31-65)"
else:
    age_group = "General"

print("Age Group: {}".format(age_group))
print("Phone: +91-{}".format(phone))