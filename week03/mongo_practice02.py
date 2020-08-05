from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

#1
# db.movies.find_one({'title' : '월-E',})
# print(['star']))

#2
target_star = db.movies.find_one({'title' : '월-E',})
# target_list = db.movies.find({'star' : target_star})
# target_list_mongo = list(target_list)
# for i in target_list_mongo :
#     print(i['title'])

#3여러정보 업데이트 (평점 0만들기)
db.movies.update_many({'star' : target_star}, {'$set', {'star' : 0}})




# movies = list(db.users.find({'star': target_star}))
# for movie in movies :
#     print(movie['title'])
