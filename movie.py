import requests
from bs4 import BeautifulSoup, NavigableString
import re

URL = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

movie_back = soup.select(
        'div[id=wrap] > div[id=container] > div[id=content] > div[class=article] > div[class=obj_section] > div[class=lst_wrap] > ul[class=lst_detail_t1] > li')

final_movie_data = []

for movie in movie_back:
    a_tag = movie.select_one('dl > dt > a')

    movie_title = a_tag.contents[0]
    movie_code = a_tag['href'].split('code=')[1]

    print("movie_title = ",movie_title)
    print("movie_code = ",movie_code,"\n")


    # movie_data = {
    #     'title' : movie_title,
    #     'code' : movie_code
    # }
    # final_movie_data.append(movie_data)
    # print(final_movie_data)