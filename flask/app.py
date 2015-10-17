#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
import time

app=Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
# 现在通过app.config["VAR_NAME"]，我们可以访问到对应的变量
# allconfig = '\n'.join(['%s: %s' % (k, v) for k, v in app.config.items()])
f = lambda a: '%s=%s' % (a[0], a[1])
allconfig = '\n'.join(map(f, app.config.items()))
print allconfig


@app.route('/')
def index():
    return 'Hello World!';


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'This is project page.'


@app.route('/about')
def about():
    return 'The about page'


if __name__=='__main__':
    app.run(host='0.0.0.0')

