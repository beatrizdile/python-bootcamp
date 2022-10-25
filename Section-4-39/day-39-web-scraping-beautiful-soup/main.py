from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/")
yv_web_page = response.text

soup = BeautifulSoup(yv_web_page, "html.parser")

article_tag = soup.find(class_="titleline").get_text()
article_text = soup.find(class_="titleline").get("href")
article_link = soup.find(class_="score").get_text()


print(article_tag)
print(article_text)
print(article_link)



