items = int(input("Number of items: "))
total_price = 0
for i in range(items):
    price = float(input("Price of item: "))
    total_price += price
if total_price > 100:
    discount = (total_price*10)/100
    final_prize = total_price - discount
else:
    final_prize = total_price
print(f"Total price for {items} is ${final_prize}")
