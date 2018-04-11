import urllib.parse
from urllib import request
from http import cookiejar
from urllib import error
from urllib import parse
from http import cookiejar
import requests

session = requests.session()

url = 'http://localhost:8000/polls/login'
values = {
    'name':'shiyanlou',
    'pwd':'shiyanlou',
    'commit':'Login'
}
headers = {'Referer':'http://localhost:8000/polls/show_login'}
request = urllib.request.Request(url,data = urllib.parse.urlencode(values).encode(encoding='UTF8'),headers=headers)

# 创建opener
cookies = cookiejar.MozillaCookieJar('my_cookies.txt') # 指定cookie的存储文件
#cookie = cookiejar.CookieJar()
#cookie_handler = urllib.HTTPCookieProcessor(cookies)

handler = urllib.request.HTTPCookieProcessor(cookies)
opener = urllib.request.build_opener(handler)

# 发送请求 & 保存cookie
response = opener.open(request)
cookies.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
print (response.code)
print (response.read())

url2 = 'http://localhost:8000/polls/date'
response2 = opener.open(url2)
print (response2.code)
print (response2.read())
