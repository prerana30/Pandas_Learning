import requests
import pandas as pd

def fetch_data_from_api():
    # Define the API endpoint and query parameters
    url = 'https://api.openaq.org/v2/measurements'
    params = {
        'location_id': '314323',
        'parameter': ['um025', 'pm25', 'pm1', 'pm10', 'um100', 'um010'],
        'date_from': '2023-02-27T05:45:00+05:45',
        'date_to': '2023-03-28T23:04:23+05:45',
        'limit': '1000'
    }

    # Send a GET request to the API
    response = requests.get(url, params=params)

    # Create a Pandas DataFrame from the JSON data in the API response
    if response.status_code == 200:
        data = response.json()['results']
        df = pd.DataFrame(data)
        return df
    else:
        print('Error: Unable to fetch data from API')

