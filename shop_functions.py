# all items avaliable and corosponding price 
items = {
    'Jacket': 119.99,
    'Gloves': 29.99,
    'Shirt': 54.99,
    'Shoes': 99.99,
    'Glasses': 59.99,
    'Hoodie': 74.99,
    'Joggers': 64.99,
    'Hat': 19.99,
    'Watch': 149.99,
    'Bracelet': 89.99
}
#listing items avalible and price 
def start_shop():
    print("Jacket=£119.99\nGloves=£29.99\nShirt=£54.99\nShoes=£99.99\nGlasses= £59.99\nHoodie= £74.99\nJoggers= £64.99\nHat= £19.99\nWatch=£149.99\nBracelet=£89.99")
    total = 0
    itemList = []
#asking user to inputs items they want
    while True:
        choice=input("enter the items that you would like to purchase:")
        if choice in items:
            total += items[choice]
            itemList.append(choice)
        elif choice == "":
            print(f"Your total is £{round(total,2)}")
            break
        else:
            print("Item not available")

    return {
        'items': itemList,
        'total_cost': round(total,2)
    }
        
        
