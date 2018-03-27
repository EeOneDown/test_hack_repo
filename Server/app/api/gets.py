# -*- coding: utf-8 -*-
from flask import jsonify, abort, request
from app import server
from app.api.api_types import DbWorker
from app.api.api_helper import api_route


@server.route(api_route('users'), methods=['GET'])
def get_users():
    # print(request.args.to_dict())
    worker = DbWorker()
    users = worker.get_all_users()
    return jsonify({'users': users})


@server.route(api_route('users/<int:user_id>'), methods=['GET'])
def get_user(user_id):
    worker = DbWorker()
    user = worker.get_user(user_id)
    if not user:
        abort(404)
    return jsonify({'user': user})
