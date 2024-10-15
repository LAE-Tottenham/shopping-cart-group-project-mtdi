import pyfiglet

def getContactDetails():
    print(pyfiglet.figlet_format("CONTACT DETAILS", font = "straight" ))
    phone_no = int(input(pyfiglet.figlet_format("Enter phone number: ", font = "straight")))
    email = input(pyfiglet.figlet_format("Enter email address: ", font = "straight"))

    return []

print(pyfiglet.figlet_format("DELIVERY", font = "straight"))
delivery_method = input(pyfiglet.figlet_format("Home or click and collect? ", font = "straight"))
address = input(pyfiglet.figlet_format("Enter Address: ", font = "straight"))
country = input(pyfiglet.figlet_format("Enter Country: ", font = "straight"))
town_city = input(pyfiglet.figlet_format("Enter Town/City: ", font = "straight")) 
postcode = input(pyfiglet.figlet_format("Enter postcode: ", font = "straight"))

total = 0

if country != "UK" :
    deliv_price = 999.99
else:
    if delivery_method == "home" :
        deliv_price = 4.99
    else:
        deliv_price = 0

print(pyfiglet.figlet_format("Total cost is " + str(total) + str(deliv_price), font = "straight"))

print(pyfiglet.figlet_format("PAYMENT", font = "straight"))
currency = input(pyfiglet.figlet_format("What currency would you like to pay with? ", font = "straight"))
payment_method = input(pyfiglet.figlet_format("Would you like to pay with Visa or mastercard? ", font = "straight"))
card_no = int(input(pyfiglet.figlet_format("Card number: ", font = "straight")))
expiry_date = input(pyfiglet.figlet_format("Enter expiry date in the format MM/YY: ", font = "straight"))
name = input(pyfiglet.figlet_format("Enter name: ", font = "straight"))
cvv = int(input(pyfiglet.figlet_format("Enter cvv: ", font = "straight")))
