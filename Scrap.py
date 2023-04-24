import requests
from bs4 import BeautifulSoup
import csv

urlhome = "https://www.bbc.com/"



res = requests.get(urlhome)
html_c = res.content

s= BeautifulSoup(html_c, "html.parser")

a_tags_title = s.find_all('a', class_='block-link__overlay-link')
# a_tags_autohors = s.find_all('a',class_='text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8')
# span_tags_dates = s.find_all('span',class_='text-gray-63 dark:text-gray-94')
a_tags_urls = s.find_all('a',class_='block-link__overlay-link')
titles = []
# dates = []
urls = []
y = 0
for a_tag_title in a_tags_title:
    y = y+1
    if(y > 10):
        break
    else:
        title = a_tag_title.text
        titles.append(title)
# for a_tag_author in a_tags_autohors:
#     author = a_tag_author.text
#     authors.append(author)

# for span_tag_date in span_tags_dates:
#     date = span_tag_date.text
#     dates.append(date)
y = 0
for a_tag_url in a_tags_urls:
    y = y+1
    if(y > 10):
        break
    else:
        x = a_tag_url['href']
        str = "https://www.bbc.com/"
        if str in x:
            url = x
        else:
            url = urlhome + a_tag_url['href']
        urls.append(url)



filename = "articles_details.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title','url'])
    for i in range(len(titles)):
        t = titles[i].strip()
        writer.writerow([t,urls[i]])

