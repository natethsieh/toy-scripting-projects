# beautiful soup can be used to scrape websites; uses HTML to grab different data 
from bs4 import BeautifulSoup 

# allows us to download that html 
import requests 

res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text, 'html.parser')

print(soup.find_all('div'))

