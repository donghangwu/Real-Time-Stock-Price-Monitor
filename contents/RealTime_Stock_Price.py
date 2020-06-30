import requests
from bs4 import BeautifulSoup
import pandas
import datetime
import time
class stock_data(object):
    
    def __init__(self,stockList):
        self.stock_list=stockList
        
    @property
    def get_stock_list():
        return self.stock_list

    def real_time_price(self,stock_symbol):
        url = "https://finance.yahoo.com/quote/" + stock_symbol + "?p="+stock_symbol+"&.tsrc=fin-srch"
        re = requests.get(url)
        web_info = BeautifulSoup(re.text,'lxml')
        while(web_info==[]):
             print("wrong!!!")
             re = requests.get(url)
             web_info = BeautifulSoup(re.text,'lxml')
        web_info = web_info.find('div',{"class":'My(6px) Pos(r) smartphone_Mt(6px)'})
        #if did not get any info from the web
        web_info = web_info.find('span').text
        return web_info

    def save_data(self):
        while(True):
            prices=[]
            col=[]
            time_count = datetime.datetime.now()
            time_count = time_count.strftime("%Y-%m-%d %H:%M:%S")
            for each in self.stock_list:
                prices.append(self.real_time_price(each))
            col = [time_count]
            col.extend(prices)
            time.sleep(5)
            #print(col)
            file = pandas.DataFrame(col)
            file = file.T
            file.to_csv('stock_price.csv',mode='a',header=False)

