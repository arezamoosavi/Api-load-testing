from os import getenv
from faust import App
import logging
from app.db.handler import pgQuery
from datetime import datetime

pg = pgQuery()

redis_server = getenv('REDIS_SERVER','redis://redis:6385/0')
kafka_broker = getenv('KAFKA_SERVER', 'kafka://kafka:9092')

faust_app = App(
    'main_app',
    version=1,
    autodiscover=True,
    origin='app',
    broker=kafka_broker,
    store=redis_server,
    key_serializer='json',
    value_serializer='json',
    )

@faust_app.task
async def on_started():
    print('Fasut Main APP STARTED . . .  \n\n')


logging.basicConfig(filename='faustLogs.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")


@faust_app.timer(interval=10)
async def fetch_Q_A():
    """
    every 3 sec return length of data that 
    has been stored in qa database
    """
    dict_Values = await pg.getAll(database='qa')
    setOfData = {datadct['question'] for datadct in dict_Values}
    print(f'Length of Unique Data at {datetime.now()} is: {len(setOfData)}')
