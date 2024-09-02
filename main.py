# -*- coding: utf-8 -*-
"""
@Time : 2024 9月 02 11:13
@Author : xushiyin
@Mobile : 18682193124
@desc : 工具集入口
"""

import typer
from rich import print, print_json  # noqa

app = typer.Typer()


@app.command()
def hello(name: str):
    data = {
        "name": "Rick",
        "age": 42,
        "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
        "active": True,
        "affiliation": None,
    }
    print(f'{name=}')
    print_json(data=data)


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == '__main__':
    app()
