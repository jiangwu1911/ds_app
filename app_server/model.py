from sqlalchemy import Column, Integer, Sequence, String, Text, DateTime, Unicode
from sqlalchemy.ext.declarative import declarative_base
import utils
import datetime

Base = declarative_base()

class JsonObj():
    def to_dict(self):
        obj_dict = self.__dict__
        d = {}
        for key, val in obj_dict.items():
             if not key.startswith("_"):
                if isinstance(val, datetime.datetime):
                    d[key] = val.isoformat()
                else:
                    d[key] = val
        return d


class User(Base, JsonObj):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('seq_pk'), primary_key=True)
    name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(100))
    enabled = Column(Integer, default=1, nullable=False)
    deleted = Column(Integer, default=0, nullable=False)

    def __init__(self, name='', password='', email='', enabled=1, deleted=0):
        self.name = name
        self.password = password
        self.email = email
        self.enabled = enabled
        self.deleted = deleted

    def __repr__(self):
        return ("<User(%d, '%s', '%s', '%s', %d, %d, %d)>"
                % (self.id,
                   self.name,
                   self.password,
                   self.email,
                   self.enabled,
                   self.deleted))


class Role(Base, JsonObj):
    __tablename__ = 'role'
    id = Column(Integer, Sequence('seq_pk'), primary_key=True)
    name = Column(String(50), nullable=False)
    desc = Column(String(200))

    def __init__(self, name='', desc=''):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return("<Role(%d, '%s', '%s')>"
               % (self.id,
                  self.name,
                  self.desc))


class UserRoleMembership(Base, JsonObj):
    __tablename__ = 'user_role_membership'
    id = Column(Integer, Sequence('seq_pk'), primary_key=True)
    user_id = Column(Integer)
    role_id = Column(Integer)

    def __init__(self, user_id=0, role_id=0):
        self.user_id = user_id
        self.role_id = role_id

    def __repr__(self):
        return("<UserRoleMembership(%d, %d, %d)>"
               % (self.id,
                  self.user_id,
                  self.role_id))


class Permission(Base, JsonObj):
    __tablename__ = 'permission'
    id = Column(Integer, Sequence('seq_pk'), primary_key=True)
    role_id = Column(Integer)
    path = Column(String(500), nullable=False)
    method = Column(String(20), nullable=False)
    is_permit = Column(Integer, default=1, nullable=False)

    def __init__(self, path='', role_id=0, method='', is_permit=1):
        self.role_id = role_id
        self.path = path
        self.method = method
        self.is_permit = is_permit

    def __repr__(self):
        return("<Permission(%d, %d, '%s', '%s', %d)>"
               % (self.id,
                  self.role_id,
                  self.path,
                  self.method,
                  self.is_permit))


class Token(Base, JsonObj):
    __tablename__ = 'token'
    id = Column(String(100), primary_key=True)
    expires = Column(DateTime)
    user_id = Column(Integer)

    def __init__(self, expires=-1, user_id=0):
        self.id = utils.get_uuid()
        self.expires = expires
        self.user_id = user_id

    def __repr__(self):
        return("<Token('%s', '%s', %d)>"
               % (self.id,
                  self.expires,
                  self.user_id))
