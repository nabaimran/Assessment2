# Vending Machine Program 

# List of items available (drinks and snacks) with prices
menu = {
    1: {'name': 'Coke', 'price': 1.50},
    2: {'name': 'Pepsi', 'price': 1.40},
    3: {'name': 'Water', 'price': 1.00},
    4: {'name': 'Chips', 'price': 1.20},
    5: {'name': 'Chocolate', 'price': 1.70}
}

def display_menu():
    """Function to display the menu of items to the user."""
    print("\nMenu:")
    for code, item in menu.items():
        print(f"{code}. {itemt["name"]} - ${item['price']:.2f}")

def get_money():
    """Function to ask the user for money input."""
    while True:
        try:
            # ask the user to enter money amount
            money = float(input("\nInsert money (in dollars): $"))
            if money <=0:
                print("Please insert a valid amount of money.")
            else:
                return money 
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            