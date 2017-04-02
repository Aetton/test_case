from aiohttp import web
from sql.sql_reqs import *
import parse
from datetime import datetime


async def index(request):
    return web.Response(text='Hello Aiohttp!')

async def get_handler(request):
    user_id = parse.parse(r'/api/{}/',str(request.rel_url))[0]
    response = await get_user_data(request, user_id)
    if response:
        return web.json_response(data=response, status=200)
    return web.json_response(data={'Error': 'No data for id = %s' % user_id}, status=400)



async def post_handler(request):
    new_message, missing_fields = {}, []
    fields = ['name', 'phone', 'arpu', 'soc_tariff']
    new_message['id'] = parse.parse(r'/api/{}/',str(request.rel_url))[0]
    new_message['date'] = str(datetime.now())
    data = await request.json()
    for f in fields:
        new_message[f] = data.get(f)
        if not new_message[f]:
            missing_fields.append(f)
    if missing_fields:
        text = 'Invalid form submission, missing fields: {}'.format(', '.join(missing_fields))
        return web.json_response(data={'result':text}, status = 400)
    response = await add_user_data(request,new_message)
    if response == 'OK':
        return web.json_response(data={'result':'OK'}, status=200)
    return web.json_response(data={'Error': 'Unknown error'}, status=400)


