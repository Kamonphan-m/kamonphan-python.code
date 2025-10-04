"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers"""

def number_operations():
   numbers = []
   # Get 10 numbers from user
   print("Enter 10 numbers:")
   for i in range(10):
       num = float(input(f"Number {i+1}: "))
       numbers.append(num)
   # Display original list
   print(f"\nOriginal numbers: {numbers}")
   # Create filtered lists
   even_numbers = [n for n in numbers if n % 2 == 0]
   odd_numbers = [n for n in numbers if n % 2 != 0]
   # Calculate average
   total = sum(numbers)
   average = total / len(numbers)
   # Numbers greater than average 
   above_average = [n for n in numbers if n > average]
   # Display results
   
   print("\nEven numbers: {even_numbers}")
   print("Odd numbers: {odd_numbers}")
   print("Numbers greater than average ({average:.2f}): {above_average}")
   print("\nStatistics:")
   print("Sum: {total}")
   print("Average: {average:.2f}")
   print("Min: {min(number)}")
if __name__ == "__main__":
    number_operations()



