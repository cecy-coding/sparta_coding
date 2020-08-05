from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
db.users.insert_one({'name': '덤블도어', 'age': 116})