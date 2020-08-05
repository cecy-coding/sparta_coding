

#네이버 영화 제목 가져오기
import requests
from bs4 import BeautifulSoup # 받아온 값들을 html 로 가공

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#old_content > table > tbody > tr:nth-child(2)

print(soup.select('#old_content > table > tbody > tr'))
numbers = soup.select('#old_content > table > tbody > tr')
movies = soup.select('#old_content > table > tbody > tr') #무비스에 tr덩어리들이 들어있음
points = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    # a_tag = movie.select_one('td.ac > img'['alt'])
    b_tag = movie.select_one('td.title > div > a')
    # c_tag = movie.select_one('td.point').text

    if b_tag is not None :
        rank = movie.select_one('td.ac > img')['alt']
        title = print(b_tag.text)
        point = movie.select_one('td.point').text
# print(rank, title, point)
        print(movie.select_one('td.ac > img')['alt'],b_tag.text,movie.select_one('td.point').text)


#몽고디비 쓰는 법~~
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

print(list(db.users.find({})))
all_users = list(db.users.find({}))
print(all_users[0]['name'])

for i in all_users :
    print(i['name'],i['age'])

same_ages = list(db.users.find({'age': 40}))
for i in same_ages :
    print(i)
# Create(생성)
# user = {'name': '론', 'age': 40}
# db.users.insert_one(user)
#
# # Read(조회) - 한 개 값만
# user = db.users.find_one({'name': '론'})
#
# # Read(조회) - 여러 값 ( _id 값은 제외하고 출력)
# same_ages = list(db.users.find({'age': 40}, {'_id': False}))
#
# # Update(업데이트)
# db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 116}})
#
# # Delete(삭제)
# db.users.delete_one({'name': '론'})