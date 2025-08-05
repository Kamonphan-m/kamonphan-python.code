"""

Personal Finance Calculator

Student: Kamonphan Mongkonsim

Date: 27 July 2025

Purpose: Calculate monthly budget and savings

"""
 
# ขอข้อมูลรายได้และค่าใช้จ่ายจากผู้ใช้

monthly_income = float(input("Enter your monthly income (THB): "))  # รายได้ต่อเดือน

rent_cost = float(input("Enter your rent cost (THB): "))  # ค่าเช่าบ้าน

food_budget = int(input("Enter your food budget (THB): "))  # ค่ากินต่อเดือน

transportation_cost = float(input("Enter your transportation cost (THB): "))  # ค่าเดินทาง

entertainment_budget = int(input("Enter your entertainment budget (THB): "))  # ค่าพักผ่อน

emergency_fund_percent = float(input("Enter emergency fund percentage (e.g., 10.5): "))  # เปอร์เซ็นต์เงินฉุกเฉิน

investment_percent = float(input("Enter investment percentage (e.g., 15.0): "))  # เปอร์เซ็นต์เงินลงทุน
 
# คำนวณค่าใช้จ่ายคงที่: ค่าเช่า + ค่าเดินทาง

total_fixed_expenses = rent_cost + transportation_cost
 
# คำนวณค่าใช้จ่ายไม่คงที่: ค่ากิน + ค่าพักผ่อน

total_variable_expenses = food_budget + entertainment_budget
 
# รวมค่าใช้จ่ายทั้งหมด

total_expenses = total_fixed_expenses + total_variable_expenses
 
# รายได้คงเหลือหลังหักค่าใช้จ่าย

remaining_income = monthly_income - total_expenses
 
# เงินฉุกเฉินที่ต้องเก็บ (เป็นเปอร์เซ็นต์ของรายได้)

emergency_fund_amount = monthly_income * (emergency_fund_percent / 100)
 
# เงินลงทุนที่ต้องเก็บ (เป็นเปอร์เซ็นต์ของรายได้)

investment_amount = monthly_income * (investment_percent / 100)
 
# เงินเหลือสำหรับออม

available_for_savings = remaining_income - emergency_fund_amount - investment_amount
 
# สัดส่วนค่าใช้จ่ายเทียบกับรายได้

expense_ratio = (total_expenses / monthly_income) * 100
 
# แสดงผลลัพธ์ทั้งหมดออกทางหน้าจอ

print("\n=== MONTHLY BUDGET REPORT ===")

print(f"Income: {monthly_income:.2f} THB")

print(f"Fixed Expenses: {total_fixed_expenses:.2f} THB")

print(f"Variable Expenses: {total_variable_expenses:.2f} THB")

print(f"Total Expenses: {total_expenses:.2f} THB")

print(f"Remaining: {remaining_income:.2f} THB")
 
print("\n=== SAVINGS BREAKDOWN ===")

print(f"Emergency Fund ({emergency_fund_percent}%): {emergency_fund_amount:.2f} THB")

print(f"Investment ({investment_percent}%): {investment_amount:.2f} THB")

print(f"Available for Savings: {available_for_savings:.2f} THB")
 
print("\n=== ANALYSIS ===")

print(f"Expense Ratio: {expense_ratio:.2f}%")
