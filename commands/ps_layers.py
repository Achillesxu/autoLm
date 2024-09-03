# -*- coding: utf-8 -*-
"""
@Time : 2024 9月 03 14:43
@Author : xushiyin
@Mobile : 18682193124
@desc :
"""
from pathlib import Path

from psd_tools import PSDImage
from rich import print  # noqa


def _print_layer_names(psd, prefix="", only_text_layers=True):
    """递归输出 PSD 文件中所有图层的名称"""
    for layer in psd:
        if layer.kind == 'type':
            print(f"{prefix}{layer.name}--{'text'}--文字: [red]{layer.text}[/red]")
        else:
            if not only_text_layers:
                print(f"{prefix}{layer.name}--{layer.kind}")
        if layer.is_group():
            _print_layer_names(layer, prefix + "    " if not only_text_layers else "", only_text_layers)


def psd_display_layers(file_path, only_text_layers=True):
    fp = Path(file_path)
    if not fp.exists():
        raise Exception(f'{file_path}不存在')
    psd = PSDImage.open(file_path)
    _print_layer_names(psd, only_text_layers=only_text_layers)
