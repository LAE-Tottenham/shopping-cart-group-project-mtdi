

import pyfiglet
#outputs instructions 
def getContactDetails():
    print(pyfiglet.figlet_format("CONTACT DETAILS", font = "straight" ))
    phone_no = int(input(pyfiglet.figlet_format("Enter phone number: ", font = "straight")))
    email = input(pyfiglet.figlet_format("Enter email address: ", font = "straight"))

    return [phone_no,email]

#stores the address and important information
def get_address():
    print(pyfiglet.figlet_format("DELIVERY", font = "straight"))
    delivery_method = input(pyfiglet.figlet_format("Home or click and collect? ", font = "straight"))
    country = input(pyfiglet.figlet_format("Enter Country: ", font = "straight"))
    town_city = input(pyfiglet.figlet_format("Enter Town/City: ", font = "straight")) 
    postcode = input(pyfiglet.figlet_format("Enter postcode: ", font = "straight"))
    house_number = input(pyfiglet.figlet_format("Enter house number: ", font = "straight"))
    address = [country,town_city,postcode,house_number]

    return delivery_method, address

total = 0
#calculate shipping cost depending on country you live in 
def shipping_cost (address, delivery_method):
    if address[0] != "UK" :
        deliv_price = 999.99
    else:
        if delivery_method == "home" :
            deliv_price = 4.99
        else:
            deliv_price = 0
    #output delivery price 
    print(pyfiglet.figlet_format("Total cost is "  + str(deliv_price), font = "straight"))

    print(pyfiglet.figlet_format("PAYMENT", font = "straight"))
def payment_method ():
    payment_method = input(pyfiglet.figlet_format("Would you like to pay with Visa or mastercard? ", font = "straight"))
    card_no = int(input(pyfiglet.figlet_format("Card number: ", font = "straight")))
    expiry_date = input(pyfiglet.figlet_format("Enter expiry date in the format MM/YY: ", font = "straight"))
    name = input(pyfiglet.figlet_format("Enter name: ", font = "straight"))
    cvv = int(input(pyfiglet.figlet_format("Enter cvv: ", font = "straight")))
    
