# from pymongo import MongoClient
#
# client = MongoClient('localhost', 27017)
# db = client.dbsparta
#
# target_movies = db.movies.find_one({'title':'월-E'})
# print(target_movies['point'])

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movies.find_one({'title': '월-E'})
target_point = target_movie['point']