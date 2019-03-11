# selenium_automation

这是一个基于Selenium的Web端的UI自动化测试狂街，采用了PageObject模式。

#

# 目录介绍

    BeautifulReport: 产生HTML Report的模版
    business: 用于处理页面逻辑事件
    common: 初始化 browser
    drivers: 存放各种浏览器的driver
    img: 存放case错误截图
    logs: 存放日志信息
    page: 存放每个页面的元素信息
    report: 存放HTML报告
    test_case: 存放测试用例
    utils: 存放一些公共的方法

# 
# 运行前提先安装依赖
    windows: pip install -r requirements.txt
    如果是 mac os 或者 linux: pip3 install -r requirements.txt