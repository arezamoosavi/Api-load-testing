from os import getenv
import faust
import logging
import asyncio
from app.tools.faust_ import faust_app as app

logging.basicConfig(filename='faustLogs.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

async def main():
    
    await app.start()
    logging.info('Faust Works')
    await app.stop()
    exit(1)



if __name__ == '__main__':

    try:
        asyncio.get_event_loop().run_until_complete(main())
        
    except Exception as e:

        logging.error('Error! {}'.format(e))
        exit(0)

