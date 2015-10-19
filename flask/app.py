#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, url_for, render_template, request, redirect, session, escape
import time

app=Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
# 现在通过app.config["VAR_NAME"]，我们可以访问到对应的变量
# allconfig = '\n'.join(['%s: %s' % (k, v) for k, v in app.config.items()])
# f = lambda a: '%s=%s' % (a[0], a[1])
# allconfig = '\n'.join(map(f, app.config.items()))
# print allconfig


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


@app.route('/user/<username>')
def profile(username):
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action='' method='post'>
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))    


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('uploads/uploaded_file.txt')
        return redirect(url_for('hello'))
    else:
        return render_template('upload_file.html')


#app.secret_key = '\x8d2\xe1\x93\xe9\xb9Lr\x99\x91\xc3\x07\xa3\x03j\x11\x8e%\xce\xe4\xf5\xf0\x85\x1a'


#@app.errorhandler(404)
#def not_found(error):
#    return render_template('error.html'), 404


@app.errorhandler(404)
def not_found(error):
    from flask import make_response
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-something'] = 'A value'
    return resp


from datetime import datetime
print '-----------------'
print 'App start at %s ' % datetime.now()


with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile', username='John Doe')
    print url_for('static', filename='style.css')


if __name__=='__main__':
    app.run(host='0.0.0.0')
