from fastapi import APIRouter,Request,status
from fastapi import HTTPException
from core.redis import r
from Model.shortner_model import Shortner
from fastapi.responses import RedirectResponse
from pydantic import BaseModel,EmailStr
import string
from datetime import datetime
from core.retry_safeRedis import safe_redis_get

BASE62 = string.ascii_letters + string.digits


def encode_base62(num):
    base = len(BASE62)
    s = []
    while num > 0:
        s.append(BASE62[num % base])
        num //= base
    return ''.join(reversed(s)) or "0"  



router=APIRouter()

class LongUrlSchema(BaseModel):
    longUrl:str

@router.post("/url")
async def create_shortUrl(request:LongUrlSchema):

    #check if this the longurl present in db

    exist=await Shortner.find_one(Shortner.longUrl == request.longUrl)
    if exist:
        return {
            "shortUrl":f"http://localhost:8001/api/v1/url/{exist.shortUrl}"
        }
    
    counter = await r.incr("shortner_cnt")
    shortUrl=encode_base62(counter)

    data=Shortner(
        shortUrl=shortUrl,
        longUrl=request.longUrl
    )

    await data.insert()

    await r.set(shortUrl,data.longUrl,ex=90*24*60*60)

    return {"shortUrl":f"http://localhost:8001/api/v1/url/{shortUrl}"}





@router.get("/url/{shortUrl}")
async def getLongUrl(shortUrl:str):

    cache=await safe_redis_get(shortUrl)
    
    if cache:
        return RedirectResponse(url=cache,status_code=302)
    
    data=await Shortner.find_one(Shortner.shortUrl==shortUrl)

    if not data:
        raise HTTPException(status_code=404,detail="URL not found")
    
    if data.expire_at < datetime.utcnow():
         raise HTTPException(status_code=410, detail="URL expired")
       
    r.set(shortUrl,data.longUrl,ex=90*24*60*60)

    return RedirectResponse(url=data.longUrl, status_code=302)