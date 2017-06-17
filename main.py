import requests
from bs4 import BeautifulSoup

html = ""
with open("/Users/user/Desktop/pagina-completa.htm", 'r')as input:
    html = input.read()


soup = BeautifulSoup(html, 'lxml')

listaUl = soup.findChildren("ul", {"class" : "customer-details"})

itens = soup.findChildren("ul" ,{"class", "customer-details"})


newSoup = BeautifulSoup(str(itens[0]), 'lxml')


