# Define the market's items and their prices
market_items = {
    "apple": {"price": 1.00},
    "banana": {"price": 0.50},
    "orange": {"price": 0.75},
    "grape": {"price": 1.50},
    "watermelon": {"price": 4.00}
}

# Request the customer's available funds
available_funds = float(input("Please enter the amount of money you have: $"))

# Print the market's items and their prices
print("Here are the items we have in the market and their corresponding prices:")
for item, details in market_items.items():
    print(f"{item.title()} (${details['price']:.2f})")

# Create an empty dictionary to store the customer's items and their quantities
customer_items = {}

# Allow the customer to choose which items and quantities they want to purchase
while True:
    # Print the customer's remaining funds and prompt them to choose an item and quantity
    print(f"\nYou have ${available_funds:.2f} remaining.")
    item_choice = input("Please choose an item to purchase (or 'done' to finish shopping): ").lower()

    # If the customer is done shopping, break out of the loop
    if item_choice == "done":
        break

    # Check if the item exists in the market
    if item_choice not in market_items:
        print("That item is not available in the market. Please choose another item.")
        continue

    # Request the quantity of the chosen item
    while True:
        quantity_choice = input(f"How many {item_choice}s do you want to buy? ")

        # Check if the quantity is a valid integer
        try:
            quantity_choice = int(quantity_choice)
        except ValueError:
            print("Invalid quantity. Please enter a valid integer.")
            continue

        # If the customer does not have enough funds for the chosen quantity of item, continue to the next iteration of the loop
        if available_funds < quantity_choice * market_items[item_choice]["price"]:
            print("You do not have enough money to purchase that many items. Please choose a smaller quantity.")
            continue

        # If the customer has enough funds for the chosen quantity of item, deduct the item's total price from their funds and add the item and quantity to their dictionary
        available_funds -= quantity_choice * market_items[item_choice]["price"]
        if item_choice in customer_items:
            customer_items[item_choice] += quantity_choice
        else:
            customer_items[item_choice] = quantity_choice
        break

# Print the customer's final list of purchased items and their remaining funds
print("\nHere are the items you have purchased:")
for item, quantity in customer_items.items():
    print(f"{quantity} {item.title()}(s)")
print(f"Your remaining funds are ${available_funds:.2f}.")
