# Vending machine program

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
        print(f"{code}. {item['name']} - ${item['price']:.2f}")

def get_money():
    """Function to ask the user for money input."""
    while True:
        try:
            # Ask the user to enter money amount
            money = float(input("\nInsert money (in dollars): $"))
            if money <= 0:
                print("Please insert a valid amount of money.")
            else:
                return money
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def select_item():
    """Function to select an item from the menu."""
    while True:
        try:
            choice = int(input("\nEnter the code for the item you want: "))
            if choice in menu:
                return choice
            else:
                print("Invalid code. Please select a valid item.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_change(item_price, money_inserted):
    """Function to calculate and return change if any."""
    if money_inserted >= item_price:
        return round(money_inserted - item_price, 2)
    return None  # Insufficient funds