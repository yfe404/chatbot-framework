from .message import MessageText, MessagePostback

class AbstractMessageFactory(object):
    """ Provide an interface for creating Message objects. """ 
    pass

class FacebookMessengerMessageFactory(AbstractMessageFactory):
    """ Provide an interface for creating Message objects
     coming from Facebook Messenger
    """

    @staticmethod
    def create_message(event):

        message = None
        if event["object"] == "page":
            for entry in event["entry"]:
                for messaging_event in entry["messaging"]:
                    sender_id = messaging_event["sender"]["id"]
                    recipient_id = messaging_event["recipient"]["id"]

                    if messaging_event.get("message"):
                        message_text = messaging_event["message"].get("text")
                        if message_text:
                            message = MessageText(message_text, sender_id)
        
                    elif messaging_event.get("postback"):
                        message_payload = messaging_event["postback"].get("payload")
                        if message_payload:
                            message = MessagePostback(message_payload, sender_id)
        return message

