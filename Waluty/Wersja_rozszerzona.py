import currencyapicom
import json
import re
import math
from fastapi import FastAPI

client = currencyapicom.Client("cur_live_Ht7cwEfYvrVC1bbDJTvjhWEkVqwHW5d71kN5BK5k")

app = FastAPI()

@app.get("/")
def home():
    return {"Data": "Test"}

@app.get("/convert/{input_currency}/{output_currencies}/{amount}/{date}")
def convert(input_currency: str = None, output_currencies: str = None, amount: str = None, date: str = None):

    input_currency = input_currency.upper()
    output_currencies = output_currencies.upper()
    output_currencies += ","

    input_currency_Regexp = re.compile(r'^[a-zA-Z]{3}$')
    output_currency_Regexp_check = re.compile(r'^([a-zA-Z]{3},){0,}+$')
    output_currency_Regexp_sort = re.compile(r'[a-zA-Z]{3}')
    date_Regexp = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')

    if output_currency_Regexp_check.match(output_currencies):
        output_currencies_tab = output_currency_Regexp_sort.findall(output_currencies)
        output_currencies_tab = sorted(output_currencies_tab)
    else:
        output_currencies_tab = []

    amount = float(amount)
    amount_check = None
    try:
        if amount == round(amount, 2) and amount >= 0:
            amount_check = True
        else:
            amount_check = False
    except:
        amount_check = False

    if ((bool(input_currency_Regexp.match(input_currency))) and (len(output_currencies_tab) > 0) and (amount_check == True) and (bool(date_Regexp.match(date)) == True)):
        try:
            currencies_tab = []

            result = client.historical(date)
            result = json.dumps(result)
            result = json.loads(result)

            for currency in output_currencies_tab:
                for_currency = result.get("data", []).get(currency, []).get("value", [])
                base_currency = result.get("data", []).get(input_currency, []).get("value", [])
                conversion = 0
                conversion = math.ceil(for_currency / base_currency * amount * 100) / 100
                conversion = f'{conversion:.2f}'

                temp_tab = []
                temp_tab.append(currency)
                temp_tab.append(conversion)

                currencies_tab.append(temp_tab)

            JSON_data = [{"currency": currency, "amount": amount} for currency, amount in currencies_tab]

            return JSON_data

        except Exception as e:
            return f"Your date or currency ID is incorrect (note: date must be after 1999-01-01) || {e}"

    else:

        output = ""

        if bool(input_currency_Regexp.match(input_currency)) != True:
            output += "Your inpur currency format is incorrect || "
        if len(output_currencies_tab) <= 0:
            output += "Your output currencies format is incorrect || "
        if amount_check != True:
            output += "Your amount format is incorrect || "
        if bool(date_Regexp.match(date)) != True:
            output += "Your date format is incorrect || "
        
        output = output[:-3]

        return output