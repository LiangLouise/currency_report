# Currency Report
A Python program to read live currency converate rate and push it to [Wechat](https://www.wechat.com/en/) 
via [Server Chan](http://sc.ftqq.com/3.version)

The report is in MD format.

# Sample Response (In Markdown Format)

|Currency|工商银行|中国银行|农业银行|交通银行|建设银行|招商银行|光大银行|浦发银行|兴业银行|中信银行|
|---     |---    |---    |---    |---     | ---   | ---   |---    | ---   | ---   | ---   |
|CAD     |519.1000|518.6200|519.4700|520.2800|519.1700|519.1500|519.2963|518.8000|521.4700|519.5000|
`Data as of 2020-03-04 15:56:38`

# Configs

## [main.py](./main.py)

`API_KEY`: Your Server Chan API Key to push the message 

`job(currencies)`: Specify a list of which Currency you want to compare with CNY, available choices are:
* AUD
* BRL
* CAD
* CHF
* DKK
* EUR
* GBP
* HKD
* JPY
* KRW
* MOP
* MYR
* NOK
* NZD
* PHP
* RUB
* SEK
* SGD
* THB
* TWD
* USD
* ZAR