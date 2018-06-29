from ..channel import FacebookMessengerInputChannel, FacebookMessengerOutputChannel, MissingTokenException

import unittest
import os 

class TestChannelsMethods(unittest.TestCase):
    def test_throws_correct_exception_when_fb_access_token_missing(self):
        self.assertRaises(MissingTokenException, FacebookMessengerOutputChannel, None, None)

    def test_throws_correct_exception_when_fb_access_token_is_empty(self):
        fb_access_token =  ""
        self.assertRaises(MissingTokenException, FacebookMessengerOutputChannel, None, fb_access_token)

    def test_dont_throws_exception_when_fb_access_token_in_env_variables(self):
        fb_access_token = "mytoken"
        out_chan = FacebookMessengerOutputChannel(None, fb_access_token)
        self.assertEquals(out_chan.send_api_url[-len(fb_access_token):], fb_access_token)

if __name__ == '__main__':
    unittest.main()






