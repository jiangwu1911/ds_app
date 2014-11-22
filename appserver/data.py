# -*- coding: UTF-8 -*-

from sqlalchemy.orm import sessionmaker
from model import User
from model import Role
from model import Permission
from model import UserRoleMembership
import utils


def insert_basic_data(engine):
    Session = sessionmaker(engine)
    session = Session()

    admin = User(name='admin', password=utils.md5encode('admin'))
    session.add(admin)

    admin_role = Role('管理员', '管理员')
    user_role = Role('普通用户', '普通用户')
    session.add(admin_role)
    session.add(user_role)
    session.flush()

    membership1 = UserRoleMembership(user_id=admin.id,
                                     role_id=admin_role.id)
    session.add(membership1)
    session.commit()
    session.close()


def insert_test_data(engine):
    Session = sessionmaker(engine)
    session = Session()

    user1 = User(name='熊大', password=utils.md5encode('abc123'))
    user2 = User(name='熊二', password=utils.md5encode('abc123'))
    session.add(user1)
    session.add(user2)
    session.flush()

    admin_role = session.query(Role).filter(Role.name=='管理员').first()
    user_role = session.query(Role).filter(Role.name=='普通用户').first()
    session.add(UserRoleMembership(user1.id, user_role.id))
    session.add(UserRoleMembership(user2.id, user_role.id))

    session.commit()
    session.close()
