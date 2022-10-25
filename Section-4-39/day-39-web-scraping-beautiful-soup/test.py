from bs4 import BeautifulSoup
import lxml


with open("website.html", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.prettify())

print(soup.p)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get_text())

company_url = soup.select_one(selector="p a")
print(company_url)

# SELECT-ONE: THE FIRST MATCH ONLY
name = soup.select_one(selector="#name")
print(name)

# SELECT: ALL MATCHES IN A LIST
headings = soup.select(selector=".heading")
print(headings)
