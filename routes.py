from views import *

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_route('GET','/api/{user_id:\w+}/', get_handler)
    app.router.add_route('POST','/api/{user_id:\w+}/', post_handler)