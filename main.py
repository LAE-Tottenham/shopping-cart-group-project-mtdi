from currency_exchange_tool import currency_convert
from shop_functions import start_shop
import pyfiglet

print(pyfiglet.figlet_format('Welcome to my shop', font = "term"))


print('Please select what you would like to buy')
items_to_buy = start_shop()