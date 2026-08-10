items = ["pencil", "eraser", "notebook", "sharpener", "glue"]

stock_counts = [12, 0, 8, 5, 3]

inventory = {item : count for item, count in zip(items, stock_counts)}
print("The school inventory is: " + str(inventory))

in_stock_items = [item for item in items if inventory[item] > 0]
print("Items in stock: " + str(in_stock_items))

chosen_item = input("Enter the item you want to check: ")
if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(f"Sorry, {chosen_item} is out of stock.")
    exit()

prices = [10, 5, 20, 15, 8]
markup_amount = int(input("Enter the markup amount: "))

marked_up_prices = list(map(lambda price: price + markup_amount, prices))
print("Marked up prices: " + str(marked_up_prices))

items_index = items.index(chosen_item)
chosen_item_price = marked_up_prices[items_index]
print(f"The price of {chosen_item} is ${chosen_item_price}.")

inventory[chosen_item] = inventory[chosen_item] - 1
print(f"Updated inventory after selling {chosen_item}: " + str(inventory))

print("")
print("===== SCHOOL STORE INVENTORY CHECKER =====")
print("Items bought: " + str(chosen_item))
print("Price paid: $" + str(chosen_item_price))
print("updated inventory: " + str(inventory))