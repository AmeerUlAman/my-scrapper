from bs4 import BeautifulSoup
import requests

url = 'https://www.robustors.com/'

# Fetch the page content
page = requests.get(url)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# Find all div elements
divs = soup.find_all('div', class_='page_frex__m400r')

print(divs)

# Pretty print each div element
# for div in divs:
#     print(div.prettify())
 
