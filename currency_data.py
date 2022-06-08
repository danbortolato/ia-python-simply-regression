import json

import requests

from key.api_key import s_k

s_date = '2020-02-11'
e_date = '2020-03-11'
link = "https://api.apilayer.com/currency_data/timeframe?start_date=2020-03-11&end_date=2020-04-11"

headers = s_k

response = requests.get(url=link, headers=headers, data=payload)
# list = json.loads(response.content.decode('utf-8'))
result = response.text
print(result)
