import requests
import json
from config import keys

class Convertion:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество валюты {amount}')

        if quote not in keys:
            raise ConvertionException('Валюта неопознана')

        if base not in keys:
            raise ConvertionException('Валюта неопознана')
        r = requests.get(
            f'https://v6.exchangerate-api.com/v6/c902610ee55f3326943e3b02/pair/{keys[quote]}/{keys[base]}/{amount}')
        result = json.loads(r.content)['conversion_result']
        return result

class ConvertionException(Exception):
    pass