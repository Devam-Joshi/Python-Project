from asyncio.windows_events import NULL
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import mysql.connector as mysqlconnector
from nsetools import nse

stock_list = ["ACC","ADANIENT","ADANIGREEN","ADANIPORTS","ADANITRANS","ALKEM","AMBUJACEM","APOLLOHOSP","AUROPHARMA","DMART","BAJAJHLDNG","BANDHANBNK","BERGEPAINT","BIOCON","BOSCHLTD","CADILAHC","CIPLA","CHOLAFIN","COLPAL","DLF","DABUR","GAIL","GLAND","HDFCAMC","HAVELLS","HINDPETRO","ICICIGI","ICICIPRULI","IGL","INDUSTOWER","NAUKRI","INDIGO","JINDALSTEL","JUBLFOOD","LTI","LUPIN","MARICO","MUTHOOTFIN","NMDC","PIIND","PIDILITIND","PEL","PGHH","PNB","SBICARD","SIEMENS","SAIL","TORNTPHARM","MCDOWELLN","VEDL","YESBANK"]

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
    sp1=[]
    sp2=[]
    sp3=[]
    sp4=[]
    sp5=[]

    soup= BeautifulSoup(r.text,'html.parser')
    sholing=soup.find('section', id='shareholding')

    key_length=0
    i=1
    k=1
    
    for stock_list in sholing.find_all('thead'):
        head=sholing.find_all('th')
        print(head)
        print(len(head))
        while(k <len(head)):
            key.insert(k,stock_list.find_all('th')[k].text)
            k=k+1  
        key_length=len(key)
        print(key_length)
    
    for s_info in sholing.find_all('tbody'):
        rows= s_info.find_all('tr')
        
        s1=1
        s2=key_length+2
        s3=key_length*2+3
        s4=key_length*3+4
        s5=key_length*4+5
    
            
        while(i<=key_length):

            sp1.insert(s1,s_info.find_all('td')[s1].text)
            sp2.insert(s2,s_info.find_all('td')[s2].text)                
            sp3.insert(s3,s_info.find_all('td')[s3].text)                
            sp4.insert(s4,s_info.find_all('td')[s4].text)
            if(len(rows)==5):  
                sp5.insert(s5,s_info.find_all('td')[s5].text)  
            else:
                sp5.insert(s5,NULL)

            i=i+1
            s1=s1+1
            s2=s2+1
            s3=s3+1
            s4=s4+1
            s5=s5+1
            
            
    ins=0
    while(ins<key_length):    
        add_val="insert into {tname}_shareholding values ('{k}','{r1}','{r2}','{r3}','{r5}','{r4}')".format(tname=j, k=key[ins],r1=sp1[ins],r2=sp2[ins],r3=sp3[ins],r5=sp5[ins],r4=sp4[ins])
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