'''
主要功能：
1、当测试完成后，生成html报告里面，插入失败截图功能
2、添加命令行参数browser,用于切换不同浏览器测试
3、添加命令行参数，用于切换不同测试环境host
4、全局参数driver调用
5、全局参数host调用
'''
from selenium import webdriver
import pytest
from py._xmlgen import  html
import logging.config

_driver=None

CON_LOG='./config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()


def pytest_addoption(parser):
    #添加命令行参数--browser
    parser.addoption(
        "--browser",action="store",default="chrome",help='browser option:firefox or chrome'
    )
    #添加命令行参数--host
    parser.addoption(
        "--host",action='store',default='https://test-companyoa.fooww.com',help="test host->https://companyoa.fooww.com/"
    )

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    '''当测试失败的时候，自动截图，展示到html报告中'''
    pytest_html=item.config.pluginmanager.getplugin('html')
    outcome=yield
    report=outcome.get_result()
    extra=getattr(report,'extra',[])

    if report.when == 'call' or report.when == 'steup':
        xfail=hasattr(report,'wasfail')
        if(report.skipped and xfail) or (report.failed and not xfail):
            file_name=report.nodeid.replace("::","_")+"png"
            screen_img = _driver.get_screenshot_as_base64()#截图保存为base64
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;"onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid=report.nodeid.encode("utf-8").decode("unicode_escape")

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    '''插入Description列和Test_nodeid列，删除原有的Test列'''
    cells.insert(1,html.th('Description'))
    cells.insert(2,html.th('Test_nodeid'))
    cells.pop(2)

@pytest.mark.optionalhook
def pytest_html_results_table_row(report,cells):
    '''Description列添加详情和Test_nodeid列添加详情，删除原有的Test列'''
    cells.insert(1,html.td(report.description))
    cells.insert(2,html.td(report.nodeid))
    cells.pop(2)

@pytest.fixture(scope='session',autouse=True)
def driver(request):
    global  _driver#定义全局变量driver
    if _driver is None:
        name=request.config.getoption("--browser")
        if name=='firefox':
            _driver=webdriver.Firefox()
        elif name=="chrome":
            _driver=webdriver.Chrome(r"D:\chromedriver.exe")
        else:
            _driver = webdriver.Chrome(r"D:\chromedriver.exe")
        logging.info("正在启动浏览器名称:%s"%name)
        _driver.maximize_window()#最大化浏览器
    def end():
        logging.info("当全部用例执行完之后，teardown quit driver!")
        _driver.quit()
    request.addfinalizer(end)
    return  _driver

@pytest.fixture(scope='session')
def host(request):
    '''全局host参数'''
    return  request.config.getoption("--host")



