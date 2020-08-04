import requests
from bs4 import BeautifulSoup, NavigableString
import re

URL = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

movie_back = soup.select(
        'div[id=wrap] > div[id=container] > div[id=content] > div[class=article] > div[class=obj_section] > div[class=lst_wrap] > ul[class=lst_detail_t1] > li')


for movie in movie_back:
    a_tag = movie.select_one('dl > dt > a')
    movie_title = a_tag.getText()
    movie_link_first = "https://movie.naver.com/"
    movie_link_back = a_tag['href']
    movie_link = movie_link_first + movie_link_back
    print(movie_title)
    print(movie_link,"\n")