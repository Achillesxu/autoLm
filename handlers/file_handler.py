# -*- coding: utf-8 -*-
"""
@Time : 2024 9月 02 16:54
@Author : xushiyin
@Mobile : 18682193124
@desc :
"""
from pathlib import Path


def find_file(search_path:str, filename:str) -> Path | None:
    """search_path 是根目录的话，检索会很慢"""
    path = Path(search_path)
    for file in path.rglob(filename):
        return file
    return None
