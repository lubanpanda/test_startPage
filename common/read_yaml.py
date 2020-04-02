import yaml

class ReadYaml():
    def __init__(self,file_path):
        self.file_path=file_path
        with open(self.file_path, 'r', encoding="utf-8") as file:
            self.data = yaml.load(file, Loader=yaml.Loader)

    def analysis_data(self,page_name,loc_name):
        '''解析data,获取元素定位'''
        return tuple(eval(self.data.get(page_name).get(loc_name)))
