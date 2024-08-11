import requests
from bs4 import BeautifulSoup
import csv

# URL of the Wikipedia article to scrape
url = 'https://en.wikipedia.org/wiki/Article_(grammar)#Types_of_article'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the content of the article (this will vary based on the website's structure)
    content = soup.find('div', {'class': 'mw-parser-output'})
    
    # Open a CSV file to write the data
    with open('wikipedia_article.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Paragraph']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header row
        writer.writeheader()
        
        # Write the data rows
        for paragraph in content.find_all('p'):
            text = paragraph.get_text(strip=True)
            writer.writerow({'Paragraph': text})
    
    print("Data has been written to wikipedia_article.csv")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
