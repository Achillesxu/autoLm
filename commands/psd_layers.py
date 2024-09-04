# -*- coding: utf-8 -*-
"""
@Time : 2024 9月 03 14:43
@Author : xushiyin
@Mobile : 18682193124
@desc :
"""
from collections import defaultdict
from pathlib import Path

from psd_tools import PSDImage
from rich import print  # noqa

from handlers.excel_handler import ExcelHandler


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
        lost_layers = list()
        psd = PSDImage.open(pf)
        _print_layer_names(psd)

        lost_layers = [i for i in fix_layers if i not in layer_names]
        fix_layer_names = {k: v for k, v in layer_names.items() if k in fix_layers}

        if len(fix_layer_names) != sum([v for v in fix_layer_names.values()]):
            print(f'[red]{pf}[/red]')
            if lost_layers:
                print(f'[red]psd文件缺少图层[/red]:')
                for l in lost_layers:
                    print(f'    [green]{l}[/green]')
            print(f'[red]psd文件重复图层[/red]: ')
            for k, v in fix_layer_names.items():
                if v > 1:
                    print(f'    [green]{k}[/green]-----[blue]{v}[/blue]')
