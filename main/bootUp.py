import uvicorn
from os import getenv
from app.api.config import routes, startup
from starlette.applications import Starlette

app = Starlette(debug=True, routes=routes, on_startup=[startup])


if __name__ == '__main__':
    H = getenv('HOST','0.0.0.0')
    P = getenv('PORT',5000)
    uvicorn.run(app, host=H, port=int(P))