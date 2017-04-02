import asyncio
import aioodbc
from settings import *
from aiohttp import web
from routes import *



async def startup(app: web.Application):
    dsn = 'Driver={SQLite3};Database=%s' % database_name
    app['db'] = await aioodbc.connect(dsn=dsn, loop=loop)


async def cleanup(app: web.Application):
    await app['db'].close()

def create_app(loop):
    app = web.Application()
    app.on_startup.append(startup)
    app.on_cleanup.append(cleanup)

    setup_routes(app)
    return app

loop = asyncio.get_event_loop()
app = create_app(loop)

web.run_app(app, host=host_name, port=port_name)