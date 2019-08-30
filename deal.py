# coding:utf-8
# filename:deal.py
from function import GetExpression_Search

from function import dowload_photo#url ,local

import requests


import json



#http请求方式：POST/FORM，使用https
#https://api.weixin.qq.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE
#调用示例（使用curl命令，用FORM表单方式上传一个多媒体文件）：
#curl -F media=@test.jpg "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE"


class wx_deal:
        access_token = ''
        image_message = ''
        def __init__(self):
                wx_deal.access_token =self.get_access_token()

        def get_access_token(self):
                url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx4222d795efaa84b0&secret=f6167154ecb20dabd65354f7cc42789c'
                result = json.loads(requests.get(url).text.encode('utf-8')) 
                return result.get('access_token')
        def updata_photo(self,file_name):#返回图片
                openFile = open(file_name, "rb")
                param = {'media': openFile}
                postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=image" % (wx_deal.access_token)
                request = requests.post(postUrl,files =param)
                return json.loads(request.text).get('media_id')
    



def char(data):
    wx = wx_deal()
    # 表情处理
    if (data.find('表情') != -1):
        if (data.find('文本') != -1):
            data = data.replace('表情', '')
            data = data.replace('文本', '')
            result = GetExpression_Search(data)
            msg_type = 'text'
            
            text=''
            for i in range(5):
                text += result[i][1]+':'+result[i][0]+'\n'
            return text, msg_type
        else:
            data = data.replace('表情', '')
            result = GetExpression_Search(data)
            msg_type = 'image'
            local = 'c:/wxpublic/temp.gif'
            dowload_photo(result[0][0], local)
            img_id = wx.updata_photo(local)
            return img_id, msg_type



