import requests

API = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(API)
data = response.json()

# Создаем отображение для соответствия полных названий валют и их кодов
currency_codes_mapping = {v['Name']: k for k, v in data['Valute'].items()}

def convert_currency(from_currency, to_currency, amount):
    # Преобразуем переданные названия валют в соответствующие коды
    from_currency_code = currency_codes_mapping.get(from_currency, from_currency)
    to_currency_code = currency_codes_mapping.get(to_currency, to_currency)

    # Если передано полное название "Российский рубль", используем код "RUB"
    if from_currency == 'Российский рубль':
        from_currency_code = 'RUB'
    if to_currency == 'Российский рубль':
        to_currency_code = 'RUB'

    if from_currency_code == 'RUB':
        from_rate = 1
    else:
        from_rate = data['Valute'][from_currency_code]['Value']

    if to_currency_code == 'RUB':
        to_rate = 1
    else:
        to_rate = data['Valute'][to_currency_code]['Value']

    converted_amount = round((amount * from_rate) / to_rate, 2)
    return converted_amount
