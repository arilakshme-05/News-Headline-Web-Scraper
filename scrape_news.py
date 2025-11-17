import requests 
from bs4 import BeautifulSoup
def scrape_bbc_headlines():
    url="https://www.bbc.com/news"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    headlines=[]
    for h in soup.find_all("h2"):
        text=h.get_text(strip=True)
        if text and len(text)>20:
            headlines.append(text)
        with open("bbc_headlines.txt","w",encoding="utf-8") as file:
            for line in headlines:
                file.write(line+"\n")
        print("BBC Headlines saved to bbc_headlines.txt")
scrape_bbc_headlines()
