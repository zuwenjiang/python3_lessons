import urllib.parse
from urllib import request
from http import cookiejar
from urllib import error
from urllib import parse
from http import cookiejar
import requests
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()


#点击单位登录
driver.get('https://ln.122.gov.cn/user/m/login')

action1 = ActionChains(driver)
source1=driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[2]/a")
driver.find_element_by_link_text("单位登录").click()


#滑动滑块
#action = ActionChains(driver)
#source=driver.find_element_by_xpath("//*[@id='nc_4_n1z']")#需要滑动的元素
#action.click_and_hold(source).perform()  #鼠标左键按下不放
#action.move_by_offset(258,0)#需要滑动的坐标
#action.release().perform() #释放鼠标


##session = requests.session()

#url = 'https://ln.122.gov.cn/user/m/login'

#values = {
#    'usertype':'2',
#    'systemid':'main',
#    'username':'21021711007410',
#    'password':'jmkj123456',
#    'captcha':'',
#    'scene':'login'
#}
#headers = {'Referer':'https://ln.122.gov.cn/m/login'}
#request = urllib.request.Request(url,data = urllib.parse.urlencode(values).encode(encoding='UTF8'),headers=headers)
#cookies = cookiejar.MozillaCookieJar('lncookies.txt') # 指定cookie的存储文件

#handler = urllib.request..HTTPCookieProcessor(cookies)
opener = urllib.request.build_opener()

# 发送请求 & 保存cookie
#response = opener.open(request)
#cookies.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中

url2 = 'http://ln.122.gov.cn/user/m/uservio/suriquery'
values2 = {
    'startDate':'20180101',
    'endDate':'20180407',
    'hpzl':'02',
    'hphm':'辽B9UC59',
    'page':'1',
    'type':'0'
}

headers2 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0','Referer':'http://ln.122.gov.cn/user/m/uservio/suriquery'}
request2 = urllib.request.Request(url2,data = urllib.parse.urlencode(values2).encode(encoding='UTF8'),headers=headers2)
response2 = opener.open(request2)
print (response2.code)
print (response2.read().decode('utf-8'))