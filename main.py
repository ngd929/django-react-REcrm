import os
import requests

from requests.exceptions import HTTPError
from dotenv import load_dotenv, dotenv_values

# config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
# print(config["RAPID_API"])
load_dotenv()
print(os.environ["RAPID_API"])


# #call the API endpoint - Use try/except to catch errors
# try:
#     response = requests.request("GET", url, headers=hdrs, params=qrystr)
#     response.raise_for_status()
#     #access json content
#     response_data = response.json()

# except HTTPError as http_err:
#     print(f'HTTP error occurred: {http_err}')
# except Exception as err:
#     print(f'Other error occurred: {err}')


url = "https://realtor.p.rapidapi.com/properties/v2/list-for-sale"

querystring = {"city":"Friendswood","limit":"20","state_code":"TX","offset":"0","sort":"relevance"}

headers = {
    'x-rapidapi-key': config["RAPID_API"],
    'x-rapidapi-host': "realtor.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)