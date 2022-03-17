import time
from datetime import datetime
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
    coa=[]
    cia= []
    cfa= []
    ncf= []

    soup= BeautifulSoup(r.text,'html.parser')
    cashflow=soup.find('section', id='cash-flow')

    key_length=0
    i=1
    k=1

    for stock_list in cashflow.find_all('thead'):
        head=cashflow.find_all('th')
        while(k <len(head)):
            key.insert(k,stock_list.find_all('th')[k].text)
            k=k+1  
        key_length=len(key)
        print(key_length)
    
    for s_info in cashflow.find_all('tbody'):
        rows= s_info.find_all('tr')
        
        cc1=1
        cc2=key_length+2
        cc3=key_length*2+3
        cc4=key_length*3+4
         
        while(i<=key_length):
            coa.insert(cc1,s_info.find_all('td')[cc1].text)
            cia.insert(cc2,s_info.find_all('td')[cc2].text)                
            cfa.insert(cc3,s_info.find_all('td')[cc3].text)                
            ncf.insert(cc4,s_info.find_all('td')[cc4].text)  
        
            i=i+1
            cc1=cc1+1
            cc2=cc2+1
            cc3=cc3+1
            cc4=cc4+1
    
    ins=0
    while(ins<key_length):    
        add_val="insert into {tname}_cash_flows values ('{k}','{r1}','{r2}','{r3}','{r4}')".format(tname=j, k=key[ins],r1=coa[ins],r2=cia[ins],r3=cfa[ins],r4=ncf[ins])
        ins=ins+1
        print(add_val)
        m_cursor.execute(add_val)
        mydb.commit()  
     
if __name__ == '__main__':
    
    i=0
    while(i<len(stock_list)):
        url=base_url+stock_list[i]+postf
        time.sleep(4)
        r=requests.get(url)
        print(url)
        print(r)
        insert_main(r,stock_list[i])
        i=i+1