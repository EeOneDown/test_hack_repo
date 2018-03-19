# -*- coding: utf-8 -*-
from flask import render_template
from app import server


@server.route('/')
@server.route('/index')
def index():
    user = {'username': 'Ivan'}
    return render_template('index.html', title='Home', user=user)
