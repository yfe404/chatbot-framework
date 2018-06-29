import requests 
import json

from ..messages.factories import FacebookMessengerMessageFactory


class FacebookMessengerInputChannel(object):

    def __init__(self, event):
        self.event = event

    def get_message(self):
        message = FacebookMessengerMessageFactory.create_message(self.event)
        return message
    

class FacebookMessengerOutputChannel(object):

    def __init__(self, event, fb_access_token):
        self.event = event

        if not fb_access_token :
            raise MissingTokenException("fb_access_token required.")
        else:
            self.fb_access_token = fb_access_token
        self.send_api_url = "https://graph.facebook.com/v2.6/me/messages?access_token=" + self.fb_access_token

    def send_text_message(self, content):
        message = FacebookMessengerMessageFactory.create_message(self.event)
        data = None
        if message:
            data = {
                'recipient':{
                    'id':message.sender
                },
                'message':{
                    'text':content
                }
            }
        res = requests.post(self.send_api_url, data=json.dumps(data), headers={'Content-Type':'Application/json'})

        return res

    
class  MissingTokenException(Exception):
    pass









        
    
