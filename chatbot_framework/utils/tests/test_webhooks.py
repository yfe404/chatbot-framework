import os
import requests
import time
from flask import Flask, Response, request
from flask_testing import LiveServerTestCase 
from ..webhook import validate_facebook_webhook


class TestMessengerWebhook(LiveServerTestCase):
        
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True

        @app.route('/', methods=['GET'])
        @validate_facebook_webhook(token="good_token")
        def validate_webhook():
            return request

        return app 

    def test_validate_facebook_webhook_nominal_case(self):
        """
        Nominal case: good request with expected parameters.
        """
        res = requests.get(self.get_server_url() +
                           '/?hub.verify_token=good_token&hub.challenge=CHALLENGE_ACCEPTED&hub.mode=subscribe')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.text, "CHALLENGE_ACCEPTED")

    def test_validate_facebook_webhook_missing_token(self):
        """
        Case where the token is missing.
        """
        res = requests.get(self.get_server_url() +
                           '/?hub.challenge=CHALLENGE_ACCEPTED&hub.mode=subscribe')
        self.assertEqual(res.status_code, 403)

        
    def test_validate_facebook_webhook_bad_token_case(self):
        """
        Case where the token doesn't correspond to env var.
        """
        res = requests.get(self.get_server_url() +
                           '/?hub.verify_token=bad_token&hub.challenge=CHALLENGE_ACCEPTED&hub.mode=subscribe')
        self.assertEqual(res.status_code, 403)

