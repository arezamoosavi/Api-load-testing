from os import getenv
from tortoise import Tortoise
from app.db.models import qa

class TorPostgre:

    def __init__(self):
        self.db_url = getenv('POSTGRES_URL')
    
    async def initdb(self):
        await Tortoise.init(db_url=self.db_url, modules={"models": ["app.db.models"]})
        await Tortoise.generate_schemas()

    async def checkall(self):
        await self.initdb()
        print("all q and a: ")
        print(await qa.all())