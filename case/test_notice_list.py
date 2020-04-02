import pytest
from page.home_page import *
from page.notice_list_page import *
import time

'''测试公告列表页'''
class TestNoticeList():

    def enter_in_notice_page(self,driver,host,pkUser,pkCompany):
        '''进入公司公告页'''
        HomePage(driver).open(host,pkUser,pkCompany)
        list=NoticeListPage(driver)
        list.enter_in_page()
        return  list

    # def test_operation_column_exist(self,driver,host):
    #     '''检查有【管理公司-全公司】和管理起始页权限，显示【操作】列'''
    #     list = self.enter_in_notice_page(driver, host, "d43c2133-a058-487d-b271-ade608548bfb",
    #                                         "68dc0e06-82b7-4024-9a5b-ae921cc53914")
    #     result=list.check_operation_column_exist()
    #     assert result==True
    #
    # def test_operation_column_not_exist(self,driver,host):
    #     '''检查没有【管理公司-全公司】或管理起始页权限，不显示【操作】列'''
    #     list=self.enter_in_notice_page(driver, host, "a01ef2d3-e87f-4910-9c37-288a3dca325e",
    #                                     "68dc0e06-82b7-4024-9a5b-ae921cc53914")
    #     result=list.check_operation_column_exist()
    #     assert result==False

    # def test_top_notice(self,driver,host):
    #     '''测试置顶'''
    #     list = self.enter_in_notice_page(driver, host, "d43c2133-a058-487d-b271-ade608548bfb",
    #                                      "68dc0e06-82b7-4024-9a5b-ae921cc53914")
    #     #检查置顶当前页面最后一篇文章
    #     article_title=list.top_or_cancel_top_notice(-1)
    #     assert list.get_toast_text()=="置顶成功"
    #     index=list.get_title_index(article_title) #获取该标题的索引
    #     assert list.get_top_icon_title_attribute(index)=="取消置顶"#检查【置顶】按钮变成【取消置顶】
    #     assert list.check_top_icon_exist(index) == True  #检查对应文章行中存在【顶】图标
    #
    # def test_cancel_top_notice(self,driver,host):
    #     '''测试取消置顶'''
    #     list = self.enter_in_notice_page(driver, host, "d43c2133-a058-487d-b271-ade608548bfb",
    #                                  "68dc0e06-82b7-4024-9a5b-ae921cc53914")
    #     #检查取消置顶当前页面第一篇文章
    #     article_title = list.top_or_cancel_top_notice(0)
    #     assert list.get_toast_text() == "取消置顶成功"
    #     index = list.get_title_index(article_title)  # 获取该标题的索引
    #     assert list.get_top_icon_title_attribute(index) == "置顶"  # 检查【取消置顶】按钮变成【置顶】
    #     assert list.check_top_icon_exist(index) == False  # 检查对应文章行中不存在【顶】图标

    def test_refresh(self,driver,host):
        '''测试刷新'''
        list = self.enter_in_notice_page(driver, host, "d43c2133-a058-487d-b271-ade608548bfb",
                                         "68dc0e06-82b7-4024-9a5b-ae921cc53914")
        # 刷新非置顶公告
        top_notice_len = list.get_top_notice_length()  # 获取置顶公告的个数
        toast_text,time_difference,index_after= list.check_refresh_notice(-1)
        assert toast_text=="公告刷新成功"
        assert time_difference==0.0
        assert index_after==top_notice_len
        #刷新置顶公告
        toast_text,time_difference,index_after=list.check_refresh_notice(top_notice_len-1)
        assert toast_text == "公告刷新成功"
        assert time_difference == 0.0
        assert index_after == 0























