from os import getenv
import asyncpg
from datetime import datetime


class pgQuery:
    def __init__(self):
        self.db_url = getenv('POSTGRES_URL')
    
    async def saveData(self, database, question, answer):  #database='qa'

        conn = await asyncpg.connect(self.db_url)
        query = '''INSERT INTO {}(question, answer, created_at) 
                            VALUES($1, $2, $3)'''.format(database)
        await conn.execute(query, question, answer, datetime.now().isoformat())
        await conn.close()
        return 'SAVED to ASyncPg!'

    
    async def getAll(self, database): #database='qa'
        
        conn = await asyncpg.connect(self.db_url)
        rows = await conn.fetch('SELECT * FROM {}'.format(database))
        await conn.close()
        return [dict(row) for row in rows]
        # return rows
        