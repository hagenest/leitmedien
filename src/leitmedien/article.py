from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Article:
    title: str
    authors: list
    keywords: list
    content: str
    url: str
    date: datetime
    isPremium: bool

