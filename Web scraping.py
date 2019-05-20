
    
import requests
from bs4 import BeautifulSoup

r = requests.get('https://qiita.com/') 
data = BeautifulSoup(r.text, 'html.parser')
data    

import requests
from bs4 import BeautifulSoup

r = requests.get('https://newspicks.com/') 
data = BeautifulSoup(r.text, 'html.parser')
elems = data.find_all("div", class_="title _ellipsis")
for e in elems:
 print(e.getText())