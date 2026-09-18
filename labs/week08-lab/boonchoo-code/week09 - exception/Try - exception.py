#ERRORS (bugs)
# 3 types => snytax errors / runtime error / logic error

age = int(input("Insert your age (!!!NUMBER ONLYE!!!): ")) #runtime error
print(age)

#ValueError Exception
try:
    age = int(input("กรอกอายุ : "))
    print (f"ปีหน้าคุณจะอายุ {age + 1} ปี")
except ValueError :#ทำหน้าที่ดักจับ error
    print ("กรอกอายุเป็นตัวเลขจำนวนเต็ม เช่น 20")
    
#ZeroDivisionException
try:
    numerator = float(input("กรอกตัวตั้ง :"))
    denominator = float(input("กรอกตัวหาร :"))
    
    result = numerator / denominator
    print(f"ผลลัพธ์ = {result}")
    
except ValueError:
    print("กรุณากรอกตัวเลขให้ถูกต้อง")
    
except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")
    
#FileNotFoundException, PermissionException สามารถทำงานรวมกับไฟล์อื่นได้เพื่อเข้าไปอ่านดาต้า
try:
    filename = input("ชื่อไฟล์ : ")
    
    with open(filename , "r" , encoding="utf - 8") as file:
        content = file.read()
        
        print("เนื้อหาในไฟล์")
        print(content)
        
except FileNotFoundError :
    print(f"ไม่พบไฟล์ชื่อ {filename}")
    
except PermissionError :
    print("ไม่มีสิทธิ์เข้าถึงไฟล์นี้")
    
#raise ใช้สำหรับ สั่งให้ Python สร้าง Exception ขึ้นเอง เมื่อข้อมูลหรือสถานการณ์ไม่เป็นไปตาม
#แม้คำสั่งนั้นจะไม่ผิดไวยากรณ์และ Python ยังทำงานต่อไปได้ตามปกติก็ตาม

try:
    score = float(input("กรอกคะแนน 0-100 : "))
    
    if not 0 <= score <= 100 : #เข้าเมื่อมีความผิดปกติ เลขไม่อยู่ระหว่าง 0-100
        raise ValueError("คะแนนต้องอยู่ระหว่าง 0 ถึง 100")
    
except ValueError as error: #เข้าเมื่อมีความผิดปกติ
    print(f"ข้อมูลไม่ถูกต้อง: {error}")
    
else:#เมื่อไม่เข้าในเงื่อนไขของ except ก็จะมาเข้าใน else ทำเมื่อไม่ผิดจึงเข้า else
    print(f"บันทึกคะแนน {score} เรียบร้อย")
    
finally:#เข้าเสมอ
    print("จบการตรวจสอบคะแนน")