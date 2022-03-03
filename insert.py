import pickle
import requests
from bs4 import BeautifulSoup
import mysql
import mysql.connector as mysqlconnector
from nsetools import nse
# Connection Of Database

mydb = mysqlconnector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="",
    database="stockmarket")

stock_list = ["abbotindia","adanient"]

url =["https://www.screener.in/company/ABBOTINDIA/",
    "https://www.screener.in/company/ADANIENT/consolidated/"]


# Define Variables
m_cursor = mydb.cursor()


def insert_ratios(r,j):
    key= []
    
    soup= BeautifulSoup(r.text,'html.parser')
    ratios= soup.find('section', id='ratios')

    debator_days_10= []
    debator_days_11=[]
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
        for k in key:
            add_year="""insert into """+j+"""_ratios (year) values (%s)"""
            m_cursor.execute(add_year,(k,))
            print(add_year,k)           
        for stock_list in ratios.find_all('tbody'):
            row=ratios.find_all('tr')
            while(i<=6):
                debator_days_10.insert(i,stock_list.find_all('td')[d].text)
                debator_days_11.insert(i,stock_list.find_all('td')[r2].text)
                i=i+1
                d=d+key_length+1
                r2=r2+key_length+1
                # print(debator_days_10)
                # print(debator_days_11)
            add_quaterly="""update """+j+"""_ratios set Debator_days=%s , Inventory_days=%s , Days_payable =%s, Cash_conversion_cycle=%s , Working_capital_days=%s, ROCE=%s where year=2010"""
            print(add_quaterly,debator_days_10)
            m_cursor.execute(add_quaterly,debator_days_10)
            add_quaterly1="""update """+j+"""_ratios set Debator_days=%s , Inventory_days=%s , Days_payable =%s, Cash_conversion_cycle=%s , Working_capital_days=%s, ROCE=%s where year=2011"""
            print(add_quaterly,debator_days_11)
            m_cursor.execute(add_quaterly1,debator_days_11)
            mydb.commit()
    get_debator_day_data_web()
if __name__ == '__main__':
    
    c=0
    while(c<len(stock_list)):
        r=requests.get(url[c])
        print(url[c])
        print(r)
        insert_ratios(r,stock_list[c])
        c=c+1   
   
