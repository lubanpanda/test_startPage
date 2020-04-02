from common.read_yaml import ReadYaml
from common.base import Base
import time
import os

#公告列表页
class NoticeListPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
        yaml = ReadYaml("./data/element_loc.yaml")
        self.company_notice_more_loc=yaml.analysis_data("index","company_notice_more_loc") # 公司公告【更多】
        self.operation_column_loc=yaml.analysis_data("notice_list","operation_column_loc")  # 操作列
        self.row_titles_loc=yaml.analysis_data("notice_list","row_titles_loc")  #所有文章标题
        self.top_btns_loc=yaml.analysis_data("notice_list","top_btns_loc") #所有置顶按钮
        self.toast_loc = yaml.analysis_data("edit_notice", "toast_loc")  # toast信息
        self. article_rows_loc=yaml.analysis_data("notice_list","article_rows_loc") #列表中的所有行
        self.top_icons_loc=yaml.analysis_data("notice_list","top_icons_loc") #【顶】标签
        self.time_columns_loc=yaml.analysis_data("notice_list","time_columns_loc")  #时间列（包含表头）
        self.refresh_btns_loc=yaml.analysis_data("notice_list","refresh_btns_loc")  #所有【刷新】按钮

    def enter_in_page(self):
        '''进入公司公告列表页'''
        self.click(self.company_notice_more_loc)

    def check_operation_column_exist(self):
        '''检查操作列是否存在'''
        return self.is_element_exist(self.operation_column_loc)

    def get_toast_text(self):
        '''获取toast提示文本内容'''
        time.sleep(0.3)
        print(self.get_text(self.toast_loc))
        return self.get_text(self.toast_loc)

    def top_or_cancel_top_notice(self,index):
        '''置顶/取消置顶置顶索引的文章并返回该文章的标题'''
        first_title=self.find_elements(self.row_titles_loc)[index].text
        self.find_elements(self.top_btns_loc)[index].click()
        return first_title

    def get_title_index(self,title):
        '''获取指定标题的索引'''
        titles=self.find_elements(self.row_titles_loc)
        for i,t in enumerate(titles):
            if t.text==title:
                return i
            elif i==len(titles):
                return None

    def get_title_by_index(self,index):
        '''根据指定索引获取公告标题'''
        return self.find_elements(self.row_titles_loc)[index].text

    def get_top_icon_title_attribute(self,index):
        '''获取指定置顶/取消置顶按钮的title属性'''
        return  self.find_elements(self.top_btns_loc)[index].get_attribute("title")

    def check_top_icon_exist(self,index):
        '''检查对应文章行中存在【顶】图标'''
        html=self.find_elements(self.article_rows_loc)[index].get_attribute("innerHTML")
        if 'class="top-text-icon">顶</div>' in html:
            return True
        else:
            return False

    def check_refresh_notice(self,index_before):
        '''检查刷新公告'''
        current_time=time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
        print (current_time)
        title = self.get_title_by_index(index_before)  # 获取指定索引公告的标题
        self.find_elements(self.refresh_btns_loc)[index_before].click()  # 点击【刷新】按钮
        toast_text= self.get_toast_text()   #获取toast
        time.sleep(3)
        index_after = self.get_title_index(title)#获取刷新后该公告当前的索引
        print(index_after)
        refresh_time = self.get_notice_time_by_index(index_after)#获取公告的刷新时间
        print(refresh_time)
        from dateutil.parser import parse
        time_difference=(parse(current_time) - parse(refresh_time)).total_seconds()
        return toast_text,time_difference,index_after#返回时间差

    def get_notice_time_by_index(self,index):
        '''获取指定某行的公告时间'''
        if index==-1:
            return self.find_elements(self.time_columns_loc)[index].text
        else:
            return self.find_elements(self.time_columns_loc)[index+1].text

    def get_top_notice_length(self):
        '''获取置顶公告的个数'''
        top_btns=self.find_elements(self.top_btns_loc)
        length=0
        print(len(top_btns))
        for top_btn in top_btns:
            if top_btn.get_attribute("title")=="取消置顶":#置顶公告的title为“取消置顶”
                length+=1
        print(length)
        return  length
























