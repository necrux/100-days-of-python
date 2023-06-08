from bs4 import BeautifulSoup
import requests

#with open("website.html") as file:
#    contents = file.read()
#
#soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)
#print(soup.title.string)

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_text = []
article_link = []

article_line = soup.find_all(name="span", class_="titleline")
for tag in article_line:
    text = tag.find(name="a").getText()
    link = tag.find(name="a").get("href")
    article_text.append(text)
    article_link.append(link)

upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

highest_upvote = max(upvotes)
highest_upvote_index = upvotes.index(highest_upvote)

print(f"{article_text[highest_upvote_index]}: {article_link[highest_upvote_index]}")

