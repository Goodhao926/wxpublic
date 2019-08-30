#coding:utf-8
#作者 ：Goodhao
#Version : 1.0
#Time : 2019/7/21 21:02
import requests
import re
import urllib

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def GetExpression_All(main_url = None):
    pattern = '<a class="col-xs-6 col-md-2" href=".*?" style="padding:5px;"><img referrerpolicy="no-referrer" src=".*?" data-backup=".*?" class="img-responsive lazy image_dtb" data-original="(.*?)" style="width: 100%;"><p style="display: none">(.*?)</p></a>'
    respond = requests.get(main_url)#获取
    re_compile = re.compile(pattern)
    re_result =  re_compile.findall(respond.text.replace('\n',''))#正则匹配
    print  respond.text
    return  re_result
def GetExpression_Search(content):
    url = 'https://www.doutula.com/search?keyword='+urllib.quote_plus(content.encode('utf-8'))
    pattern = '<a class="col-xs-6 col-md-2" href=".*?" style="padding:5px;"><img referrerpolicy="no-referrer" src="//www.doutula.com/img/loader.gif" data-backup=".*?" class="img-responsive lazy image_dtb" data-original="(.*?)" style="width: 100%;"><p style="display: none">(.*?)</p>'
    respond = requests.get(url)#获取
    re_compile = re.compile(pattern)
    re_result =  re_compile.findall(respond.text.replace('\n',''))#正则匹配
  #  print respond.text
    return  re_result
def show_photo(locals):
    img = Tkinter.PhotoImage(locals)
    Canvas = Tkinter.Canvas(root, height=600, width=600, bg='pink')
    Canvas.create_image(0, 0, image=img)
    Canvas.pack()
def dowload_photo(url,local): 
        r = requests.get(url)
        with open(local,'wb') as f:
            	f.write(r.content)
def download():
    content = '不知道'
    result = GetExpression_Search(content)
    for item in range(len(result)):
        dowload_photo(result[item][0],"d:/image/" + result[item][1] + ".gif")
