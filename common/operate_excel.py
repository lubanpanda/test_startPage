#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import xlrd

class OperateExcel():
    def __init__(self,file_path):
        self.file_path=file_path
        self.excel=self.get_excel()

    def get_excel(self):
        tables=xlrd.open_workbook(self.file_path)
        return tables

    def get_sheet(self,i):
        '''
        通过index获取sheet内容
        '''
        sheet_data=self.excel.sheets()[i]
        return sheet_data

    def get_lines(self):
        '''
        获取行数
        '''
        lines=self.get_sheet().nrows
        return lines

    def get_cell(self,row,cell):
        '''
        获取单元格内容
        '''
        data=self.get_sheet().cell(row,cell).value
        return data
if __name__ == '__main__':
    book=OperateExcel()