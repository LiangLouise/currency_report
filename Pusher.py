from requests import post


class Pusher:
    def __init__(self, key):
        self.api = f"https://sc.ftqq.com/{key}.send"

    def post_message(self, title, desp):
        body = {'text': title, 'desp': desp}
        print(title)
        print(desp)
        response = post(self.api, data=body)
