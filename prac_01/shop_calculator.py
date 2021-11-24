DISCOUNT_RATE = 0.1
MIN_TOTAL_PRICE = 100
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
total_price = 0                                                   # accumulator for total price
for i in range(1, number_of_items + 1):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > MIN_TOTAL_PRICE:
    total = total_price - (total_price * DISCOUNT_RATE)
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
