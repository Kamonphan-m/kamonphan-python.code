print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

total_seconds = int(input("Enter seconds: "))

hours = total_seconds // 3600

remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60

seconds = remaining_seconds % 60

print(f"{total_seconds} seconds = {hours} hour(s), {minutes} minute(s), {seconds} second(s)")