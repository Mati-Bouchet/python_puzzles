# Create a function that returns any of the items you can afford in the store with the money you have in your wallet

items_purchase = {
    "water": 2,
    "bread": 4,
    "carrots": 10,
    "beer": 15,
    "phone": 150,
    "ps5": 600,
    "tv": 800
                }

money_in_wallet = int(input("How much money do you have? "))

def avail_for_purchase(ite, money):
    can_purchase = []
    for product, price in ite.items():
        if price <= money:
            can_purchase.append(product)
    return can_purchase

print("********************")


def purchase(ite, money):
    cart = []
    money_spent = 0
    
    while True:
            
        print("Items for purchase: ")
        for product, price in ite.items():       
            print(product, price)
            
        print(f"Your cart: {cart}")
            
        print(f"You have {money} dollars.")
        print("If you want to quit, please press Q. ")
        
        choice = input("Please write which item you want to purchase: ")
        
        item_price = ite[choice]
        if choice == "Q".lower():
            break
            
        elif item_price > money:
            print("You can't afford this product. ")

        elif choice in ite:
            cart.append(choice)
            money_spent += item_price
            money -= item_price
            
        else:
            print("This item is not in the list. ")
            
        print("********************")
        
    print(f"{choice} has been added to the cart")
    
    print(f"You have left {money} dollars")
        
    print(f"Your cart: {cart}")
        
    print(f"You have spent {money_spent} dollars.")
    
    print("If you want to quit, please press Q. ")
      
affordable_items = avail_for_purchase(items_purchase, money_in_wallet)
print(f"You can buy: {affordable_items}")

purchase(items_purchase, money_in_wallet)
