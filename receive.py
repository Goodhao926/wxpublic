# -*- coding: utf-8 -*-
# filename: receive.py

import xml.etree.ElementTree as ET
class Msg(object):
    def __init__(self,xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text
class TextMsg(Msg):
    def __init__(self,xmlData):
        Msg.__init__(self,xmlData)
        self.Content = xmlData.find('Content').text.encode('utf-8')
class ImageMsg(Msg):
    pass

        

def parse_xml(xml_data):
    if xml_data == 0:
        return None
    xmlData = ET.fromstring(xml_data)
    msg_type = xmlData.find('MsgType').text
    if msg_type == 'text':
        return TextMsg(xmlData)
    elif msg_type == 'image':
        pass
        
    
        
