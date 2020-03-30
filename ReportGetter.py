# coding: utf-8

from requests import get
import pytz, json
from datetime import datetime

target_url = "http://vip.stock.finance.sina.com.cn/forex/api/openapi.php/ForexService.getBankForex"
name_refer_dict = {
    'xc_buy_price': "钞买价",
    'xh_buy_price': "汇买价",
    'xc_sell_price': "钞卖价",
    'xh_sell_price': "汇卖价"
    }

curr_type_dict = {
    "CAD": "加元",
    "JPY": "日元",
    "USD": "美元",
    "HKD": "港币"
}


def add_time(time_zone):
    return f"`Data as of {datetime.now(time_zone).strftime('%Y-%m-%d %H:%M:%S %Z%z')}` \n"


class ReportGetter:
    
    def __init__(self):
        self.data = json.loads(get(target_url).content)['result']['data']['bank']

    def build_sales_report_en(self, types):
        report = "|Curr|工商银行|中国银行|农业银行|交通银行|建设银行|招商银行|光大银行|浦发银行|兴业银行|中信银行|\n"
        report += "|:----: |:----: |:----: | :----: |:----: | :----: |:----: |:----: |:----: |:----: |:----: |\n"

        for curr_type in types:
            report += f"|*{curr_type}*"

            for item in self.data.get(curr_type):
                # Keep two decimal
                report += "|" + "{:.2f}".format(float(item['xh_sell_price']))
                # report += f"|{item['xh_sell_price']}"
            report += "|\n"

        report += add_time(pytz.timezone('US/Eastern'))

        return report

    def build_sales_report_cn(self, types):
        report = "|币种|工商银行|中国银行|农业银行|交通银行|建设银行|招商银行|光大银行|浦发银行|兴业银行|中信银行|\n"
        report += "|--- |---    |---    |---    |---     | ---   | ---   |---    | ---   | ---   | ---   |\n"

        for curr_type in types:
            report += f"|*{curr_type_dict[curr_type] if curr_type_dict[curr_type] else curr_type}*"

            for item in self.data.get(curr_type):
                # Keep two decimal
                report += "|" + "{:.2f}".format(float(item['xh_sell_price']))
            report += "|\n"

        report += add_time(pytz.timezone('Asia/Shanghai'))

        return report
