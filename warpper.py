import json
import requests
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall
import queue
file=open('text.txt','w')

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

url = 'http://movie.mtime.com/111754/characters.html'
response = requests.get(url=url, headers=headers)
contents=response.content
soup=BeautifulSoup(contents,"html.parser")
href_q=queue.Queue()
for tag in soup.find_all('td'):
    href_q.put(tag.find('a').get('href'))
    print(tag.find('a').get('href'))
while(not href_q.empty()):
    response=requests.get(href_q.get())
    contents = response.content
    soup = BeautifulSoup(contents, "html.parser")
    for tag in soup.find_all('dd',class_="cha_box"):
        m_name=tag.find('h3').text
        m_text=tag.find('div',class_="cha_mid").text
        file.write(m_name+"是"+m_text+'\n')
        print(m_text)

