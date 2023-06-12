import requests
import hashlib
import time
import pandas as pd

token = '0e556d07bc8f4aa14ce99df24bacbf6f58201b13257e797d7f8497d42ecc0e79'

secret_token = '696a6f47212d93f88cef71238cfb3d1cd357905b3e34eabd2bbc49124553c129'

# Generate the Unix timestamp
timestamp = int(time.time())

# Construct the query string
query_string = f'time={timestamp}'

# Generate the hash
hash_string = secret_token + str(timestamp)
hash_value = hashlib.sha512(hash_string.encode()).hexdigest()

# Construct the URL with the query string and hash
url = f'https://api.fabdb.net/cards?{query_string}&hash={hash_value}'

parameters = {
    "page":1,
    "per_page":100

} 

total_pages = 21
# Set the request headers
headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/json'
}

data_records = []

for page in range(1, total_pages + 1):
    parameters['page'] = page

    response = requests.get(url, params=parameters)

    # Process the response or store the data as per your requirement
    data = response.json()

    # Extract the relevant data records from the response
    data_records.extend(data['data'])
  
# Create a DataFrame from the extracted data records
df = pd.DataFrame(data_records)

# Display the DataFrame
print(df)
