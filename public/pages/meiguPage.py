# -*- coding:utf-8 -*-
import time
from public.common import basepage
import re
import urllib
import urllib3
import json

class MeiguPage(basepage.Page):

    def into_httptest_page(self):
        """"打开test页面"""
        self.dr.open("http://172.16.57.34:8888/?t=696d29e0940a4957748fe3fc9efd22a3")


    def click_meigu_pankou_button(self):
        self.dr.move_to_element('link_text->实时服务')
        time.sleep(3)

        self.dr.move_to_element('link_text->盘口')
        time.sleep(3)
        self.dr.click('link_text->美股')
        content = "server=183.136.163.57:1818 ;requestId=17176 ;emcode=AAPL.O"
        self.dr.clear_type('id->param', content)
        self.dr.click('link_text->提交')
        time.sleep(3)
        #获取美股的盘口数据
        message = self.dr.get_element('id->valueLabel').text
        self.dr.my_print("{0} meigu pankou shuju ".format(message))
        msg = re.findall(r'\{([^{}]+)\}', message)
        text1 = msg[0]
        self.dr.my_print("{0} ".format(text1))
        list = []
        list.append(text1.split(','))
        list2 = list[0]
        #print list[0]
        text2 = list2[27]
       # print text2
        list3 = []
        list3.append(text2.split('='))
       # print list3
        list4 = list3[0]
        price = list4[1]
        str_price = str(price)
        self.dr.my_print("{0} meigu latest price ".format(str_price))
        # print u"test页面最新价:" + str(price)
        str_price = str(price)
        return str_price

    def read_latest_price_from_http(self):
        """"读取http返回的股票代码和最新价"""
        url = "http://183.136.163.9/quote/ussIndex?code=AAPL.O&index=8042"
        url_request = urllib.request.urlopen(url)
        buffer = url_request.read()
        print(buffer)
        stockData = json.loads(buffer)
        print(stockData.keys())
        list = stockData["result"]["list"]
        print(list)
        stockMsg = list[0]
        stockCode = stockMsg["code"]
        print(stockCode)
        stockPrice = stockMsg["value"][0]
        print("stockPrice" + str(stockPrice))
        # if stockCode == "Null" or stockPrice == "Null":
        #     print "Error"
        # else:
        #     print "OK"
        str_stockPrice = str(stockPrice)
        self.dr.my_print("http leasted price {0}".format(str_stockPrice))
        return str_stockPrice

    def compare_price(self):
        price1 = self.click_meigu_pankou_button()
        price2 = self.read_latest_price_from_http()
        if price1 == price2:
            self.dr.my_print("===============")
            self.dr.my_print("service test get the price{0} is equal to http {1}latest price ".format(price1, price2))




