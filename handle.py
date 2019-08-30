#coding:utf-8
import web
import hashlib
import reply
import receive
import requests
from deal import char














def post_image(file_name):
    url = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token='+access_token+'&type=image'
    return requests.post(url,file = file_name)
    




class Handle:
    def GET(self):
        data = web.input()
        if data==0:
            print 'Error:data = None'
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        token = 'goodhao926'
        list = [token,timestamp,nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,list)
        hashcode = sha1.hexdigest()
        print signature,timestamp,nonce
        if hashcode == signature:
            return echostr
        else:
            return ''
    def POST(self):
        post_data = web.data()
        # print "Handle Post webdata is ", post_data
        recMsg = receive.parse_xml(post_data)
        if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName

            content, msg_type = char(recMsg.Content)
            if msg_type == 'image':
                replyMsg = reply.ImageMsg(toUser, fromUser, content)
            elif msg_type == 'text':
                replyMsg = reply.TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        else:
            return 'success'



            
            
