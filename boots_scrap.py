import requests
from bs4 import BeautifulSoup
from lxml import etree

# # URL of the webpage you want to scrape
url = 'https://www.boots.com/health-pharmacy/medicines-treatments/sleep'  # Replace with your URL

# # Send a GET request to fetch the page content
response = requests.get(url)

# # Check if the request was successful
if response.status_code == 200:
#     # Parse the content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
# # Find all the h3 tags with product names
    product_names = soup.select('#hits div.oct-teaser__contents.oct-teaser__contents--only-foreground-image .oct-teaser__contents-panel--main-content a > div > h3')
    print('product_names',product_names)
# # Loop through the list and extract the text
    for product in product_names:
        print(product.get_text(strip=True))
