import datetime
import pymongo
from article import Article


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["leitmedien"]
articles = db.articles

def drop():
    articles.drop()

def insert(article: Article):
    articles.insert_one(article.__dict__)

def find():
    return articles.find()

