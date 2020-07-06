import requests, json
from bs4 import BeautifulSoup

res = requests.get('https://www.freecodecamp.org/news/')
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.find_all(class_='post')

allPosts = []
for post in posts:
    info = post.find(class_='post-card-content')
    title = info.h2.text
    title = title.lstrip()
    title = title.rstrip()
    author = post.find(class_='author-name-tooltip').text
    author = author.lstrip()
    author = author.rstrip()
    img = post.find(class_='post-card-image')['src']
    date = info.footer.time.text
    link = info.h2.a['href']
    link = 'https://www.freecodecamp.org{}'.format(link)
    allPosts.append(
        {'title': title,
         'author': author,
         'img': img,
         'date': date,
         'link': link
    })

with open('posts.json','w') as json_file:
    json.dump(allPosts, json_file, indent=3)