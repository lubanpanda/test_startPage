from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import  ActionChains
import logging.config
import time


#基于原生的selenium做二次封装
class Base():
     def __init__(self,driver,time=10,t=0.5):
         self.driver=driver
         self.timeout=time    #最长超时时长
         self.t=t        #查询元素的间隔时间


     def find_element(self,locator):
         '''
         定位单个元素：定位到元素，返回元素对象，没定位到，TimeOut异常
         :param locator: 元组类型 定位方式+属性值 类似("xpath","xpath语句") ("id","id属性值") ("css selector","css选择语句")
         :return:
         '''
         if not isinstance(locator,tuple):#检查传的参数是否为元组类型
             logging.error('locator参数类型错误，必须传元组类型：loc=("id","value")')
         else:
            logging.info("正在定位元素信息:定位方式->%s,Value值->%s"%(locator[0],locator[1]))
            ele=WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
            return ele

     def find_elements(self,locator):
         '''
         定位一组元素：定位到元素，返回元素列表，没定位到，返回空列表
         :param locator: 元组类型 定位方式+属性值 类似("xpath","xpath语句") ("id","id属性值") ("css selector","css选择语句")
         :return:
         '''
         if not isinstance(locator,tuple):#检查传的参数是否为元组类型
            logging.error('locator参数类型错误，必须传元组类型：loc=("id","value")')
         try:
             logging.info("正在定位元素信息：定位方式->%s，value值->%s"%(locator[0],locator[1]))
             eles=WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_all_elements_located(locator))
             return eles
         except:
             return []

     def send_keys(self,locator,text=""):
         '''
         文本框赋值
         :param locator:
         :param text:
         :return:
         '''
         ele=self.find_element(locator)
         ele.send_keys(text)

     def click(self,locator):
         '''
         点击元素
         :param locator:
         :return:
         '''
         ele=self.find_element(locator)
         ele.click()


     def clear(self,locator):
         '''
         清空文本框内容
         :param locator:
         :return:
         '''
         ele=self.find_element(locator)
         ele.clear()

     def is_selected(self,locator):
         '''
         判断元素是否被选中，返回bool值
         :param locator:
         :return: bool类型
         '''
         ele=self.find_element(locator)
         r=ele.is_selected()
         return r

     def is_element_exist(self,locator):
         '''
         判断元素是否存在，返回bool值
         :param locator:
         :return: bool类型
         '''
         try:
             self.find_element(locator)
             return True
         except:
             return False

     def is_title(self,title=''):
         '''
         判断标题是否与预期结果一致，返回bool值
         :param title:
         :return:bool类型
         '''
         try:
             result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(title))
             return result
         except:
             return False

     def is_title_ontains(self,title=''):
        '''
        判断标题是否包含预期内容，返回bool值
        :param title:
        :return: bool类型
        '''
        try:
            result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(title))
            return result
        except:
            return False

     def is_text_in_element(self,locator,text=''):
         '''
         判断指定元素中是否包含预期字符串，返回bool值
         :param locator:
         :param text:
         :return:
         '''
         if not isinstance(locator,tuple):
             logging.error('locator参数类型错误，必须传元组类型：loc=("id","value")')
         try:
             result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,text))
             return result
         except:
             return False

     def is_value_in_element(self,locator,value=''):
         '''
         判断指定元素的value属性值中包含预期字符串，返回bool值
         :param locator:
         :param value:
         :return:
         '''
         if not isinstance(locator,tuple):
             logging.error('locator参数类型错误，必须传元组类型：loc=("id","value")')
         try:
             result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator,value))
             return result
         except:
             return False

     #判断页面上是否有alert，返回bool值
     def is_alert(self,timeout=3):
         '''
         判断页面上是否有alert，返回bool值
         :param timeout:
         :return:
         '''
         try:
             result=WebDriverWait(self.driver,timeout,self.t).until(EC.alert_is_present())
             return result
         except:
             return False

     def switch_alert(self):
         '''
         切换到alert并返回alert的内容
         :return:
         '''
         r=self.is_alert()
         if not r:
             logging.info("alert不存在")
         else:
             return r

     def  get_title(self):
         '''
         获取title值
         :return:
         '''
         return self.driver.title

     def get_text(self,locator):
        '''
        获取文本
        :param locator:
        :return:
        '''
        try:
             text=self.find_element(locator).text
             return text
        except:
            logging.info('获取text失败，返回""')
            return ""

     def get_attribute(self,locator,attribute_name):
         '''
         获取属性
         :param locator:
         :param attribute_name:
         :return:
         '''
         try:
             ele=self.find_element(locator)
             return ele.get_attribute(attribute_name)
         except:
             logging.info('获取%s失败，返回""'%attribute_name)
             return ""

     def js_focus_element(self,locator):
         '''
         聚焦元素
         :param locator:
         :return:
         '''
         target=self.find_element(locator)
         js="arguments[0].scrollIntoView();"
         self.driver.execute_script(js,target)

     def js_scroll_top(self):
         '''
         滚动到顶部
         :return:
         '''
         js="window.scrollTo(0,0)"
         self.driver.execute_script(js)

     def js_scroll_bottom(self,x=0):
         '''
         滚动到底部
         :param x:
         :return:
         '''
         js="window.scrollTo(%s,document.body.scrollHeight)"%x
         self.driver.execute_script(js)

     def select_by_index(self,locator,index=0):
         '''
         根据索引选择下拉框选项,默认选第1个
         :param locator:
         :param index:
         :return:
         '''
         ele=self.find_element(locator)#定位select这一栏
         Select(ele).select_by_index(index)

     def select_by_value(self,locator,value):
         '''
         根据value属性定位下拉框选项
         :param locator:
         :param value:
         :return:
         '''
         ele=self.find_element(locator)#定位select这一栏
         Select(ele).select_by_value(value)

     def select_by_text(self,locator,text):
         '''
         根据文本值定位下拉框选项
         :param locator:
         :param text:
         :return:
         '''
         ele = self.find_element(locator)  # 定位select这一栏
         Select(ele).select_by_visible_text(text)

     def switch_to_frame(self,id_index_locator):
         '''
         切换iframe
         :param id_index_locator:
         :return:
         '''
         try:
            #用index定位
             if isinstance(id_index_locator,int):
                 self.driver.switch_to.frame(id_index_locator)
             #用id/name定位
             elif isinstance(id_index_locator,str):
                 self.driver.switch_to.frame(id_index_locator)
             #用find_element系列方法取得WebElement对象
             elif isinstance(id_index_locator,tuple):
                 ele=self.find_element(id_index_locator)
                 self.driver.switch_to.frame(ele)
         except:
             logging.info("iframe切换异常")

     def switch_to_default_content(self):
         '''从frame中切回主文档'''
         self.driver.switch_to.default_content()

     def switch_window(self,window_name):
         '''
         切换到指定的window_name页面，window_name:指定页面窗口的handle
         :param window_name:
         :return:
         '''
         self.driver.switch_to.window(window_name)

     def move_to_element(self,locator):
         '''
         鼠标悬停操作
         :param locator:
         :return:
         '''
         ele=self.find_element(locator)
         ActionChains(self.driver).move_to_element(ele).perform()

if __name__ == '__main__':
    driver=webdriver.Chrome(r"D:\chromedriver.exe")
    web=Base(driver)

























