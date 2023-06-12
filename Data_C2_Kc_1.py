import requests
import hashlib
import time
import pandas as pd

token = '0e556d07bc8f4aa14ce99df24bacbf6f58201b13257e797d7f8497d42ecc0e79'

secret_token = '696a6f47212d93f88cef71238cfb3d1cd357905b3e34eabd2bbc49124553c129'

timestamp = int(time.time())

query_string = f'time={timestamp}'

hash_string = secret_token + str(timestamp)
hash_value = hashlib.sha512(hash_string.encode()).hexdigest()

url = f'https://api.fabdb.net/cards?{query_string}&hash={hash_value}'

headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)

# Check the response status code
print(f'Response status code: {response.status_code}')

# Check the response content
print(f'Response content: {response.content}')

if response.status_code == 200:
    # Request was successful
    data = response.json()
    print(f'Response data: {data}')
    if isinstance(data, list):
        # Convert non-dictionary items to dictionaries
        data = [item if isinstance(item, dict) else {'data': item} for item in data]
        df = pd.DataFrame(data)
        print(df)
else:
    # Request failed
    print(f'Request failed with status code: {response.status_code}')
