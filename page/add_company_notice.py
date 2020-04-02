#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from common.read_yaml import ReadYaml
from common.base import Base
import time
import os

#新增公司公告页
class AddCompanyNotice(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
        yaml = ReadYaml("./data/element_loc.yaml")
        self.company_notice_more_loc = yaml.analysis_data("index", "company_notice_more_loc")  # 公司公告【更多】
        self.add_article_loc = yaml.analysis_data("notice_list","add_article_loc") # 【新增文章】按钮
        self.go_back_btn_loc= yaml.analysis_data("notice_list","go_back_btn_loc") # 【<】按钮
        self.scroll_bar_loc=yaml.analysis_data("notice_list","scroll_bar_loc") #滚动条
        self.add_type_loc = yaml.analysis_data("edit_notice","add_type_loc") # 【新增类型】按钮
        self.selected_type_loc = yaml.analysis_data("edit_notice","selected_type_loc")  # 选中类型
        self.drop_down_button_loc = yaml.analysis_data("edit_notice","drop_down_button_loc") # 类型下拉按钮
        self.types_loc = yaml.analysis_data("edit_notice","types_loc") # 所有类型
        self.title_input_loc = yaml.analysis_data("edit_notice","title_input_loc") # 标题输入框
        self.release_button_loc = yaml.analysis_data("edit_notice","release_button_loc") # 发布按钮
        self. release_confirm_loc=yaml.analysis_data("edit_notice","release_confirm_loc")  #发布提示页面-【确定】按钮
        self.toast_loc =yaml.analysis_data("edit_notice","toast_loc")   # toast信息
        self.add_attachment_loc = yaml.analysis_data("edit_notice","add_attachment_loc") # 【添加附件】按钮
        self.attachment_tip_loc = yaml.analysis_data("edit_notice","attachment_tip_loc")  # 附件大小提示文本
        self.attachment_title_loc = yaml.analysis_data("edit_notice","attachment_title_loc")  # 附件标题
        self.delete_attachment_loc =yaml.analysis_data("edit_notice","delete_attachment_loc")   # 删除附件按钮
        self.iframe_loc=yaml.analysis_data("edit_notice","iframe_loc")#iframe
        self.body_loc=yaml.analysis_data("edit_notice","body_loc")  #正文
        self.body_paragraph_loc=yaml.analysis_data("edit_notice","body_paragraph_loc")  #正文段落
        self.checkboxes_loc=yaml.analysis_data("edit_notice","checkboxes_loc")   #两个复选框，标题标红和发布到滚动栏
        self.row_titles_loc=yaml.analysis_data("notice_list","row_titles_loc")  # 所有文章标题
        self.return_btn_loc=yaml.analysis_data("edit_notice","return_btn_loc") #【返回】按钮
        self.not_saving_prompt_loc=yaml.analysis_data("edit_notice","not_saving_prompt_loc") # 编辑内容未保存提示文本
        self.close_button_loc= yaml.analysis_data("edit_notice","close_button_loc") # 提示页面-【关闭】按钮

    def enter_in_page(self):
        '''进入公司公告列表页'''
        self.click(self.company_notice_more_loc)

    def check_add_article_button(self):
        '''检查【新增文章】按钮是否存在'''
        return self.is_element_exist(self.add_article_loc)

    def click_add_article_button(self):
        '''点击【新增文章】按钮'''
        self.click(self.add_article_loc)
        # self.find_element(add_article_loc).send_keys(Keys.ENTER)

    def get_selected_type(self):
        '''检查选中的类型'''
        self.find_element(self.drop_down_button_loc).click()
        selected_type=self.get_text(self.selected_type_loc)
        self.find_element(self.drop_down_button_loc).click()
        return selected_type

    def get_all_types(self):
        '''获取所有类型'''
        types_text=[]
        self.find_element(self.drop_down_button_loc).click()
        types=self.find_elements(self.types_loc)
        for t in types:
            types_text.append(t.text)
        self.find_element(self.drop_down_button_loc).click()
        return types_text

    def check_title_default_text(self):
        '''检查标题默认文本
        由于标题输入框是根据文本属性定位的，所以直接检查该元素是否存在'''
        return self.is_element_exist(self.title_input_loc)

    def input_title(self,text=''):
        '''输入标题'''
        self.send_keys(self.title_input_loc,text)

    def get_title_text(self):
        '''获取标题输入框中的内容'''
        return self.get_text(self.title_input_loc)

    def click_realease(self):
        '''点击【发布】'''
        self.click(self.release_button_loc)

    def click_and_confirm_release(self):
        self.click_realease()
        '''点击【确定】发布'''
        self.click(self.release_confirm_loc)

    def get_toast_text(self):
        '''获取toast提示文本内容'''
        time.sleep(0.3)
        print(self.get_text(self.toast_loc))
        return self.get_text(self.toast_loc)

    def get_attachment_tip_text(self):
        '''获取附件提示文本'''
        return self.get_text(self.attachment_tip_loc)

    def add_attachment(self,file_path):
        '''添加附件'''
        self.click(self.add_attachment_loc)
        print(file_path)
        time.sleep(2)
        os.system("D:\\test.exe %s"%file_path)

    def get_attachment_title(self):
        '''获取添加的附件的标题'''
        return self.get_attribute(self.attachment_title_loc,"download")

    def check_delete_attchment(self):
        '''检查删除添加的附件后,按钮显示为【添加附件】'''
        self.click(self.delete_attachment_loc)
        return self.is_element_exist(self.add_attachment_loc)

    def edit_notice_body(self,text):
        '''编辑正文'''
        self.switch_to_frame(self.iframe_loc)
        self.switch_to_frame(self.iframe_loc)
        self.send_keys(self.body_loc,text)
        self.switch_to_default_content()

    def get_body_text(self):
        '''获取段落中显示的文本'''
        self.switch_to_frame(self.iframe_loc)
        text=self.get_text(self.body_paragraph_loc)
        self.switch_to_default_content()
        return text

    def  input_title_and_body(self,title="测试标题",body="测试正文"):
        '''输入标题和正文'''
        self.input_title(title)
        self.edit_notice_body(body)

    def get_title_marked_red_checkbox_class_name(self):
        '''获取标题标红复选框的class'''
        checkboxes=self.find_elements(self.checkboxes_loc)
        return  checkboxes[0].get_attribute("class")

    def check_title_marked_red(self):
        '''勾选标题标红'''
        checkboxes = self.find_elements(self.checkboxes_loc)
        checkboxes[0].click()

    def check_title_red(self,title):
        '''在文章列表中检查标题标红'''
        title_eles=self.find_elements(self.row_titles_loc)
        for title_ele in title_eles:
            if title_ele.text==title:
                if title_ele.get_attribute("style")=="color: red;":
                    return True

    def check_title_in_article_list(self,title):
        '''检查文章标题在文章列表中'''
        title_eles = self.find_elements(self.row_titles_loc)
        for title_ele in title_eles:
            if title_ele.text == title:
                return True

    def get_publish_to_scroll_bar_checkbox_class_name(self):
        '''获取发布到滚动栏复选框的class'''
        checkboxes = self.find_elements(self.checkboxes_loc)
        return checkboxes[1].get_attribute("class")

    def check_publish_to_scroll_bar(self):
        '''勾选发布到滚动条'''
        checkboxes = self.find_elements(self.checkboxes_loc)
        checkboxes[1].click()

    def get_scroll_bar_text(self):
        '''获取滚动条文本内容'''
        return self.get_text(self.scroll_bar_loc)

    def click_return(self):
        '''点击【返回】按钮'''
        self.click(self.return_btn_loc)

    def get_not_saving_prompt(self):
        '''获得提示文本内容'''
        self.click_return()
        return self.get_text(self.not_saving_prompt_loc)

    def check_click_close_in_prompt(self):
        '''检查在提示页面点击【关闭】后，停留在编辑页面'''
        self.click(self.close_button_loc)
        return self.is_element_exist(self.return_btn_loc)

    def check_click_confirm_in_prompt(self):
        '''检查在提示页面点击【确定】，返回到文章列表页'''
        self.click(self.release_confirm_loc)
        return self.is_element_exist(self.row_titles_loc)
























