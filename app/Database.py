from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from Model.shortner_model import Shortner

async def start_db():
    client=AsyncIOMotorClient("mongodb://localhost:27017", maxPoolSize=100,
    minPoolSize=10)
    db=client["urlShortner"]
    await init_beanie(database=db,document_models=[Shortner])

