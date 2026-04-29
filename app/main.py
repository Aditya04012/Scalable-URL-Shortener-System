from fastapi import FastAPI,Request,HTTPException
from Database import start_db
from core.redis import r
from rate_limiter import rate_limit
from Routes.Routes import router
app = FastAPI()




@app.on_event("startup")
async def redis_start():
    try:
        await r.ping()
        print("Redis Connected")
    except:
        print("Redis Down")



@app.on_event("startup")
async def init_database():
    await start_db()
    print("DB Connected!")

"""
@app.middleware('http')
async def rate_limit_middleware(request:Request,call_next):
    key=f"rate:{request.client.host}"

    allowed=await rate_limit(r,key,limit=100,window=60)

    if not allowed:
        raise HTTPException(status_code=429,detail="Too many Requests")
    
    response=await call_next(request)
    return response
"""

app.include_router(router,prefix="/api/v1")