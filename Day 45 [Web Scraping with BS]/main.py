from bs4 import BeautifulSoup
import lxml
import requests

url = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=url).text

soup = BeautifulSoup(response, "lxml")
title_tag = soup.select("div h3")
print(title_tag)

# with open("website.html", encoding="utf-8") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "lxml")
# print(soup.find_all(name="a"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
