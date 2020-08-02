from Pusher import Pusher
from ReportGetter import ReportGetter
import os

API_KEY = os.environ['API_KEY']


def job(currencies):
    p = Pusher(API_KEY)
    getter = ReportGetter('US/Eastern')

    p.post_message(f"Current CNY To Forex Rate and Bitcoin Report", getter.build_report(currencies))


if __name__ == '__main__':
    job(["CAD", "USD", "JPY"])
