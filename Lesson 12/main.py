import requests
import pandas as pd
import yaml

with open('credentials.yaml') as fh:
    dictionary_data = yaml.safe_load(fh)

token = dictionary_data.get('token')

start_dt = '2023-11-01'
end_dt = '2023-11-30'
URL = f'https://api.apilayer.com/fixer/timeseries?start_date={start_dt}&end_date={end_dt}&base=USD&symbols=RUB,EUR'
headers = {'apikey': token}
r = requests.get(url=URL, headers=headers)
result = []
header = ['Дата', 'Валюта', 'Курс к доллару']
print(r.json()['rates'])
for i in range(len(r.json()['rates'])):
    for j in range(len(list(list(r.json()['rates'].values())[i].values()))):
        temp = [list(r.json()['rates'].keys())[i], list(list(r.json()['rates'].values())[i].keys())[j],
                list(list(r.json()['rates'].values())[i].values())[j]]
        result.append(temp)

print(result)
my_df = pd.DataFrame(result)
my_df.to_csv('currencies.csv', header=header, index=False)