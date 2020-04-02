from selenium import webdriver
from  common.base import Base
import time




class HomePage(Base):
    def open(self,host,PKUser,PKCompany,cityCode="rikaze"):
        '''打开起始页'''
        self.driver.get(host+"/oa/#/startPage?cityCode="+cityCode+"&pkUser="+PKUser+"&pkCompany="+PKCompany)
        self.driver.refresh()
        time.sleep(5)

if __name__ == '__main__':
    driver=webdriver.Chrome(r"D:\chromedriver.exe")
    home=HomePage(driver)
    home.open("https://rikaze.fooww.com/")