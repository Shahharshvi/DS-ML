#If u want ot scrape a website:
# 1.Use the APi
# 2.HTML Web scraping using some toll like bs4

import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"
#Step 1: Get the HTML

r=requests.get(url)
htmlContent=r.content
# print(htmlContent)

# Step2:Parse the HTML
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify())

# Step3:HTML Tree traversal

#Commonly used type of objects
# 1.Tag
# 2.NavigableString
# 3.BeautifulSoup
# 4.Comment
# title=soup.title
# print(title)
# print(type(title))
# print(type(soup))
# print(type(title.string))

#Get all paragraphs from page
# paras=soup.find_all('p')
# print(paras)

#Get all paragraphs from page
# anchor=soup.find_all('a')
# print(anchor)

#Get all links on page
# for link in anchor:
#     print(link.get('href'))

# all_links=set()
# for link in anchor:
#     if(link.get('href')!='#' and link.get('href')!='https://codewithharry.com' ) :
#         linkText=("https://codewithharry.com"+link.get('href'))
#         all_links.add(linkText)
#         print(linkText)


# links = soup.find_all('a')

# Iterate over the links and print their href values excluding those starting with 'https://codewithharry.com'
# for link in links:
#     href = link.get('href')
#     if href and not href.startswith('https://codewithharry.com'):
#         print(href)
#Get first element in HTML page
# print(soup.find('p'))

#get classes of any element in HTML page
# print(soup.find('p')['class'])


#get id of any element in HTML page--will give error
# print(soup.find('p')['id'])

#find all elements with class lead
# print(soup.find_all("p",class_="mt-2"))

#Get the text from tags/soup
# print(soup.find('p').get_text())

#To get text of html page
# print(soup.get_text())

#comment
# markup="<p><!-- this is a comment --></p>"
# soup2=BeautifulSoup(markup)
# print(soup2)
# print(type(soup2.p))
# print(type(soup2.p.string))


# .children- Tag's children are available as a list
# .contents-Tag's children are available as a generator

imgpreview2=soup.find(id='imgpreview2')
# print(imgpreview2)
# print(imgpreview2.children)

# print(imgpreview2.content)


# for elem in imgpreview2:
#     print(elem)

# for elem in imgpreview2.children:
#     print(elem)

# for elem in imgpreview2.contents:
#     print(elem)

# for item in imgpreview2.strings:
#     print(item)

#remove spaces
# for item in imgpreview2.stripped_strings:
#     print(item)

# print(imgpreview2.parent)

# for item in imgpreview2.parents:
#     # print(item)
#     print(item.name)

# print(imgpreview2.next_sibling)
# print(imgpreview2.next_sibling.next_sibling)
# print(imgpreview2.previous_sibling.previous_sibling)

elem = soup.select('footer')
print(elem)
elem = soup.select('#loginModal')
print(elem)