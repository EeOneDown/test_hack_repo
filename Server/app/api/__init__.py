# -*- coding: utf-8 -*-
def api_route(method):
    return '/api/v1.0/{0}'.format(method)


users = [
    {
        'username': 'Ivan',
        'id': 1,
        'temperature': 36.6
    },
    {
        'username': 'Alex',
        'id': 2,
        'temperature': 36.7
    },
    {
        'username': 'Dan',
        'id': 3,
        'temperature': 36.8
    },
    {
        'username': 'Vas',
        'id': 4,
        'temperature': 36.5
    }
]


from app.api import gets
from app.api import errors
from app.api import posts
