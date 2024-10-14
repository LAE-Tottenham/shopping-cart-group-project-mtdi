import math # you'll probably need this

exchange_rates = {
    'USD': 1.13, 
    'EUR': 1.15,
    'VND': 32442.36,
    'ZAR': 22.87,
    'CAD': 1.80
}
def check_currency_exists(currency):
    return 

def currency_convert(original_c, new_c, amount):
    if check_currency_exists(new_c):
          amount *= exchange_rates[new_c]
          return amount 
    else:
         return ("currency not avaliable in store")


