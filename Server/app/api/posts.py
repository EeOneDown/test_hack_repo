# -*- coding: utf-8 -*-
from flask import jsonify, abort, request
from app import server
from app.api import api_route, users


@server.route(api_route('users'), methods=['POST'])
def create_user():
    # print(request.json)
    if not request.json or 'username' not in request.json:
        abort(400)
    user = {
        'id': users[-1]['id'] + 1,
        'username': request.json['username'],
        'temperature': request.json.get('temperature', 0)
    }
    users.append(user)
    return jsonify({'user': user}), 201
