import requests
from bs4 import BeautifulSoup
import mysql.connector as mysqlconnector
from nsetools import nse
import aiohttp
import asyncio

stock_list = ["ABBOTINDIA","ADANIENT"]

url =["https://www.screener.in/company/ABBOTINDIA/",
        "https://www.screener.in/company/ADANIENT/consolidated/"]
# Database Connection

mydb = mysqlconnector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="",
    database="stockmarket")

m_cursor = mydb.cursor()


def insert_main(r,j): 
    key= []
    debtor_days=[]
    inventory_days=[]
    days_payable=[]
    cash_conversion_cycle=[]
    working_capital_days=[]
    ROCE=[]
    soup= BeautifulSoup(r.text,'html.parser')
    ratios= soup.find('section', id='ratios')

    key_length=0
    def get_debator_day_data_web():
        i=1
        k=1
        d=1
        r2=2
        insert_year=0 # for index length

        for stock_list in ratios.find_all('thead'):
            head=ratios.find_all('th')
            while(k<=12):
                key.insert(k,stock_list.find_all('th')[k].text)
                k=k+1  
                # print(key)
            key_length=len(key)
            # print(key_length)
        
        print(key)      
        for s_info in ratios.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=1
            id=key_length+2
            dp=key_length*2+3
            cc=key_length*3+4
            wd=key_length*4+5
            ro=key_length*5+6
            
            while(i<=key_length):
                debtor_days.insert(i,s_info.find_all('td')[i].text)
                inventory_days.insert(id,s_info.find_all('td')[id].text)                
                days_payable.insert(dp,s_info.find_all('td')[dp].text)                
                cash_conversion_cycle.insert(cc,s_info.find_all('td')[cc].text)  
                working_capital_days.insert(wd,s_info.find_all('td')[wd].text)  
                ROCE.insert(ro,s_info.find_all('td')[ro].text)  

                dp=dp+1
                id=id+1
                i=i+1
                cc=cc+1
                wd=wd+1
                ro=ro+1
            print(cc)
            print(debtor_days,inventory_days,days_payable,cash_conversion_cycle,working_capital_days,ROCE)
            # m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()
    get_debator_day_data_web()
    
if __name__ == '__main__':
    
    i=0
    while(i<len(stock_list)):
        r=requests.get(url[i])
        print(url[i])
        print(r)
        insert_main(r,stock_list[i])
        i=i+1   