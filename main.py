# -*- coding: utf-8 -*-
"""
@Time : 2024 9月 02 11:13
@Author : xushiyin
@Mobile : 18682193124
@desc : 工具集入口
"""

import typer
from rich import print, print_json  # noqa

from commands import psd_layers, excel_cmd

app = typer.Typer()


@app.command()
def layers(excel_name: str):
    psd_layers.check_psd_text_layers(excel_name)


@app.command()
def data(excel_name: str):
    excel_cmd.read_excel2json(excel_name)


if __name__ == '__main__':
    app()
