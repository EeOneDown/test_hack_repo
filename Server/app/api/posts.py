# -*- coding: utf-8 -*-
from flask import jsonify, abort, request
from app import server
from app.api.api_helper import api_route
from app.api.api_types import DbWorker


@server.route(api_route('users'), methods=['POST'])
def create_user():
    # print(request.json)
    if not request.json or 'name' not in request.json:
        abort(400)
    worker = DbWorker()
    new_user = worker.add_new_user(request.json['name'],
                                   request.json.get('description', None))
    return jsonify({'user': new_user}), 201
