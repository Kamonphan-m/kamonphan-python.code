# Complete this program to classify people by age
age = int(input("Enter age: "))
if age < 0:
    print("Invalid age ")
elif age <= 12:
    print("Child ")
elif age <= 19:
    print("Teenager ")
elif age <= 59:
    print("Adult ")
else:
    print("Senior")



# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here: