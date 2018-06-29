import apiai
import json


class Dialogflow(apiai.ApiAI):
    def __init__(self, api_key, session_id, lang):
        super().__init__(api_key)
        self.session_id = session_id if session_id else "default"
        self.lang = lang if lang else "en"


    def send_text_message(self, text_message):
        assert type(text_message) == str
        request = self.text_request()
        request.session_id = self.session_id 
        request.lang = self.lang
        request.query = text_message
        self.response = json.load(request.getresponse())


    def get_response(self, *args):
        if len(args) == 0:
            return self.response
        
        response_args = dict()
        if self.response:
            for arg in args:
                try:
                    if '.' in arg:
                        key_list = arg.split('.')
                        desired_item = self.response
                        for cnt in range(len(key_list)):
                            desired_item = desired_item[key_list[cnt]]
                        response_args[arg] = desired_item
                except KeyError:
                    print("erro")
                if arg in self.response.keys():
                    response_args[arg] = self.response[arg]
          
        return response_args

    def _set_session(self, session_id):
        self.session_id = session_id
