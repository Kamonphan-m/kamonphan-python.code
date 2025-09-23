import random

#refactor != debug

def test_random():
   
    # สุ่มเลขระหว่าง 1 - 10 เก็บไว้ในตัวแปรชื่อ dandom_number
    random_number = random.randint(1, 100)
   
    # รับค่าการทายเลขจากผู้ใช้ เก็บไว้ในตัวแปรชื่อ guess_number
    guess_number = input("What is your guess number?:")

    if random_number == guess_number:
        print("Congratulations")

    if random_number < guess_number:
        print("Too much")

    print(random_number)


test_random()