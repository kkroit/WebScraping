import requests

# Sending request with URL

URL = 'http://www.facebook.com'

response = requests.get(URL)
print(response.text)
print(response.status_code)