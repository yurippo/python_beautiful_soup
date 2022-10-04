import bs4
import requests


HOST = "https://donnees.montreal.ca"
PATH = "/search"
QUERY_STRING = "?q=tags:Eau&from=0"

EAU_URL = HOST + PATH + QUERY_STRING

response = requests.get(EAU_URL)

soup = bs4.BeautifulSoup(response.text)

# print(soup)

#soup = print(response.text)

#soup = bs4.BeautifulSoup(response.text)

# selectionner tous le titres de jeux de données
# tous les éléments <a> qui sont enfants d'éléments <h3> avec la classe "text-lg"
#result = soup.select("h3.text-lg a")

# selectionner tous le titres de jeux de données
# tous les éléments <a> qui sont enfants d'éléments <h3> avec la classe "text-lg"
result = soup.select("div h3.text-lg.font-bold a")

# tapper votre solution ici
# indice: soup.???
result_one = soup.select("#main-container\ z-10 div.container.mx-auto.md\:flex.p-gutter main ul div div div.flex.flex-col.w-4\/5 h3 a")


print(result_one)
