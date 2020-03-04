# coding: utf-8

from requests import get
import json
from datetime import datetime

target_url = "http://vip.stock.finance.sina.com.cn/forex/api/openapi.php/ForexService.getBankForex"
name_refer_dict = {
    'xc_buy_price': "钞买价",
    'xh_buy_price': "汇买价",
    'xc_sell_price': "钞卖价",
    'xh_sell_price': "汇卖价"
    }


class ReportGetter:
    
    def __init__(self):
        self.data = json.loads(get(target_url).content)['result']['data']['bank']

    def build_sales_report(self, curr_type):
        report = f"# Current {curr_type} Selling Price Report \n"
        report += f"## Data as of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n"
        report += "|工商银行|中国银行|农业银行|交通银行|建设银行|招商银行|光大银行|浦发银行|兴业银行|中信银行|\n"
        report += "|---    |---    |---    |---     | ---   | ---   |---    | ---   | ---   | ---   |\n"

        for item in self.data.get(curr_type):
            report += f"|{item['xh_sell_price']}"
        report += "|\n"
        return report
