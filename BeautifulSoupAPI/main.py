import collections

from bs4 import BeautifulSoup

# with open("./website.html", "r") as f:
#     contents = f.read()
#
# # import lxml
# # bs = BeautifulSoup(contents, "lxml")
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())
#
# all_anchors = soup.find_all(name="a")
# print(all_anchors)
#
# if len(all_anchors) > 0:
#     print(all_anchors[0].getText())
#     print(all_anchors[0].get("href"))
#
# headings = soup.find(name="h1", id="name")
# print(headings)
#
# section_headings = soup.find(name="h3", class_="heading")
# print(section_headings)


import requests

# get whole data from the URL by requests package
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
# print(soup.prettify())

articles = [article.getText()
            for article in soup.find_all(name="span", class_="titleline")]

links = [article.find(name="a").get("href")
         for article in soup.find_all(name="span", class_="titleline")
         if article.find(name="a")]

up_votes = []
for sub_text in soup.find_all(name="td", class_="subtext"):
    if sub_text.find(name="span", class_="score"):
        up_votes.append(int(sub_text.find(name="span", class_="score").getText().split()[0]))
    else:
        up_votes.append(0)

# if len(articles) == len(links) == len(up_votes):
#     for i in range(len(articles)):
#         print(f"{articles[i]}, available at {links[i]}, {up_votes[i]} Points")

largest_vote = max(up_votes)
largest_index = up_votes.index(largest_vote)

print(f"Maximum Votes for: {articles[largest_index]}, "
      f"available at {links[largest_index]}, "
      f"{up_votes[largest_index]} Points")
