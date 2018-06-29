import os

from flask import Flask, Response, request
from chatbot_framework.channels.channel import FacebookMessengerInputChannel, FacebookMessengerOutputChannel
from chatbot_framework.utils.webhook import validate_facebook_webhook

app = Flask(__name__)

@app.route('/', methods=['GET'])
@validate_facebook_webhook(os.environ.get("FB_VERIFY_TOKEN"))
def validate_webhook():
    return request

@app.route('/', methods=['POST'])
def handle_message():

    """ Example code for a simple echo bot for Facebook messenger """

    event = request.get_json()
    input_channel = FacebookMessengerInputChannel(event)
    output_channel = FacebookMessengerOutputChannel(event, os.environ.get("FB_ACCESS_TOKEN"))
    message = input_channel.get_message()

    if message.message_type == "text":
        res = output_channel.send_text_message(message.content)

    res = Response("OK", status=200, mimetype='application/text')
    return res

if __name__ == '__main__':
    app.run()

