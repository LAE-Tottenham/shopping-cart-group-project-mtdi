import pyfiglet as pfg 
from currency_exchange_tool import currency_convert  
from shop_functions import start_shop

print (pfg.figlet_format("shopping list",font="larry3d"))


print('Please select what you would like to buy')
items_to_buy = start_shop()



