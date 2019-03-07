import requests

# Sending request with URL

URL = 'http://www.facebook.com'

response = requests.get(URL)

file = open('/home/kkroit/result.txt', "wb")

# In this following loop it will go to the response content and every time it is going to pick 10000 bytes and
# it will take it to data

for data in response.iter_content(10000):
    file.write(data)

file.close()