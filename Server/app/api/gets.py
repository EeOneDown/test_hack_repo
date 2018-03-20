# -*- coding: utf-8 -*-
from flask import jsonify, abort, request
from app import server
from app.api import api_route, users


@server.route(api_route('users'), methods=['GET'])
def get_users():
    # print(request.args.to_dict())
    return jsonify({'users': users})


@server.route(api_route('users/<int:user_id>'), methods=['GET'])
def get_user(user_id):
    user = list(filter(lambda u: u['id'] == user_id, users))
    if not user:
        abort(404)
    return jsonify({'user': user[0]})