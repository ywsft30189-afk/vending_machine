# Simple Vending Machine Project
# This program simulates a simple vending machine

# Dictionary that stores products
# Each product has: name, price, and quantity
products = {
    1: ["Pepsi", 1.5, 5],        # Product number 1
    2: ["ships", 1.0, 7],        # Product number 2
    3: ["Chocolate", 2.0, 4],    # Product number 3
    4: ["Water", 0.5, 10],       # Product number 4
    5: ["Orangeu_juice", 2.5, 6]         # Product number 5
}

# Function to display all available products
def show_products():
    # Print a title for the products list
    print("\nAvailable Products:")
    
    # Loop through the products dictionar
    for key, value in products.items():
        # Print product number, name, price, and quantity
        print(f"{key}. {value[0]} - ${value[1]} (Quantity: {value[2]})")

# Main vending machine function
def vending_machine():
    # Infinite loop to keep the program running
    while True:
        # Show products to the user
        show_products()

        # Ask the user to choose a product
        choice = input("\nEnter product number (0 to exit): ")

        # If user enters 0, exit the program
        if choice == "0":
            print("Thank you for using the vending machine")
            break  # Stop the loop

        # Check if the input is not a number
        if not choice.isdigit():
            print("Please enter a valid number")
            continue  # Go back to the start of the loop

        # Convert the input from string to integer
        choice = int(choice)

        # Check if the product number exists
        if choice not in products:
            print("Product not found")
            continue

        # Check if the selected product is out of stock
        if products[choice][2] == 0:
            print("Sorry, this product is out of stock")
            continue

        # Ask the user to insert money
        money = float(input("Insert money: "))
        # Get the price of the selected product
        price = products[choice][1]

        # Check if the inserted money is not enough
        if money < price:
            print("not enough money")
            continue

        # Calculate the change
        change = money - price

        # Reduce the quantity of the product by 1
        products[choice][2] -= 1

        # Print purchase confirmation
        print("you bought:", products[choice][0])

        # Print the change rounded to 2 decimal places
        print("payment:", round(money, 2), "$")
        print("your change:", round(change, 2), "$")
        print("thank you for using the vending machine")

# Run the program
vending_machine()
