#id VARCHAR(20) PRIMARY KEY
#date DATETIME
#name VARCHAR(50)
#phone VARCHAR(10)
#arpu INT
#soc_tariff VARCHAR (10)
from settings import *
import asyncio


async def add_user_data(request, user):
    user_id = user['id']
    user_date = user['date']
    user_name = user['name']
    user_phone = user['phone']
    user_arpu = user['arpu']
    user_soc_tariff = user['soc_tariff']
    db = request.app['db']
    cur = await db.cursor()
    sql_req = "SELECT * FROM users where id = '{id}'".format(id = user_id)
    print(sql_req)
    await cur.execute(sql_req)
    r = await cur.fetchall()
    if len(r):
        sql_req = u"UPDATE users \
                           SET date = '{date}', name = '{name}',\
                           phone = '{phone}', arpu = '{arpu}', soc_tariff = '{soc_tariff}'\
                           WHERE id = '{id}'".format(id = user_id, date = user_date, name = user_name, phone = user_phone, arpu = user_arpu, soc_tariff = user_soc_tariff)
        print(sql_req)
        await cur.execute(sql_req)
        await db.commit()
    else:
        sql_req = u"INSERT INTO users (id, date, name, phone, arpu, soc_tariff)\
                                   VALUES ('{id}','{date}','{name}','{phone}',{arpu},'{soc_tariff}')".format(id=user_id, date=user_date, name=user_name, phone=user_phone,
                                                           arpu=user_arpu, soc_tariff=user_soc_tariff)
        await cur.execute(sql_req)
        await db.commit()
    await cur.close()
    request.app.loop.create_task(delete_user_data(request,user_id))
    return 'OK'

async def get_user_data(request, user_id):
    response_dict = {}
    db = request.app['db']
    cur = await db.cursor()
    await cur.execute("SELECT * FROM users where id = '{id}'".format(id=user_id))
    await db.commit()
    r = await cur.fetchone()
    await cur.close()
    if r:
        print(r)
        fields = ['id','date','name', 'phone', 'arpu', 'soc_tariff']
        for i in range(len(fields)):
            response_dict[fields[i]] = str(r[i])
        return response_dict
    else:
        r = None


async def delete_user_data(request, user_id):
    await asyncio.sleep(3600)
    db = request.app['db']
    cur = await db.cursor()
    await cur.execute("DELETE FROM users where id = '{id}'".format(id=user_id))
    await db.commit()
    await cur.close()
