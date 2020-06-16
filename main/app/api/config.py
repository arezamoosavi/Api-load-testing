from starlette.responses import PlainTextResponse, JSONResponse, Response
from starlette.routing import Route
from pydantic import BaseModel
import asyncio
import json
from app.db.handler import pgQuery

pg = pgQuery()

class number_serializer(BaseModel):
    number: float

async def homepage(request):

    dict_Values = await pg.getAll(database='qa')
    # print(dict_Values)
    return Response(json.dumps(dict_Values), status_code=200, media_type="application/json")

async def health_check(request):
    return PlainTextResponse('up', status_code=200)


async def getSquare(request):
    n = request.path_params['number']
    n_ser = number_serializer(**{"number": n})
    
    saved = await pg.saveData(database='qa', question=n_ser.number, answer=n_ser.number**2)
    print(saved)
    return JSONResponse({'result': n_ser.number**2}, status_code=200)



async def startup():
    print('Ready to go fast!')


routes = [
    Route('/', homepage),
    Route('/health_check', health_check, name="health_check"),
    Route("/square/{number}", getSquare),

]