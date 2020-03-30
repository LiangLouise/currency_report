from Pusher import Pusher
from ReportGetter import ReportGetter
from datetime import datetime
import os

API_KEY = os.environ['API_KEY']


def job(currencies):
    p = Pusher(API_KEY)
    getter = ReportGetter()

    p.post_message(f"Current CNY To Forex Rate Report", getter.build_sales_report_en(currencies))


def test(currencies):
    getter = ReportGetter()
    print(getter.build_sales_report_en(currencies))
    print(getter.build_sales_report_cn(currencies))


if __name__ == '__main__':
    job(["CAD", "USD", "JPY"])
