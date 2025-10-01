print("Welcome to the shop!!!")
item = ["apple", "banana", "carrot", "durian", "eggplant", "grape"]
price = [1, 1.50, 1, 3, 2, 1]
full_order=[]
full_price=0
while True:
    print("\nThe items and prices are:")
    for i in range(len(item)):
        print(i + 1, ".", item[i], "--", price[i], "$")

    # Loop until integer input
    while True:
        order = input("What would you like to buy? (input number) ")
        try:
            order = int(order)
            if 1 <= order <= len(item):   # Check if in range
                break
            else:
                print("Please enter a number between 1 and", len(item))
        except ValueError:
            print(" Thats not a valid number, try again.")
    #Single item checkout
    print("You bought a", item[order - 1], "for", price[order - 1], "$")
    full_order.append(item[order-1]) #add item to full order
    full_price+=price[order-1]
    again = input("Do you want to buy more? (yes/no) ") # buy again?
    if again not in ["yes", "y", "Yes"]:
        print("You bought:",full_order, "and costs", full_price,"$.")
        discount=input("Do you have a discount code?")
        if discount == "yes":
            full_price=full_price/10*7.5
            print("Your new price is",full_price,"$")
        print("Thanks for shopping! ")
        break
