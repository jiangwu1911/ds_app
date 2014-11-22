# -*- coding: UTF-8 -*-

from bottle import route, get, post, delete, request, response, hook, static_file

from actions import auth
import model
import utils
import settings as conf


def define_route(app):
    @app.route('/dsapp/:path#.+#')
    def server_static(path):
        return static_file(path, root=conf.static_files_path)

    #---------- auth related ----------
    @app.post('/login')
    def login(db):
        response.content_type = "application/json"
        return auth.login(request, db)

    @app.post('/logout')
    def logout(db):
        response.content_type = "application/json"
        return auth.logout(request, db)

    @app.get('/roles')
    def list_role(db):
        return auth.list_role(request, db)

