import time
import os
import httplib
import urllib

class PushoverSender:
    def __init__(self, user_key, api_key):
        self.user_key = user_key
        self.api_key = api_key

    def send_notification(self, text):
        conn = httplib.HTTPSConnection("api.pushover.net:443")
        post_data = {'user': self.user_key, 'token': self.api_key, 'message': text}
        conn.request("POST", "/1/messages.json",
                    urllib.urlencode(post_data), {"Content-type": "application/x-www-form-urlencoded"})

def get_key(filename):
    with open(filename) as f:
        key = f.read().strip()
    return key

def main():
    user_key = get_key(os.path.join(os.path.dirname(__file__), 'user.key'))
    api_key = get_key(os.path.join(os.path.dirname(__file__), 'apitoken.key'))

    pushover_sender = PushoverSender(user_key, api_key)
    pushover_sender.send_notification('hello pushover')

if __name__ == '__main__':
    main()
