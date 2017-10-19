from selenium import webdriver

chrome_capabilities={
    'browserName':'chrome',
    'version':'61.0.3163.91',
    'platform':'ANY',
    'javascriptEnabled':True,
    'marionette':True
}

browser=webdriver.Remote('http://192.168.99.100:5555/wd/hub',desired_capabilities=chrome_capabilities)
browser.get('https://www.baidu.com')
browser.get_screenshot_as_file('D:/baidu.png')
browser.close()