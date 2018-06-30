from flask import Flask, Response, request
from chatbot_framework.channels.channel import FacebookMessengerInputChannel, FacebookMessengerOutputChannel
from chatbot_framework.utils.webhook import validate_facebook_webhook
from chatbot_framework.nlp.nlp_engines import Dialogflow

import os 
import string
import random

app = Flask(__name__)
nlp_engine = Dialogflow(
    api_key=os.environ["DIALOGFLOW_API_KEY"],
    session_id=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
    lang="en"
)

@app.route('/', methods=['GET'])
@validate_facebook_webhook(os.environ.get("FB_VERIFY_TOKEN"))
def validate_webhook():
    return request

@app.route('/', methods=['POST'])
def handle_message():

    event = request.get_json()
    input_channel = FacebookMessengerInputChannel(event)
    output_channel = FacebookMessengerOutputChannel(event, os.environ.get("FB_ACCESS_TOKEN"))
    message = input_channel.get_message()

    if message.message_type == "text":
        nlp_engine.send_text_message(message.content)
        response_from_nlp_engine = nlp_engine.get_response("result.fulfillment.speech")
        text_response_from_nlp_engine = response_from_nlp_engine.get("result.fulfillment.speech")
        res = output_channel.send_text_message(text_response_from_nlp_engine)

    res = Response("OK", status=200, mimetype='application/text')
    return res

if __name__ == '__main__':
    app.run()

