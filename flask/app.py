#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask


app=Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
# 现在通过app.config["VAR_NAME"]，我们可以访问到对应的变量
# allconfig = '\n'.join(['%s: %s' % (k, v) for k, v in app.config.items()])
f = lambda a: '%s=%s' % (a[0], a[1])
allconfig = '\n'.join(map(f, app.config.items()))
print allconfig
