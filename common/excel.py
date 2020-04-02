import xlrd


class ReadExcel():
    def __init__(self,file_path,sheet_name):
        self.file_path=file_path
        self.sheet_name=sheet_name

    def read_excel(self):
        workbook=xlrd.open_workbook(self.file_path)#打开excel表，填写路径
        table=workbook.sheet_by_name(self.sheet_name)#找到对应的sheet页
        row_num=table.nrows#获取总行数
        if row_num<=1:
            print("没数据")
        else:
            d={}
            for i in range(1,row_num):
                d[table.cell_value(i,1)+"_"+table.cell_value(i,1)]=table.cell_value(i,2)
            return d
if __name__ == '__main__':
    r=ReadExcel("../data/elementData.xlsx","elementsInfo")
    d=r.read_excel()
    for i in d.items():
        print(i)







