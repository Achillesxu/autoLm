# -*- coding: utf-8 -*-
"""
@Time : 2024 9月 04 09:27
@Author : xushiyin
@Mobile : 18682193124
@desc :
"""
import getpass


def get_cur_user():
    return getpass.getuser()


def get_cur_user_desktop_path():
    return f'C:/Users/{get_cur_user()}/Desktop'
