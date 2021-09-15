import requests
import os
import bs4
import re

def imagereq(siteUrl):
    res = requests.get(siteUrl)
    if res.raise_for_status() != 200: # here the statuss code returns None, which is Https status code that would be either 200(successful) or 404(unsuccessful) refer link section in the code
        soup = bs4.BeautifulSoup(res.content,"html.parser")
        data = soup.find_all(string = re.compile(r'img'))
        return data[0]

def imagedownload(i_link):
    image_res = requests.get(i_link)
    path = os.getcwd()
    os.makedirs(path + '\\Img')
    filename = open(path+ "\\Img\\Img01.png","wb")
    filename.write(image_res.content)
    filename.close()


imagelink = imagereq("https://xkcd.com/")
imagedownload(imagelink)



# Link for raise_for_status() : https://requests.kennethreitz.org/en/master/api/#requests.Response.raise_for_status
