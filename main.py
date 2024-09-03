# -*- coding: utf-8 -*-
"""
@Time : 2024 9月 02 11:13
@Author : xushiyin
@Mobile : 18682193124
@desc : 工具集入口
"""

import typer
from rich import print, print_json  # noqa

from commands import ps_layers, excel_cmd

app = typer.Typer()


@app.command()
def ps_display_layers(file_path: str, only_text_layers: bool = True):
    ps_layers.psd_display_layers(file_path, only_text_layers)


@app.command()
def get_json(excel_path: str):
    excel_cmd.read_excel2json(excel_path)


if __name__ == '__main__':
    app()
