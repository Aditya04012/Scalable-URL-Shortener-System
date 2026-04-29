from beanie import Document
from pydantic import Field
from typing import Optional
from datetime import datetime,timedelta

class Shortner(Document):
    shortUrl:Optional[str]=None
    longUrl:str
    expire_at:datetime=Field(default_factory=lambda: datetime.utcnow()+timedelta(days=90))


    class Settings:
        name="shortner"
        indexes = ["shortUrl", "longUrl"]