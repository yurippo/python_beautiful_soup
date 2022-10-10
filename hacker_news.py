import codecs
from bs4 import BeautifulSoup
import requests #to be able to download data from the URL

#requests allows us to get hold of the data from a particular URL
request = requests.get("https://news.ycombinator.com/")
#then we can save the data we got in response in a variable

#then we can print out the text of the response
yc_webpage = request.text #save the page returned in response in a variable
#equivalente to what we did in the other code when we opened our html file and we read the file contents of the file

#now I'm going to use Beautiful Soup to parse that webpage
soup = BeautifulSoup(yc_webpage,"html.parser") #and our Soup was created

print(soup.title.get_text())


#this code grabs all the article tags
articles = soup.find_all (class_="titleline") #(name ="a",class_="titleline")
#creating these 2 lists to save each of the articles and links in these 2 lists

article_texts = []
article_links = []

for article_tag in articles:
    # this code grabs the first article text
    article_text = article_tag.get_text()
    #this code adds the article text to the list
    article_texts.append(article_text)
    #this text gets the article link
    article_link = article_tag.get("href")
    #this code adds the article link to the list
    article_links.append(article_link)

#this code grabs the article upvote but for that I need to create a list using list comprehension here
# and a for loop to get each of the score it's the same as creating the loop above but much shorter

article_up_votes = [int(score.get_text().split()[0]) for score in soup.find_all("span", class_="score")]


#Now printing everything the article texts, the article links and the article votes
print(article_texts)
print(article_links)
print(article_up_votes)

#Challenge can I print out the title and link for the hacking news story with the highest number of upvotes.
#Hint use the index of the largest number inside the article_upvotes list as a guide)

max_value = max(article_up_votes)
print(max_value)

max_index = article_up_votes.index(max_value)
print(max_index)

#result_list = [article_texts[max_index],article_links[max_index],max_value]

#print(result_list)

#Another option to resolve this challenge

# largest_num = max(article_up_votes)
# print(largest_num)
# largest_index = article_up_votes.index(largest_num)
# print(article_texts[largest_index])
# print(article_links[largest_index])













#
# #this code grabs the first article tag
# article_tag = soup.find (name = "a",class_= "titlelink")
#
#
# #this code grabs the first article text
# article_text = soup.find (name = "a",class_= "titlelink")
#
#
# #this text gets the article link
# article_link = soup.find (name = "a",class_= "titlelink")
#
#
# #this code grabs the article upvote
#article_up_vote = soup.find ("span", class_="score").get_text() #we need to dig one step more with .get_text() to get the number of points
#
#
# #printing the first article tag
# print(article_tag)
# #printing the first article text
# print(article_text.get_text())
# #printing the article link
# print(article_link.get("href"))
# #printing the article upvote
#print(article_up_vote)





# all_anchor_tags = soup.find_all (name = "a",class_= "titlelink")
#


