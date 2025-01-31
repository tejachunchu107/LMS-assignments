#Day 18
import requests
from bs4 import BeautifulSoup

def fetch_title(url):
    
    response = requests.get(url)
    
   
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        
        title = soup.title.string
        return title
    else:
        return "Failed to retrieve the webpage"


url = 'https://example.com'
title = fetch_title(url)
print(title)
