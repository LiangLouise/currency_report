# Currency Report
A Python program to read live currency converate rate and bitcoin rate, then push it to [Wechat](https://www.wechat.com/en/) 
via [Server Chan](http://sc.ftqq.com/3.version)

The report is in MD format.

# Sample Response (In Markdown Format)

|Curr|工商银行|中国银行|农业银行|交通银行|建设银行|招商银行|光大银行|浦发银行|兴业银行|中信银行|
|:----: |:----: |:----: | :----: |:----: | :----: |:----: |:----: |:----: |:----: |:----: |
|*CAD*|522.80|521.99|522.02|523.65|522.17|522.58|522.03|521.78|522.26|523.93|
|*USD*|699.05|698.94|698.90|699.19|698.98|700.02|699.19|698.92|699.12|700.70|
|*JPY*|6.62|6.61|6.61|6.62|6.62|6.62|6.61|6.61|6.62|6.63|

![image](/demo/demo.png)

`Data as of 2020-08-02 18:10:48 EDT-0400` 

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

# Data Source

* [Bitcoin](https://www.coindesk.com/coindesk-api)