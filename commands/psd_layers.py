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
from handlers.utils import get_cur_user
from handlers.excel_handler import ExcelHandler
from collections import defaultdict

def check_psd_text_layers(file_path):
    def _print_layer_names(psd_obj):
        """递归输出 PSD 文件中所有图层的名称"""
        for layer in psd_obj:
            if layer.kind == 'type' and layer.is_visible:
                layer_names[layer.name] += 1
                # print(f"{layer.name}")
            if layer.is_group():
                _print_layer_names(layer)

    eh = ExcelHandler(str(file_path))
    psd_paths, fix_layers = eh.read_psd_path()

    for pf in psd_paths:
        if not Path(pf).exists():
            print(f'[red]{pf}[/red]')
            return

        layer_names = defaultdict(int)
        psd = PSDImage.open(pf)
        _print_layer_names(psd)

        fix_layer_names = {k:v for k, v in layer_names.items() if k in fix_layers}

        if len(fix_layer_names) != sum([v for v in fix_layer_names.values()]):
            print(f'[red]{pf} 需要修改的可见文本图层存在重复命名文本图层:[/red]')
            for k, v in fix_layer_names.items():
                if v > 1:
                    print(f'    [green]{k}[/green]-----[blue]{v}[/blue]')
