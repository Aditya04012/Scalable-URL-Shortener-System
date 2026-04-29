async def rate_limit(redis,key:str,limit:int=100,window:int=60):
    current=await redis.incr(key)

    if(current==1):
        await redis.expire(key,window)
    
    if current>limit:
        return False
    
    return True