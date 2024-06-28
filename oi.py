# %%
import requests
from bs4 import BeautifulSoup

url = 'https://www.residentevildatabase.com/personagens/ada-wong/'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'pt-BR,pt;q=0.6',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'priority': 'u=0, i',
    'referer': 'https://www.residentevildatabase.com/personagens/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

resp = requests.get(url, headers=headers)
# %%
resp.status_code
# %%
soup = BeautifulSoup(resp.text)

# %%
div_page = soup.find("div", class_="td-page-content")

# %%
paragrafo = div_page.find_all("p")[1]

# %%

ems = paragrafo.find_all("em")

# %%

data={}
for i in ems:
    chave, valor = i.text.split(":")
    chave = chave.strip(" ")
    data[chave] = valor.strip(" ")
    
data    
    
