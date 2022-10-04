import codecs

from bs4 import BeautifulSoup
#import lxml

# with open("website.html") as file:
#        contents = file.read()
#
contents = codecs.open("website.html", "r", "utf-8") #this code opens de html file and dumps the html file into a variable
#print(contents.read())

soup = BeautifulSoup(contents,"html.parser")
#this line of code does the parsing creates our soup

#print(soup.title)
#print(soup.title.string)
#print(soup.prettify()) #returns the entire html file indented ppretty cool

#print(soup.a) # we are drilling down the html file grabbing either the html tag this will bring the first anchor a tag found in the website
#print(soup.li) #we can swap that with the first li for example
#print(soup.p) #we can swap that with the first paragraph for example
#we're essentialy drilling down the html file fiding the tags we're interested in and then getting hold of either the name of the tag or the actual tags of the html file

#BUT WHAT IF WE WANTED ALL OF THE PARAGRAPHS OR ALL OF THE ANCHOR TAGS IN OUR HTML FILE, WEBSITE?

#HOW DO WE DO THAT?!

all_anchor_tags = soup.find_all(name = "a") #find_all will bring all the tag names equal to a (to grab all the tags from the html file
#and we can basicaly change it to any of the tag names available on the website

#print(all_anchor_tags)

#But if we wanted only the text from the tag we would need a for to get it

#for tag in all_anchor_tags:
#    print(tag.getText()) #this is if I wanted the text
#     print(tag.get("href")) #this will bring me all of the URLS, the links from the html file

#heading = soup.find(name="h1",id="name")
#print(heading)

section_heading = soup.find(name="h3",class_="heading")
#print(section_heading.get_text()) #that will print the name of that tag
print(section_heading.get("class"))

class_is_heading = soup.find_all(class_="heading")
print(class_is_heading)

h3_heading = soup.find_all("h3",class_="heading")

print(h3_heading)

company_url = soup.select_one(selector="p a")#this string is the css selector
# #select_one will give us the first matching item and select will give us all the matching items in a list

print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)

#we can use everything we know about css selectors to select particular items out of an html file
#and this will be very useful because the elements will be nexted into divs and the div has an id all I have to do
#is to narrow down the div and narrow down on the element I want

#We've used Beautiful Soup to select Html elements on a HTML file :)


