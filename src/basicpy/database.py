from pymongo import MongoClient
from datetime import datetime
from structure import Article

client = client = MongoClient('mongodb://localhost:27017/')
db = client["leitmedien"]
articles = db["articles"]

example = Article(
    title="Is Water really a liquid?",
    newspaper="TIEZ",
    url="https://www.tiez.de/water-liquid/",
    summary="lorem ipsum aqua",
    published=datetime.now(),
    content="lorem ipsum aqua dolor sit amet",
    authors=["John Doe"],
    keywords=["water", "liquid"],
    isPaywall=False,
    scraped=datetime.now(),
    keywords=["Test"],
    sentiment={"neg": 0.23, "neu": 0.56, "pos": 0.10, "compound": 0.85}
)

def insert_article(article):
    articles.insert_one(article.__dict__)

def get_articles():
    return articles.find()

def drop_articles():
    articles.drop()

def test():
    drop_articles()
    insert_article(example)
    print(get_articles())

