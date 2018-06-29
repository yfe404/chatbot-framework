class Message(object):
    """ Represents an incoming message. """
    pass

class MessageText(Message):
    """ Represents a text message """

    def __init__(self, content, sender=None):
        self.message_type = "text"
        self.content = content
        self.sender = sender

class MessagePostback(Message):
    """ Represents a postback message """

    def __init__(self, content, sender=None):
        self.message_type = "postback"
        self.content = content
        self.sender = sender



