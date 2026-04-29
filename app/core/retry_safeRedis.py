import asyncio
from core.circuit_breaker import circuit
from core.redis import r as redis

async def safe_redis_get(key):
    if not circuit.can_call():
        return None  # fallback

    for attempt in range(3):  # retry
        try:
            value = await redis.get(key)
            circuit.record_success()
            return value
        except Exception:
            await asyncio.sleep(0.1 * (2 ** attempt))  # exponential backoff

    circuit.record_failure()
    return None