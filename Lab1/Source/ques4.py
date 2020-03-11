from bs4 import BeautifulSoup
import requests

# Enter URL from where you have to fetch the data
url = requests.get("https://catalog.umkc.edu/course-offerings/graduate/comp-sci/")
data = url.text
soup = BeautifulSoup(data, "html.parser")

# Using FindAll to find specific class

for p in soup.findAll('p',{'class':'courseblocktitle'}):
    for title, detail in zip(soup.findAll('span', {'class': 'title'}),
                             soup.findAll('p', {'class': 'courseblockdesc'})):

        # Print each course detail
        print ("Course Name: ", title.string)
        print("Detail: ", detail.string)
        print("---------------------------")

