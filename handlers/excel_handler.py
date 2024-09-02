# -*- coding: utf-8 -*-
"""
@Time : 2024 9月 02 13:49
@Author : xushiyin
@Mobile : 18682193124
@desc :
"""
import io
from rich import print # noqa
from rich.traceback import Traceback # noqa
from openpyxl import load_workbook
from collections import defaultdict
FontRedColor = 'FFEA3324'


class ExcelHandler:
    def __init__(self, f_path: str | io.BytesIO, sheet_name: str|None = None):
        self.f_path = f_path
        self.sheet_name = sheet_name
        self.wb = None
        self.ws = None

    def load_excel(self):
        self.wb = load_workbook(self.f_path, data_only=True, read_only=True)

    def get_all_sheet_names(self):
        return self.wb.sheetnames

    @staticmethod
    def find_valid_key_value(in_dict, in_key):
        """only ascii letter"""
        if in_key in in_dict:
            return in_dict[in_key]
        else:
            ss = in_key
            while True:
                ss = chr(ord(ss) - 1)
                if ss in in_dict:
                    return in_dict[ss]

    def read_sheet_data(self):
        print(f'读取excel: [red]{self.f_path}[/red]')
        self.load_excel()

        if self.sheet_name is None:
            s_names = self.get_all_sheet_names()
            self.sheet_name = s_names[0]
            print(f'默认读取 sheet: [red]{self.sheet_name}[/red]')
        else:
            print(f'读取 sheet: [red]{self.sheet_name}[/red]')

        cur_sheet = self.wb[self.sheet_name]
        find_header = False
        row_header = list()
        row_datas = list()

        try:
            for row in cur_sheet.iter_rows(min_row=1, max_row=200, min_col=1, max_col=20):
                if find_header:
                    row_cols = list()
                    row_cols.append({
                        'value': row[0].value,
                        'column': row[0].column_letter,
                    })
                    for co in row[1:]:
                        if co.value and co.font.color.value == FontRedColor:
                            row_cols.append({
                                'value': co.value,
                                'column': co.column_letter,
                            })
                        else:
                            continue
                    row_datas.append(row_cols)
                else:
                    if row[0].value == '商品ID':
                        find_header = True
                        for co_h in row:
                            if co_h.value:
                                row_header.append({
                                    'value': co_h.value,
                                    'column': co_h.column_letter,
                                })
                    else:
                        continue
        except Exception:
            print(Traceback())
        # print(f'{row_header=}')
        header_dict = {i['column']:i['value'] for i in row_header}
        # print(f'{header_dict=}')
        # print(row_datas)
        target_data = list()
        for row in row_datas:
            tmp = defaultdict(list)
            for col in row:
                t_key = self.find_valid_key_value(header_dict, col['column'])
                tmp[t_key].append(col['value'])
            target_data.append(tmp)

        # print(target_data)
        return target_data


if __name__ == '__main__':
    eh = ExcelHandler('C:\\Users\\Achil\\Desktop\\健康节听诊器（调整）.xlsx')
    data = eh.read_sheet_data()
    print(data)