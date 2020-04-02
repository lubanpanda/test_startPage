import pytest
from page.home_page import *
from page.add_company_notice import *
import time

'''测试新增公告'''
class TestAddNotice():
    def enter_in_notice_page(self,driver,host,pkUser,pkCompany):
        '''进入公司公告页'''
        HomePage(driver).open(host,pkUser,pkCompany)
        add=AddCompanyNotice(driver)
        add.enter_in_page()
        return  add

    # def test_exist_add_button(self, driver, host):
    #     '''测试有新增管理公司权限-显示【新增文章】按钮'''
    #     add = self.enter_in_notice_page(driver, host, "d43c2133-a058-487d-b271-ade608548bfb",
    #                                     "68dc0e06-82b7-4024-9a5b-ae921cc53914")
    #     result = add.check_add_article_button()
    #     assert result == True
    #     time.sleep(5)
    #
    # def test_notExist_add_button(self, driver, host):
    #     '''测试没有新增管理公司权限-显示【新增文章】按钮'''
    #     add = self.enter_in_notice_page(driver, host, "a01ef2d3-e87f-4910-9c37-288a3dca325e",
    #                                     "68dc0e06-82b7-4024-9a5b-ae921cc53914")
    #     time.sleep(4)
    #     result = add.check_add_article_button()
    #     assert result == False
    #
    # def test_article_type(self, driver, host):
    #     '''测试新增文章的类型'''
    #     add = self.enter_in_notice_page(driver, host, "d43c2133-a058-487d-b271-ade608548bfb",
    #                                     "68dc0e06-82b7-4024-9a5b-ae921cc53914")
    #     add.click_add_article_button()
    #     assert add.get_title() == "编辑/新增公告"  # 检查新增公告页面显示
    #     selected_type = add.get_selected_type()
    #     assert selected_type == "公司公告"  # 检查默认选中类型
    #     all_types = add.get_all_types()
    #     assert all_types == ["公司公告", "门店公告", "规章制度", "新增类型"]  # 检查所有类型
    #
    # def test_article_title(self, driver, host):
    #     '''测试新增文章的标题'''
    #     add = self.enter_in_notice_page(driver, host, "d43c2133-a058-487d-b271-ade608548bfb",
    #                                     "68dc0e06-82b7-4024-9a5b-ae921cc53914")
    #     add.click_add_article_button()
    #     # 检查不输入标题
    #     add.input_title()
    #     add.click_realease()
    #     assert add.get_toast_text() == "标题不能为空"
    #     # 检查标题小于4个中文字符
    #     time.sleep(3)
    #     add.input_title("测试")
    #     add.click_realease()
    #     assert add.get_toast_text() == "标题不少于4个字"
    #     # 检查输入超过40位字符  ！！！！无法获取到标题文本框中的内容
    #     # add.input_title("测试数据"*12)
    #     # title_text=add.get_title_text()
    #     # assert title_text=="测试数据"*10
    #     # 输入大于4个小于40个任意字符
    #     time.sleep(3)
    #     add.input_title("测试aa123")
    #     add.click_realease()
    #     assert add.get_toast_text() == "内容不能为空"
    #
    # def test_add_attachment(self,driver,host):
    #     '''检查新增文章添加附件'''
    #     add = self.enter_in_notice_page(driver, host,"d43c2133-a058-487d-b271-ade608548bfb","68dc0e06-82b7-4024-9a5b-ae921cc53914")
    #     add.click_add_article_button()
    #     #检查附件大小提示文本
    #     attachment_tip_text=add.get_attachment_tip_text()
    #     assert attachment_tip_text=="(附件大小不超过5M)"
    #     #上传应用程序附件
    #     add.add_attachment("D:\\phpStudy.exe")
    #     assert  "格式不对" in add.get_toast_text()
    #     time.sleep(2)
    #     #上传大于5M的文件
    #     add.add_attachment("D:\\chromedriver.exe")
    #     assert  add.get_toast_text()=="仅支持5M以内文件上传"
    #     time.sleep(2)
    #     #上传支持的文件
    #     add.add_attachment("D:\\1.txt")
    #     assert  add.get_toast_text()=="上传成功"
    #     assert  add.get_attachment_title()=="1.txt"
    #     #检查删除附件
    #     assert add.check_delete_attchment()
    #     #再次添加附件
    #     add.add_attachment("D:\\2.txt")
    #     assert add.get_toast_text() == "上传成功"
    #     assert add.get_attachment_title() == "2.txt"
    #
    # def test_edit_notice_body(self,host,driver):
    #     '''检查编辑正文'''
    #     add = self.enter_in_notice_page(driver, host, "d43c2133-a058-487d-b271-ade608548bfb",
    #                                     "68dc0e06-82b7-4024-9a5b-ae921cc53914")
    #     add.click_add_article_button()
    #     add.input_title("测试aa123")
    #     #检查不输入内容
    #     add.click_realease()
    #     assert add.get_toast_text() == "内容不能为空"
    #     #检查输入任意类型内容
    #     text="张三123；！aaaddd"
    #     add.edit_notice_body(text)
    #     assert  text==add.get_body_text()
    #     #检查输入内容超过2万字
    #     # text2="测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试" \
    #     #       "测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试"*250
    #     # add.edit_notice_body(text2)
    #     # add.click_realease()
    #     # assert add.get_toast_text() == "公告正文最多2万字"
    #
    # def test_title_marked_red(self,driver,host):
    #     '''检查标题标红复选框'''
    #     add = self.enter_in_notice_page(driver, host, "d43c2133-a058-487d-b271-ade608548bfb",
    #                                     "68dc0e06-82b7-4024-9a5b-ae921cc53914")
    #     add.click_add_article_button()
    #     #检查默认不勾选
    #     class_name=add.get_title_marked_red_checkbox_class_name()
    #     assert "is-checked" not  in class_name
    #     #检查勾选后标题为红色字体
    #     title="测试"+time.strftime("%Y_%m_%d_%H_%M_%S")
    #     add.input_title_and_body(title,"测试正文")
    #     add.check_title_marked_red()
    #     add.click_and_confirm_release()
    #     assert add.check_title_red(title)

    def test_publish_to_scroll_bar(self,driver,host):
        '''检查发布到滚动栏复选框'''
        add = self.enter_in_notice_page(driver, host, "d43c2133-a058-487d-b271-ade608548bfb",
                                        "68dc0e06-82b7-4024-9a5b-ae921cc53914")
        add.click_add_article_button()
        # 检查默认不勾选
        class_name=add.get_publish_to_scroll_bar_checkbox_class_name()
        assert "is-checked" not in class_name
        #检查勾选发布到滚动栏
        title = "测试" + time.strftime("%Y_%m_%d_%H_%M_%S")
        add.input_title_and_body(title, "测试正文")
        add.check_publish_to_scroll_bar()
        add.click_and_confirm_release()
        assert  add.get_scroll_bar_text() == title

    def test_release_article(self,driver,host):
        '''测试发布'''
        add = self.enter_in_notice_page(driver, host, "d43c2133-a058-487d-b271-ade608548bfb",
                                        "68dc0e06-82b7-4024-9a5b-ae921cc53914")
        add.click_add_article_button()
        title = "测试" + time.strftime("%Y_%m_%d_%H_%M_%S")
        add.input_title_and_body(title, "测试正文")
        #检查发布
        add.click_and_confirm_release()
        assert  add.get_toast_text()=="操作成功"
        #检查发布的文章显示在文章列表中
        assert  add.check_title_in_article_list(title)

    def test_cancel_edit(self,driver,host):
        '''测试取消编辑'''
        add = self.enter_in_notice_page(driver, host, "d43c2133-a058-487d-b271-ade608548bfb",
                                        "68dc0e06-82b7-4024-9a5b-ae921cc53914")
        add.click_add_article_button()
        title = "测试" + time.strftime("%Y_%m_%d_%H_%M_%S")
        add.input_title_and_body(title, "测试正文")
        #检查点击【返回】显示的提示信息文本
        assert add.get_not_saving_prompt()=="您编辑的内容尚未保存，离开会使内容丢失。是否确认离开？"
        #检查在提示页面点击【关闭】按钮
        assert add.check_click_close_in_prompt()==True
        #检查在提示页面点击【确定】按钮
        add.click_return()
        assert add.check_click_confirm_in_prompt()==True




















if __name__ == '__main__':
    pytest.main(["-s","test_add_company_notice.py"])