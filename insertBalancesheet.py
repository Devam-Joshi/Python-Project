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
    user="root",
    password="",
    database="stockmarket")

m_cursor = mydb.cursor()


def insert_main(r,j):
    key= []
    bs1=[]
    bs2=[]
    bs3=[]
    bs4=[]
    bs5=[]
    bs6=[]
    bs7=[]
    bs8=[]
    bs9=[]
    bs10=[]

    soup= BeautifulSoup(r.text,'html.parser')
    balancesheet=soup.find('section', id='balance-sheet')

    key_length=0
    i=1
    k=1

    for stock_list in balancesheet.find_all('thead'):
        head=balancesheet.find_all('th')
        print(head)
        while(k <len(head)):
            key.insert(k,stock_list.find_all('th')[k].text)
            k=k+1  
        key_length=len(key)
        print(key_length)
    
    for s_info in balancesheet.find_all('tbody'):
        rows= s_info.find_all('tr')
        
        b1=1
        b2=key_length+2
        b3=key_length*2+3
        b4=key_length*3+4
        b5=key_length*4+5
        b6=key_length*5+6
        b7=key_length*6+7
        b8=key_length*7+8
        b9=key_length*8+9
        b10=key_length*9+10

            
        while(i<=key_length):
            bs1.insert(b1,s_info.find_all('td')[b1].text)
            bs2.insert(b2,s_info.find_all('td')[b2].text)                
            bs3.insert(b3,s_info.find_all('td')[b3].text)                
            bs4.insert(b4,s_info.find_all('td')[b4].text)  
            bs5.insert(b5,s_info.find_all('td')[b5].text)  
            bs6.insert(b6,s_info.find_all('td')[b6].text)  
            bs7.insert(b7,s_info.find_all('td')[b7].text)  
            bs8.insert(b8,s_info.find_all('td')[b8].text)  
            bs9.insert(b9,s_info.find_all('td')[b9].text)  
            bs10.insert(b10,s_info.find_all('td')[b10].text)  

            i=i+1
            b1=b1+1
            b2=b2+1
            b3=b3+1
            b4=b4+1
            b5=b5+1
            b6=b6+1
            b7=b7+1
            b8=b8+1
            b9=b9+1
            b10=b10+1

    print(bs10)
    ins=0
    while(ins<key_length):    
        add_val="insert into {tname}_balancesheet values ('{k}','{r1}','{r2}','{r3}','{r4}','{r5}','{r6}','{r7}','{r8}','{r9}','{r10}')".format(tname=j, k=key[ins],r1=bs1[ins],r2=bs2[ins],r3=bs3[ins],r4=bs4[ins],r5=bs5[ins],r6=bs6[ins],r7=bs7[ins],r8=bs8[ins],r9=bs9[ins],r10=bs10[ins])
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