# coding=utf-8

import mechanize
import random

browser = mechanize.Browser()
browser.set_handle_robots(False)
headers = [
    ('Accept', 'text/javascript, text/html, application/xml, text/xml, */*'),
    ('Content-type', 'application/x-www-form-urlencoded'),
    ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36')]
browser.addheaders = headers

imageNumber = 1
dirname = "images"

def load() :
	word = gen()
	src = "https://www.google.com/search?q=%s&tbm=isch&&newwindow=1&source=lnms&tbm=isch&sa=X&ei=dh-8U7UB1uPwBff5gbAN&ved=0CAYQ_AUoAQ&biw=1440&bih=779"%(word)

	global dirname
	dirname = "images_%s"%(word)

	data = browser.open(src).read()
	save_img(data)


def gen() :
	words = []

	flag = True
	endFlag = 0
	while flag :
		char = chr(ord("a") + random.randrange(0, 25))
		words.append(char)
		endFlag += 10

		if random.randrange(0, 1000) < endFlag :
			flag = False
			break


	return "".join(words)

def save_img(data) :
	from bs4 import BeautifulSoup

	file = open("read.html", "w")
	file.write(repr(data))

	soup = BeautifulSoup(data)
	imgs = soup.findAll("img")

	if len(imgs) <= 0 :
		load()
		return

	import os
	if not os.path.exists(dirname) :
		os.makedirs(dirname)

	global imageNumber

	for img in imgs :
		imgsrc = img.get("src")
		if imgsrc :
			browser.retrieve(imgsrc, "%s/image_%s"%(dirname, imageNumber))
			imageNumber += 1


if __name__ == "__main__" :
	load()
