# coding: utf-8

from datetime import datetime, timedelta
from requests import get
import json
import matplotlib.pyplot as plt
import pytz
from io import BytesIO
import base64


cur_target_url = "http://vip.stock.finance.sina.com.cn/forex/api/openapi.php/ForexService.getBankForex"
# Historical Data in USD
# params: start, end; value format: 2020-8-1
bitcoin_historical_url = "https://api.coindesk.com/v1/bpi/historical/close.json"
bitcoin_curr_url = "https://api.coindesk.com/v1/bpi/currentprice.json"

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


def get_pre_date(time_zone, days_to_minus):
    now = datetime.now(time_zone)
    return (now - timedelta(days=days_to_minus)).strftime('%Y-%m-%d')


class ReportGetter:
    
    def __init__(self, default_time_zone):
        self.default_time_zone = pytz.timezone(default_time_zone)
        self.cur_data = json.loads(get(cur_target_url).content)['result']['data']['bank']

        self.bitcoin_his_data = json.loads(get(bitcoin_historical_url, params={
            "start": get_pre_date(self.default_time_zone, 7),
            "end": get_pre_date(self.default_time_zone, 0)
        }).content)['bpi']
        self.bitcoin_cur_data = json.loads(get(bitcoin_curr_url).content)['bpi']

    def build_sales_report_en(self, types):
        report = "|Curr|工商银行|中国银行|农业银行|交通银行|建设银行|招商银行|光大银行|浦发银行|兴业银行|中信银行|\n"
        report += "|:----: |:----: |:----: | :----: |:----: | :----: |:----: |:----: |:----: |:----: |:----: |\n"

        for curr_type in types:
            report += f"|*{curr_type}*"

            for item in self.cur_data.get(curr_type):
                # Keep two decimal
                report += "|" + "{:.2f}".format(float(item['xh_sell_price']))
                # report += f"|{item['xh_sell_price']}"
            report += "|\n"

        return report

    def build_sales_report_cn(self, types):
        report = "|币种|工商银行|中国银行|农业银行|交通银行|建设银行|招商银行|光大银行|浦发银行|兴业银行|中信银行|\n"
        report += "|--- |---    |---    |---    |---     | ---   | ---   |---    | ---   | ---   | ---   |\n"

        for curr_type in types:
            report += f"|*{curr_type_dict[curr_type] if curr_type_dict[curr_type] else curr_type}*"

            for item in self.cur_data.get(curr_type):
                # Keep two decimal
                report += "|" + "{:.2f}".format(float(item['xh_sell_price']))
            report += "|\n"

        return report

    def build_bitcoin_report_cn(self):
        dates = []
        prices = []
        # Add historical prices to the plot
        for attribute, value in self.bitcoin_his_data.items():
            dates.append(attribute[5:])
            prices.append(value)
        # Append the latest price to the end of the plot
        curr_price = self.bitcoin_cur_data['USD']['rate_float']
        dates.append(get_pre_date(pytz.timezone('US/Eastern'), 0)[5:])
        prices.append(curr_price)
        plt.plot(dates, prices, 'b--', label='USD')
        plt.plot(dates, prices, 'b^-')
        plt.title('Bitcoin/USD')
        plt.xlabel('date')
        plt.ylabel('USD')
        for (x, y) in zip(dates, prices):
            plt.annotate(y, xy=(x, y), textcoords='data')
        plt.legend()
        plt.grid()

        save_file = BytesIO()
        plt.savefig(save_file, format='png')
        file_base64 = base64.b64encode(save_file.getvalue()).decode('utf8')
        return f"![image](data:image/png;base64,{file_base64})"

    def build_report(self, types):
        curr_part = self.build_sales_report_en(types)
        bitcoin_part = self.build_bitcoin_report_cn()

        curr_time = add_time(pytz.timezone('US/Eastern'))

        return curr_part + "\n" + bitcoin_part + "\n" + curr_time
