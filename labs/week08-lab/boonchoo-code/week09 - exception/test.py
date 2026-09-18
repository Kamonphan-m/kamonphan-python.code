"""
โจทย์ 1 : เครื่องคำนวณอย่างปลอดภัย
เขียนโปรแกรมรับตัวเลข 2 จำนวนและตัวดำเนินการ 1 ตัว ได้แก่ + - * / แล้วแสดงผลลัพธ์
โปรแกรมต้องจัดการกรณีต่อไปนี้
ฺิฺ- ผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข 
# ValueError 
- ผู้ใช้ตัวเลขดำเนินอื่นนอกจาก + - * / raise VaeError
- ผู้ใช้พยายามหารด้วยศูนย์
# ZerodivisionError
- โปรแกรมต้องแสดง จบการทำงาน เสมอด้วย fianlly

ตัวอย่างผลลัพธ์ที่คาดหวัง
ตัวเลขที่ 1: 10 
ตัวเลขที่ 2: 0 
เครื่องหมาย ( +,-,*,/)

ไม่สามารถหารด้วยศูนย์ได้
"""

try:
    num1 = float(input("ตัวเลขที่ 1:"))
    num2 = float(input("ตัวเลขที่ 2:"))
    operator = input("เครื่องหมาย (+,-,*,/):")

    result = 0
    if operator == "+":
        result = num1 + num2 
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("เครื่องหมายต้องเป็น + - * / เท่านั้น")

    print(f"{num1} {operator} {num2} = {result}")

except ValueError: # กรณีผู้ใช้ไท่พิมตัวเลข
    print("กรุณาเป็นตัวเลขเท่านั้น!")

except ZeroDivisionError: #กรณีผู้ใช้ใส่ตัวหาร 0 
    print("ไม่สามารถหารด้วยศูนย์ได้")

except Exception: #กรณีอื่นๆ
    print("ทำอะไรไม่ได้บางอย่างแต่ไม่แน่ใจ")

else: #จะทำที่นี่ก็ต่อเมื่อไม่มี exception
    print("คำนวณการทำงานเรียบร้อยแล้ว")

finally:
    print("จบการทำงาน")