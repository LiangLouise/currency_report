from requests import post


class Pusher:
    def __init__(self, key):
        self.api = f"https://sc.ftqq.com/{key}.send"

    def post_message(self, title, desp):
        body = {'text': title, 'desp': desp}
        print(f"Sending Report:{title}...")
        response = post(self.api, data=body)
        print(f"Request Status: {response.status_code}")
