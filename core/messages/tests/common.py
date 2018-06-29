"""
Common utilities for testing messages.
"""


def generate_valid_facebook_text_message(recipient_id, sender_id, message_text, timestamp=None, message_id=None):
    data = {
            "object":"page",
            "entry":[
                {
                    "id":recipient_id,
                    "time":timestamp if timestamp else 1458692752478,
                    "messaging":[
                        {
                            "sender":{
                                "id":sender_id
                            },
                            "recipient":{
                                "id":recipient_id
                            },

                            "timestamp":timestamp if timestamp else 1458692752478,
                            "message":{
                                "mid":message_id if message_id else "mid.1457764197618:41d102a3e1ae206a38",
                                "text":message_text,

                            }
                        }
                    ]
                }
            ]
        }

    return data


def generate_valid_facebook_postback_message(recipient_id, sender_id, message_payload, timestamp=None):
    data = {
            "object":"page",
            "entry":[
                {
                    "id":recipient_id,
                    "time":timestamp if timestamp else 1458692752478,
                    "messaging":[
                        {
                            "sender":{
                                "id":sender_id
                            },
                            "recipient":{
                                "id":recipient_id
                            },
                            "timestamp":timestamp if timestamp else 1458692752478,
                            "postback":{
                                "title": "Test postback",
                                "payload": message_payload
                            }
                        }   
                    ]
                }
            ]
        }

    return data


