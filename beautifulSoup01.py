from bs4 import BeautifulSoup
import requests

url = "https://pf.kakao.com/_eAGqxb"

r = requests.get(url)


soup = BeautifulSoup(r.text, "html.parser")

# elements = soup.find_all(class_="wrap_home")

# print(elements)
print(r.text)

item = soup.select(".view_profile")

print("item : ", item)