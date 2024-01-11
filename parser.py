import lxml
import requests
from bs4 import BeautifulSoup as BS


def get_data(url):
	"""
		Getting headers and urls of articles
	"""

	data = {}

	# request to site with news
	resp = requests.get(url)

	# making soup object
	soup = BS(resp.text, "lxml")

	# getting list of all news article
	articles = soup.find_all("div", class_="ArticleItem")
	articles = articles[0:10]

	# getting urls and headers from artcile
	for article in articles:
		url = article.find("a", class_="ArticleItem--name")["href"]
		header = article.find("a", class_="ArticleItem--name").text.strip()

		# write data to dictionary
		data[header] = url

	return data


def main():
	url = "https://kaktus.media/?lable=8&date=2024-01-10&order=time"

	data = get_data(url)

	print(*data.items(), sep="\n")


if __name__ == "__main__":
	main()
