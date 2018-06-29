from ..factories import FacebookMessengerMessageFactory
from .common import generate_valid_facebook_text_message, generate_valid_facebook_postback_message

import unittest

class TestFactoriesMethods(unittest.TestCase):

    def test_can_create_message_text_from_facebook(self):

        recipient_id = 1
        sender_id = 2
        message_text = "Hello World!"

        event = generate_valid_facebook_text_message(recipient_id, sender_id, message_text)

        message = FacebookMessengerMessageFactory.create_message(event)

        self.assertEqual(message.message_type, 'text')
        self.assertEqual(message.content, message_text)
        self.assertEqual(message.sender, sender_id)

    def test_can_create_message_postback_from_facebook(self):

        recipient_id = 1
        sender_id = 2
        message_payload = "HELLO_POSTBACK"

        event = generate_valid_facebook_postback_message(recipient_id, sender_id, message_payload)

        message = FacebookMessengerMessageFactory.create_message(event)

        self.assertEqual(message.message_type, 'postback')
        self.assertEqual(message.content, message_payload)
        self.assertEqual(message.sender, sender_id)

    

if __name__ == '__main__':
    unittest.main()






