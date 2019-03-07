import requests
import bs4

# Sending request with URL

URL = 'http://www.facebook.com'

response = requests.get(URL)


parsed_data = bs4.BeautifulSoup(response.text)

# fetch all links
all_links = parsed_data.select('a')
print(len(all_links))

# fetch text of all links
for l in all_links:
    # print(l.getText())
    # print(l.get('href'))
    # print(l.get('title'))
    print(l.attrs)



