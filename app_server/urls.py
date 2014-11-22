# -*- coding: UTF-8 -*-

import model
import utils
import settings as conf


def define_route(app):
    @app.route('/dsapp/:path#.+#')
    def server_static(path):
        return static_file(path, root=conf.static_files_path)
