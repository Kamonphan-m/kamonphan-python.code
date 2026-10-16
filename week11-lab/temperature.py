"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
# === TEMPERATURE ANALYSIS ===

# 1. ฟังก์ชันรับค่าอุณหภูมิ 7 วัน และเก็บใน list
def get_temperatures():
    temps = []
    print("Enter temperature for 7 days:")
    for i in range(1, 8):
        # เพื่อความสะดวกและกัน error สามารถใช้ค่ากำหนดไว้ล่วงหน้า หรือรับ input ได้
        # ในที่นี้ใช้ input ตามรูปแบบการบ้านทั่วไป
        t = float(input(f"Day {i}: "))
        temps.append(t)
    return temps

# 2. ฟังก์ชันคำนวณค่าเฉลี่ย ค่าสูงสุด ค่าต่ำสุด และคืนค่าเป็น tuple
def analyze_temps(temp_list):
    avg = sum(temp_list) / len(temp_list)
    high = max(temp_list)
    low = min(temp_list)
    return avg, high, low

# 3. ฟังก์ชันแสดงผลลัพธ์ให้ออกมาสวยงามตรงตามรูปแบบตัวอย่าง
def display_analysis(avg, high, low):
    print("\nTemperature Analysis for the Week:")
    print(f"Average: {avg:.1f} C")
    print(f"Highest: {high} C")
    print(f"Lowest: {low} C")

# ส่วนหลักในการรันโปรแกรม (Main Execution)
if __name__ == "__main__":
    week_temps = get_temperatures()
    average_temp, highest_temp, lowest_temp = analyze_temps(week_temps)
    display_analysis(average_temp, highest_temp, lowest_temp)
    