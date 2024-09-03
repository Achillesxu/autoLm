# -*- coding: utf-8 -*-
"""
@Time : 2024 9月 03 22:13
@Author : xushiyin
@Mobile : 18682193124
@desc :
"""
from handlers.excel_handler import ExcelHandler

def read_excel2json(excel_path:str):
    eh = ExcelHandler(excel_path)
    eh.read_sheet_data()
