import requests
import pyfiglet

#outputs instructions 
def getContactDetails():
    print(pyfiglet.figlet_format("CONTACT DETAILS", font = "straight" ))
    phone_no = int(input(pyfiglet.figlet_format("Enter phone number: ", font = "straight")))
    email = input(pyfiglet.figlet_format("Enter email address: ", font = "straight"))

    return [phone_no,email]
#stores the address and important information
def getAddress():
    validCountries = ["UK","England","Scotland","Wales","Northern Ireland"]
    print(pyfiglet.figlet_format("DELIVERY", font = "straight"))
    print(f"We only deliver to {[validCountries]}")
    country = input(pyfiglet.figlet_format("Enter Country: ", font = "straight"))
    postcode = input(pyfiglet.figlet_format("Enter postcode: ", font = "straight"))

    if country not in validCountries:
        print("We do not deliver to that country")

    return postcode

def validateStatus(postcode):
    url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = requests.get(url)
    postcode = response.json()

    status = postcode.get("status")

    while status != 200:
        print("Invalid postcode")
        postcode = input("Enter a new postcode")
        url = f"https://api.postcodes.io/postcodes/{postcode}"
        response = requests.get(url)
        postcode = response.json()
        status = postcode.get("status")

#calculate shipping cost depending on distance
def shippingCost(postcode):
    delivery_method = input(pyfiglet.figlet_format("Standard (1) or Next Day (2)", font = "straight"))
    url = f"https://api.distancematrix.ai/maps/api/distancematrix/json?origins=N17%200BX&destinations={postcode}&key=OsI6PtznNFLu0fE0C14Uw5vgB0XF5s4hoTdlfzsGM5WKMx0lKfNkLLtMWMG9FZJb"
    response = requests.get(url)
    distance = response.json()

    if delivery_method == "1":
        delivery_price = distance.get("rows")[0].get("elements")[0].get("distance").get("value") / 1000
    elif delivery_method == "2":
        delivery_price = distance.get("rows")[0].get("elements")[0].get("distance").get("value") / 500

    return delivery_price

#print(pyfiglet.figlet_format("Total cost is " + str(total) + str(deliv_price), font = "straight"))

getPaymentInfo():
    print(pyfiglet.figlet_format("PAYMENT", font = "straight"))
    currency = input(pyfiglet.figlet_format("What currency would you like to pay with? (ISO 4217)", font = "straight"))
    payment_method = input(pyfiglet.figlet_format("Would you like to pay with Visa or mastercard? ", font = "straight"))
    card_no = int(input(pyfiglet.figlet_format("Card number: ", font = "straight")))
    expiry_date = input(pyfiglet.figlet_format("Enter expiry date in the format MM/YY: ", font = "straight"))
    name = input(pyfiglet.figlet_format("Enter name: ", font = "straight"))
    cvv = int(input(pyfiglet.figlet_format("Enter cvv: ", font = "straight")))
