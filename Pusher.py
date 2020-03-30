from requests import post


class Pusher:

    def __init__(self, key):
        self.api = f"https://sc.ftqq.com/{key}.send"
        self.push_bear_api = f"https://pushbear.ftqq.com/sub?sendkey={key}"

    def post_message(self, title, desp):
        body = {'text': title, 'desp': desp}
        print(f"Sending Report:{title}...")
        response = post(self.api, data=body)
        print(f"Request Status: {response.status_code}")

    def post_via_push_bear(self, title, desp):
        body = {'text': title, 'desp': desp}
        print(f"Sending Report:{title}...")
        response = post(self.push_bear_api, data=body)
        print(f"Request Status: {response.status_code}")
