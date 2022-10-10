import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
#I use requests to get the URL and dump into the response variable

#then we can print out the text of the response
greatest_movies_webpage = response.text #save the page returned in response in a variable
#equivalente to what we did in the other code when we opened our html file and we read the file contents of the file

#now I'm going to use Beautiful Soup to parse that webpage
soup = BeautifulSoup(greatest_movies_webpage,"html.parser") #and our Soup was created

#print(soup.prettify())
#prettifly returns the entire website, webpage, html file in a beutiful format

#print(soup.title.get_text())
#to print our beautiful soup

#this code grabs all the movie tags

movies = soup.find_all (name="h3",class_="title")

movie_texts = []

for movie_tag in movies:
    # this code grabs the first article text
    movie_text = movie_tag.get_text()
    #this code adds the article text to the list
    movie_texts.append(movie_text)
    #this text gets the article link

#another way to do it is

#for n in range(len(movie_texts)-1,-1,-1):
    #print(movie_texts[n])

movies_final = movie_texts[::-1] #one way to do it

#now it's the part of the code we'll write on the file

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies_final:
        file.write(f"{movie}\n")

print(movies_final)