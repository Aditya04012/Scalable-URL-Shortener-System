import redis.asyncio as redis

r = redis.Redis(
    host='',
    port=6379,
    password='',
    max_connections=100,
    decode_responses=True
)

def get_redis():
    return r