#importing the libraries for webscraping
import requests
from bs4 import BeautifulSoup

#getting the web content through url
html_doc = requests.get('https://en.wikipedia.org/wiki/Deep_learning')

#scrapping content using BeautifulSoup
soup = BeautifulSoup(html_doc.text, 'html.parser')
title = soup.title.string
links = []
#finding links in the page
for link in soup.find_all('a'):
    links.append(link.get('href'))

#saving the output to the text file webscraping
with open('webscraping.txt', 'w') as f:
    f.write("Title: " + title + "\n")
    f.write("Links: " + "\n")
    for link in links:
        f.write("Link: " + str(link) + "\n")