# Shopping Calculator Template

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# TODO: Calculate subtotal
# TODO: Calculate discount amount
# TODO: Calculate price after discount
# TODO: Calculate tax amount
# TODO: Calculate final total
# TODO: Display itemized receipt


item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

subtotal = item_price * quantity
discount_amount = subtotal * (discount_percent / 100)

price_after_discount = subtotal - discount_amount

tax_amount = price_after_discount * (tax_percent / 100)

final_total = price_after_discount + tax_amount

print("\n" + "="*30)
print("       SHOPPING RECEIPT       ")
print("==========" + "====================")
print(f"Subtotal:         ${subtotal:.2f}")
print(f"Discount ({discount_percent}%):  -${discount_amount:.2f}")
print(f"Price After Disc: ${price_after_discount:.2f}")
print(f"Tax ({tax_percent}%):       +${tax_amount:.2f}")
print("-"*30)
print(f"TOTAL AMOUNT:     ${final_total:.2f}")
print("="*30)