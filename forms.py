from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal

c_codes = CurrencyCodes()
c_rates = CurrencyRates(force_decimal=True)

def get_country_codes(rates_dict):
    """helper function to extract country codes from the rates dictionary as given from API"""
    country_codes = []
    for key in rates_dict:
        country_codes.append(key)
    return country_codes

def validate_currency(currency_to_convert):
    """validates for correct currency to convert from or to"""
    rates = c_rates.get_rates("USD")
    ##we do this because the API excludes the input currency in their list when returning the dict of currency codes
    country_codes = get_country_codes(rates)
    adj_country_codes = [*country_codes, "USD"]

    if currency_to_convert not in adj_country_codes:
        return False

    return True

def validate_amount_type(amount):
    """validation for correct currency amount"""
    try:
        float(amount)
    except ValueError:
        return False
    else: 
        return True

def calc_converted_currency(currency_from, currency_to, amount):
    """Converts given amount in from currency_from to currency_to and returns the result to display to user"""
    if validate_currency(currency_from) and validate_currency(currency_to) and validate_amount_type(amount):
        converted_result = round(c_rates.convert(currency_from, currency_to, Decimal(amount)),2)
        symbol = c_codes.get_symbol(currency_to)
        return f"The result is {symbol} {converted_result}"
    else: 
        return ""

