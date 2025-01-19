# Vending Machine Program SA2

print("""
                     █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▀█▀ █░█ █▀▀   █▀ █▀▄▀█ ▄▀█ █▀█ ▀█▀  
                     ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ░█░ █▀█ ██▄   ▄█ █░▀░█ █▀█ █▀▄ ░█░  

                            █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀  █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
                            ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█  █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄""")

# Dictionary of products categorized
Products = {
    'Drinks': {
        1: {'name': 'Granola Bars', 'price': 2.0, 'stock': 7, 'code': 1},
        2: {'name': 'Cookie', 'price': 3.0, 'stock': 8, 'code': 2},
        3: {'name': 'Water', 'price': 2.0, 'stock': 8, 'code': 3},
        4: {'name': 'Coke', 'price': 1.5, 'stock': 5, 'code': 4},
        5: {'name': 'Pepsi', 'price': 1.4, 'stock': 5, 'code': 5},
        6: {'name': 'Ice tea', 'price': 4.0, 'stock': 5, 'code': 6}
    },
    'Snacks': {
        7: {'name': 'Chicken Sandwich', 'price': 3.0, 'stock': 8, 'code': 7},
        8: {'name': 'Chips', 'price': 1.2, 'stock': 5, 'code': 8},
        9: {'name': 'Chocolate', 'price': 1.7, 'stock': 5, 'code': 9},
        10: {'name': 'Biscuits', 'price': 1.0, 'stock': 5, 'code': 10}
    }
}

# Suggestions for the customers
suggestions = {
    1: 8,   # Granola Bars -> Chips
    2: 10,  # Cookie -> Biscuits
    3: 8,   # Water -> Chips
    4: 10,  # Coke -> Biscuits
    5: 10,  # Pepsi -> Biscuits
    6: 9,   # Ice Tea -> Chocolate
    7: 4,   # Chicken Sandwich -> Coke
    8: 3,   # Chips -> Water
    9: 4,   # Chocolate -> Coke
    10: 6   # Biscuits -> Ice Tea
}

def display_menu():
    """Display the categorized menu."""
    print("\nAvailable Products:")
    for category, items in Products.items():
        print(f"\n{category}:")
        for code, item in items.items():
            stock = "Out of stock" if item['stock'] == 0 else f"${item['price']:.2f}"
            print(f"{code}. {item['name']} - {stock}")

def get_money():
    """Get money input from the user."""
    while True:
        try:
            money = float(input("\nInsert money (in AED): "))
            if money <= 0:
                print("Please insert a valid amount of money.")
            else:
                return money
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def select_item():
    """Select an item from the menu."""
    while True:
        try:
            choice = int(input("\nEnter the code for the item you want: "))
            for category in Products.values():
                if choice in category:
                    item = category[choice]
                    if item['stock'] == 0:
                        print(f"Sorry, {item['name']} is out of stock.")
                    else:
                        return item
            print("Invalid code. Please select a valid item.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def update_stock(item_code):
    """Update the stock of the purchased item."""
    for category in Products.values():
        if item_code in category:
            category[item_code]['stock'] -= 1


def vending_machine():
    """Main function to handle purchases."""
    while True:
        display_menu()

        # Select an item
        item = select_item()
        print(f"\nYou selected: {item['name']} which costs AED {item['price']:.2f}")

        # Insert money
        money_inserted = get_money()

        # Check if enough money is inserted
        if money_inserted < item['price']:
            print(f"Not enough money. You inserted AED {money_inserted:.2f} but {item['name']} costs AED {item['price']:.2f}.")
            print("Transaction canceled. Please try again.")
            continue

        # Calculate change
        change = round(money_inserted - item['price'], 2)

        # Dispense the item and update stock
        update_stock(item['code'])
        print(f"\nDispensing {item['name']}...")

        # Display change if any
        if change > 0:
            print(f"Change returned: AED {change:.2f}")
        else:
            print("No change to return.")

        # Suggest complementary item
        if item['code'] in suggestions:
            suggested_item_code = suggestions[item['code']]
            for category in Products.values():
                if suggested_item_code in category:
                    suggested_item = category[suggested_item_code]
                    if suggested_item['stock'] > 0:
                        add_on = input(f"Would you like to add {suggested_item['name']} for AED {suggested_item['price']:.2f}? (yes/no): ").lower()
                        if add_on == 'yes':
                            if money_inserted >= item['price'] + suggested_item['price']:
                                update_stock(suggested_item_code)
                                print(f"Dispensing {suggested_item['name']}...")
                                change = round(money_inserted - (item['price'] + suggested_item['price']), 2)
                                if change > 0:
                                    print(f"Updated change returned: AED {change:.2f}")
                                break
                            else:
                                print("Not enough money for the additional item.")

        # Ask if the user wants to buy more items
        more_items = input("\nWould you like to purchase another item? (yes/no): ").lower()
        if more_items != 'yes':
            print("Thank you for using the vending machine!")
            break

# Run the vending machine
vending_machine()
