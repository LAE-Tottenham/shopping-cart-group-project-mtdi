import pyfiglet as pfg 
from currency_exchange_tool import *  
from shop_functions import start_shop
from account import *
from cart import *
login_or_create = input("would you like to login, say (yes) for login, or (no) for creating a acoount")
if login_or_create == "yes" or "y":
    login_account()
else:
    create_account()

print (pfg.figlet_format("shopping list",font="larry3d"))


print('Please select what you would like to buy')
items_to_buy = start_shop()

print ("enter contact details:")
getContactDetails()

print("enter the following infromation:")
address, canDeliver = get_address()

print ("your shipping cost is:")

postcode = address[2]
validateStatus(postcode)
shippingCost = shippingCost(postcode)

total = items_to_buy.get("total_cost") + shippingCost
print(total)

print("enter payment information:")
payment_method()

change_currency = input("would you like to switch currencies from GBP? yes or no")
if change_currency.lower() == "yes" or "y":
    currency = input("enter the new currency that you would like to change to ")
    if check_currency_exists(currency):
        print(f"your final total is: {currency_convert("GBP", currency, total)} {currency}")













