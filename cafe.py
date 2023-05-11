# Defining the menu, the stock and the price for each item on the menu.
menu = ["Smoothie", "Juice", "Apple", "Cake"]
stock = {"Smoothie": 30, "Juice": 40, "Apple": 20, "Cake": 10}
price = {"Smoothie": 4.0, "Juice": 2.0, "Apple": 1.0, "Cake": 4.0}

# Loop to calculate the total stock worth and printing the result.
total_stock = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

print("The total stock worth in the cafe is £" + str(total_stock))