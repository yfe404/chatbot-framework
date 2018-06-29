import unittest
import time 

from ..nlp_engines import Dialogflow

class TddDialogflowWrapper(unittest.TestCase):
    
    def setUp(self):
        api_key = "3b43833d08be4225a7552e5d5a646631"
        self.dialogflow = Dialogflow(api_key, "my_session", "en")

    def test_send_text_message(self):
        
        message = "Hello!"
        self.dialogflow.send_text_message(message)
        resolved_query = self.dialogflow.response.get("result").get("resolvedQuery")

        assert resolved_query == message
        
    def test_get_response(self):

        message = "Hello!"
        self.dialogflow.send_text_message(message)
        response = self.dialogflow.get_response("result.fulfillment.speech", "result.resolvedQuery", "result.action")

        assert response.get("result.fulfillment.speech").startswith("Hello and welcome")
        assert response.get("result.resolvedQuery") == message
        assert response.get("result.action") == "say-hello"


    def test_set_session(self):

        session_id_0 = "session0" + str(time.time())
        session_id_1 = "session1" + str(time.time())

        message_0_from_session_0 = "Hello"
        message_1_from_session_0 = "okay"
        message_0_from_session_1 = "Hello"
        
        self.dialogflow._set_session(session_id_0)
        self.dialogflow.send_text_message(message_0_from_session_0)
        response = self.dialogflow.get_response("result.fulfillment.speech")
        assert response.get("result.fulfillment.speech").startswith("Hello and welcome")

        self.dialogflow.send_text_message(message_1_from_session_0)
        response = self.dialogflow.get_response("result.fulfillment.speech")
        assert response.get("result.fulfillment.speech").startswith("Can you write you name")

        self.dialogflow._set_session(session_id_1)
        self.dialogflow.send_text_message(message_0_from_session_1)
        response = self.dialogflow.get_response("result.fulfillment.speech")
        assert response.get("result.fulfillment.speech").startswith("Hello and welcome")


if __name__ == '__main__':
    unittest.main()


        
