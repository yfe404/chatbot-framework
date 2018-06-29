import os
from flask import Response

def validate_facebook_webhook(token):
    def decorator(func):
        def func_wrapper(*args, **kwargs):
            request = func(*args, **kwargs)
            if request.args.get('hub.verify_token', '') == token:
                response = Response(request.args.get('hub.challenge', ''), status=200, mimetype='application/text')
            else:
                response = Response("Error, wrong validation token", status=403, mimetype='application/text')
            return response

        return func_wrapper
    return decorator
