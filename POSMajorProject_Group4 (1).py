#POINT OF SALE ASSIGNMENT

# SHOWS THE PRODUCTS AND STOCK AVAILABILTY
products = {
    "rice": 200,
    "flour": 220,
    "milk": 300,
    "bread": 450,
    "eggs": 70,
    "sugar": 200,
    "juice": 350,
    "soap": 240,
    "toothpaste": 250,
    "water": 100
}

stock = {
    "rice": 15,
    "flour": 12,
    "milk": 25,
    "bread": 20,
    "eggs": 200,
    "sugar": 15,
    "juice": 20,
    "soap": 10,
    "toothpaste": 5,
    "water": 50
}

cart = {}

# THIS SHOWS THE PRODUCT
def show_products():
    print("\nPRODUCT LIST")
    for item in products:
        print(item, "-", "$", products[item], "stock:", stock[item])

# THIS ALLOWS YOU TO CHECK IF STOCK IS LOW OR NOT
def low_stock_alert():
    found = False

    for item in stock:
        if stock[item] < 5:
            if found == False:
                print("\nLOW STOCK ALERT")
            print(item, "is low! Only", stock[item], "left")
            found = True

    if found == False:
       pass #this does nothing

# THIS ALLOWS YOU TO ADD ITEMS
def add_item():
    item = input("Enter item name: ").lower()

    if item in products:
        try:
            quantity = int(input("Enter quantity:"))
        except:
            print("Invalid Input")
            return

        if quantity <= stock[item]:

            if item in cart:
                cart[item] = cart[item] + quantity
            else:
                cart[item] = quantity

            stock[item] = stock[item] - quantity
            print("Item added")
            if stock[item]<5:

#sends a message if the stock of the item is low
                print(f"Low stock alert for",{item})

        else:
            print("Not enough stock")

    else:
        print("Item not found")

# THIS ALLOWS YOU TO REMOVE ITEMS
def remove_item():
    item = input("Enter item to remove: ").lower()

    if item in cart:
        stock[item] = stock[item] + cart[item]
        del cart[item]
        print("Item removed")

    else:
        print("Item not in cart")

#THIS ALLOWS YOU TO VIEW THE ITEMS IN THE CART
def view_cart():
    print("\nCART")

    total = 0

    for item in cart:
        price = products[item] * cart[item]
        print(item, cart[item], "$", price)
        total = total + price

    print("Subtotal: $", total)

# THIS SHOWS THE CHECKOUT AND CALCULATIONS OF THE COST
def checkout():
    if not cart:
        print("Cart is empty")
        return
    total = 0

    for item in cart:
        total = total + (products[item] * cart[item])

    # SHOWS DISCOUNT - 5% IF TOTAL MORE THAN $5000
    discount = 0

    print("Debug total:",total)
    if total > 5000:
        discount = total * 0.05

    # SHOWS TAX - 10% TAX
    tax = (total - discount) * 0.10

    final_total = total - discount + tax

    print("\nCHECKOUT")
    print("Subtotal: $", total)
    print("Discount: $", discount)
    print("Tax: $", tax)
    print("Total: $", final_total)



    try:
        money = float(input("Enter payment: "))
    except:
        print("Invalid payment")
        return

    while money < final_total:
        print("Not enough money")
        money = float(input("Enter payment: "))

    change = money - final_total

    # SHOWS RECEIPT
    print("\nRECEIPT")
    print("BEST BUY STORE\n")

    print(f"{'Item':<10} {'Qty':<5} {'Unit Price':12} {'Total'}")

    for item in cart:
        quantity = cart[item]
        unit_price = products[item]
        item_total = quantity * unit_price

        # HELPS TO ALIGN THE TEXT ON THE RECEIPT 
        print(f"{item:<10} {quantity:<5} ${unit_price:<12} ${item_total}")



    print("\nSubtotal: $", total)
    
    print("Discount: $", discount)
    
    print("Tax: $", tax)

    print("Total: $", final_total)
    
    print("Paid: $", money)
    
    print("Change: $", change)

    print("\nThank you for shopping with us!")

    cart.clear()

# THIS SHOWS THE MENU
while True:
    print("\n1 Show Products")
    
    print("2 Add Item")
    
    print("3 Remove Item")
    
    print("4 View Cart")
    
    print("5 Checkout")
    
    print("6 Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_products()
        low_stock_alert()


    elif choice == "2":
        add_item()


    elif choice == "3":
        remove_item()


    elif choice == "4":
        view_cart()


    elif choice == "5":
        checkout()


    elif choice == "6":
        print("System closed")
        break


    else:
        print("Invalid choice")
