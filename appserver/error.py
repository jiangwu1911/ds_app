# -*- coding: UTF-8 -*-

from bottle import HTTPError

# ----- Basic -----
class EmptyVariableError(HTTPError):
    def __init__(self, varname):
        msg = "'%s'字段不能为空。" % varname
        super(EmptyVariableError, self).__init__(400, msg)


class DatabaseError(HTTPError):
    def __init__(self, msg):
        msg = "数据库错误: %s。" % msg
        super(DatabaseError, self).__init__(500, msg)


class UploadFolderNotSetError(HTTPError):
    def __init__(self, msg):
        msg = "服务器没有设置上传目录"
        super(UploadFolderNotSetError, self).__init__(500, msg)


# ----- Auth related -----
class UserNotFoundOrPasswordError(HTTPError):
    def __init__(self, username):
        msg = "用户名不存在，或密码错误。"
        super(UserNotFoundOrPasswordError, self).__init__(403, msg)


class TokenNotFoundError(HTTPError):
    def __init__(self, token_id):
        msg = "Token不存在。"
        super(TokenNotFoundError, self).__init__(401, msg)


class TokenNotProvidedError(HTTPError):
    def __init__(self):
        msg = "请求中没有包含Token。"
        super(TokenNotProvidedError, self).__init__(401, msg)


class TokenExpiredError(HTTPError):
    def __init__(self, token_id):
        msg = "Token已过期。"
        super(TokenExpiredError, self).__init__(401, msg)


class PermissionDenyError(HTTPError):
    def __init__(self):
        msg = "没有访问权限。"
        super(PermissionDenyError, self).__init__(403, msg)


class RoleNotFoundError(HTTPError):
    def __init__(self):
        msg = "权限定义不存在。"
        super(RoleNotFoundError, self).__init__(404, msg)

