from dataclasses import dataclass
from datetime import datetime


@dataclass
class Article:
    title: str
    newspaper: str
    url: str
    summary: str
    published: datetime
    content: str
    authors: list
    keywords: list
    isPaywall: bool = False
    scraped: datetime = datetime.now
    sentiment: dict = {"neg": 0, "neu": 0, "pos": 0, "compound": 0}