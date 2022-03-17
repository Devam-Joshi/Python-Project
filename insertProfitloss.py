import time
from datetime import datetime
from turtle import pos
import requests
from bs4 import BeautifulSoup
import mysql.connector as mysqlconnector
from nsetools import nse

stock_list = ["ACC","ADANIENT","ADANIGREEN","ADANIPORTS","ADANITRANS","ALKEM","AMBUJACEM","APOLLOHOSP","AUROPHARMA","DMART","BAJAJHLDNG","BERGEPAINT","BIOCON","BOSCHLTD","CIPLA","COLPAL","DLF","DABUR","GAIL","GLAND","HDFCAMC","HAVELLS","HINDPETRO","ICICIGI","ICICIPRULI","IGL","INDUSTOWER","NAUKRI","INDIGO","JINDALSTEL","JUBLFOOD","LTI","LUPIN","MARICO","MUTHOOTFIN","NMDC","PIIND","PIDILITIND","PEL","PGHH","SIEMENS","SAIL","TORNTPHARM","VEDL"]

base_url="https://www.screener.in/company/"
postf="/consolidated/"

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
    sales=[]
    expense= []
    oprofit= []
    opm= []
    oincome= []
    intrest= []
    deprication= []
    pbt= []
    tax= []
    nprofit= []
    eps= []
    payout= []

    soup= BeautifulSoup(r.text,'html.parser')
    profitloss=soup.find('section', id='profit-loss')

    key_length=0
    i=1
    k=1

    for stock_list in profitloss.find_all('thead'):
        head=profitloss.find_all('th')
        while(k < len(head)):
            key.insert(k,stock_list.find_all('th')[k].text)
            k=k+1  
            print(key)
        key_length=len(key)
        print(key_length)
    
    for s_info in profitloss.find_all('tbody'):
        rows= s_info.find_all('tr')
        
        cc1=1
        cc2=key_length+2
        cc3=key_length*2+3
        cc4=key_length*3+4
        cc5=key_length*4+5
        cc6=key_length*5+6
        cc7=key_length*6+7
        cc8=key_length*7+8
        cc9=key_length*9+10
        cc10=key_length*10+11
        cc11=key_length*11+12
        cc12=key_length*12+12
         
        while(i<=key_length):
            sales.insert(cc1,s_info.find_all('td')[cc1].text)
            expense.insert(cc2,s_info.find_all('td')[cc2].text)                
            oprofit.insert(cc3,s_info.find_all('td')[cc3].text)                
            opm.insert(cc4,s_info.find_all('td')[cc4].text)  
            oincome.insert(cc5,s_info.find_all('td')[cc5].text)  
            intrest.insert(cc6,s_info.find_all('td')[cc6].text)  
            deprication.insert(cc7,s_info.find_all('td')[cc7].text)  
            pbt.insert(cc8,s_info.find_all('td')[cc8].text)  
            tax.insert(cc9,s_info.find_all('td')[cc9].text)  
            nprofit.insert(cc10,s_info.find_all('td')[cc10].text)
            eps.insert(cc11,s_info.find_all('td')[cc11].text)
            payout.insert(cc12,s_info.find_all('td')[cc12].text)

            i=i+1
            cc1=cc1+1
            cc2=cc2+1
            cc3=cc3+1
            cc4=cc4+1
            cc5=cc5+1
            cc6=cc6+1
            cc7=cc7+1
            cc8=cc8+1
            cc9=cc9+1
            cc10=cc10+1
            cc11=cc11+1
            cc12=cc12+1
    
    ins=0
    while(ins<key_length):    
        add_val="insert into {tname}_profit_loss values ('{k}','{r1}','{r2}','{r3}','{r4}','{r5}','{r6}','{r7}','{r8}','{r9}','{r10}','{r11}','{r12}')".format(tname=j, k=key[ins],r1=sales[ins],r2=expense[ins],r3=oprofit[ins],r4=opm[ins],r5=oincome[ins],r6=intrest[ins],r7=deprication[ins],r8=pbt[ins],r9=tax[ins],r10=nprofit[ins],r11=eps[ins],r12=payout[ins])
        ins=ins+1
        print(add_val)
        # m_cursor.execute(add_val)
        mydb.commit()  
     
if __name__ == '__main__':
    
    i=0
    while(i<len(stock_list)):
        url=base_url+stock_list[i]+postf
        # time.sleep(4)
        r=requests.get(url)
        print(url)
        print(r)
        insert_main(r,stock_list[i])
        i=i+1