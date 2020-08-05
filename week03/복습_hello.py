# 변수, 자료형, 함수, 조건문, 반복문

#변수
# a = '2'
# b = 3
# first_name = 'sparta'
# print (a+first_name)

#자료형
# a_list = ['사과', '배', '감']
#
# a_list.append('키위')
# print(a_list)

# a_dict = {'name': 'aaa', 'age' : 20}
# a_dict['height'] = 100
# print(a_dict)

#함수
#
# def sum(a,b) :
#     return a+b
# result = sum(1,2)
#
# print(result)

#조건문
# def is_adult(age):
#     if age>20:
#         print('성인')
#     else:
#         print('청소년')
# is_adult(21)

#반복문
# fruits = ['사과', '배', '감', '귤']
# for fruit in fruits:
#     print(fruit)

# fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']
# # count = 0
# for fruit in fruits :
#     if fruit == '사과':
#         count += 1
# print(count)

# def count_fruit(name):
#     count = 0
#     for fruit in fruits:
#         if fruit == name:
#             count += 1
#     return count
# result = count_fruit('수박')
# print(result)

#
#
# import requests  # requests 라이브러리 설치 필요
#
# # requests 를 사용해 요청(Request)하기
# response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
#
# # 응답(response) 데이터인 json을 쉽게 접근할 수 있게 만들어 city_air 에 담고
# city_air = response_data.json()
#
# print(city_air)
#
# gus =city_air["RealtimeCityAir"]["row"]
# for gu in gus:
#     if gu["PM10"] < 10:
#         print(gu["MSRSTE_NM"],gu["PM10"])


#웹크롤링
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이ㅜㄹ한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')


# title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
#그린북만 가져오기
# print(title.text)
#속성만가져오기
# print(title['href'])

trs = soup.select('#old_content > table > tbody > tr')
for tr in trs:
    title = tr.select_one('td.title > div > a')
    if title is not None:
        rank = tr.select_one('td > img ')['alt']
        point = tr.select_one('td.point').text

        doc = {
            'title' :title.text,
            'rank' : rank,
            'point' : point
        }

        db.movies.insert_one(doc)

         # print(rank['alt'], title.text, point.text)
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1)
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img