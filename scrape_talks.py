from lxml import html
import requests
from map_words import get_themes

def get_info(url, session):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	title = tree.xpath("//h1[@class='title']//text()")
	author = tree.xpath("//a[@class='article-author__name']//text()")
	position = tree.xpath("//p[@class='article-author__title']//text()")

	title = title[0].strip()
	author = author[0].replace('Â\xa0', ' ')
	author = author.replace('By ', '').strip()
	position = position[0].strip()

	text_ = tree.xpath("//div[@class='body-block']/p//text()")
	text = ""
	for paragraph in text_:
		try:
			int(paragraph)
		except ValueError:
			paragraph = paragraph.replace('â\x80\x99', "'")
			paragraph = paragraph.replace('Â\xa0', ' ')
			paragraph = paragraph.replace('â\x80\x9c', '"')
			paragraph = paragraph.replace('â\x80\x9d', '"')
			paragraph = paragraph.replace('â\x80\x94', '-')
			paragraph = paragraph.replace('â\x80¦', '...')
			text += paragraph.strip()
	return title, author, position, text

urls = []
urls.append('https://www.lds.org/general-conference/2016/10/i-will-bring-the-light-of-the-gospel-into-my-home?lang=eng')
urls.append('https://www.lds.org/general-conference/2016/10/the-master-healer?lang=eng')
urls.append('https://www.lds.org/general-conference/2016/10/rise-up-in-strength-sisters-in-zion?lang=eng')

session = "General Women's Session"

for url in urls:
	title, author, position, text = get_info(url, session)
	num_themes = 5
	themes = get_themes(text, num_themes)
	print('TITLE: ', title)
	print('AUTHOR: ', author)
	print('POSITION: ', position)
	print('SESSION: ', session)
	print('THEMES: ', themes)
