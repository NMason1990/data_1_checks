
# importing packages and requests from api
import pandas as pd
from pandas import json_normalize
import requests

url = "https://omgvamp-hearthstone-v1.p.rapidapi.com/cards/types/Minion"

headers = {
	"X-RapidAPI-Key": "dfafdd2951msh214c441e47ba622p120bf6jsn0127ae649412",
	"X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())

df = pd.DataFrame(response)

df[df['Rarity'] == 'Legendary']
