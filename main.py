from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

#req = Request('https://jolybell.com', headers={'User-Agent': 'Mozilla/5.0'})
#webpage = urlopen(req).read()

#soup = BeautifulSoup(webpage, 'lxml')
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'lxml')


tag = soup.b
tag.name = 'block'
tag['id'] = 'verybold'

print(tag.get('id'))

css_soup = BeautifulSoup('<p class="body"></p>', 'lxml')
print(css_soup.p['class'])