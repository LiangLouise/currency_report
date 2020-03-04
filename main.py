from Pusher import Pusher
from ReportGetter import ReportGetter
from datetime import datetime

API_KEY = "${API_KEY}"

def job(currency):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    p = Pusher(API_KEY)
    getter = ReportGetter()
    p.post_message(f"Current CNY/{currency} rate at {time}", getter.build_sales_report(currency))


if __name__=='__main__':
    job("CAD")
