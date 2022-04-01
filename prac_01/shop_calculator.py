num_items = int(input("Enter number of items: "))

total_price = 0

for i in range(num_items):
    price = float(input("Price of item: "))
    total_price += price

if total_price >= 100:
    discount = total_price * 0.10
    total_price -= discount

print("Total price of {} items is {}".format(num_items, total_price))
