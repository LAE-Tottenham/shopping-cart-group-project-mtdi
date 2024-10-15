import math

exchange_rates = {
    'USD': 1.13, 
    'EUR': 1.15,
    'VND': 32442.36,
    'ZAR': 22.87,
    'CAD': 1.80
}

def check_currency_exists(currency):
    if currency in exchange_rates:
        return True
    else:
        return False

def currency_convert(original_c, new_c, amount):
    if check_currency_exists(new_c) and original_c == "GBP":
        amount *= exchange_rates[new_c]
        return amount 
    elif not check_currency_exists(new_c):
        return ("Currency not avaliable in store")
    elif original_c != "GBP":
        return ("Cannot convert from that currency")
