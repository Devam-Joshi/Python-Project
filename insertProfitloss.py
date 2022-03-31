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
    soup= BeautifulSoup(r.text,'html.parser')
    profitloss=soup.find('section', id='profit-loss')

    key= []
    sales=[]
    expenses=[]
    oprofit=[]
    opm=[]
    oincome=[]
    intrest=[]
    Depreciation=[]
    pbt=[]
    tax=[]
    net=[]
    eps=[]
    divinded=[]


    key_length=0
    i=1
    k=1

    for s_info in profitloss.find_all('thead'):
        head=s_info.find_all('th')
        while(k<len(head)):
            key.insert(k,s_info.find_all('th')[k].text)
            k=k+1
    print(key)
    key_length=len(key)
    
    for s_info in profitloss.find_all('tbody'):
        rows= s_info.find_all('tr')
        
        sal=1
        expen=key_length+2
        opr=key_length*2+3
        op=key_length*3+4
        oincm=key_length*4+5
        intr=key_length*5+6
        dep=key_length*6+7
        pb=key_length*7+8
        tx=key_length*8+9
        nt=key_length*9+10
        ep=key_length*10+11
        dp=key_length*11+12

            
        while(i<=key_length):
            sales.insert(sal,s_info.find_all('td')[sal].text)
            expenses.insert(expen,s_info.find_all('td')[expen].text)                
            oprofit.insert(opr,s_info.find_all('td')[opr].text)                
            opm.insert(op,s_info.find_all('td')[op].text)  
            oincome.insert(oincm,s_info.find_all('td')[oincm].text)  
            intrest.insert(intr,s_info.find_all('td')[intr].text)  
            Depreciation.insert(dep,s_info.find_all('td')[dep].text)  
            pbt.insert(pb,s_info.find_all('td')[pb].text)  
            tax.insert(tx,s_info.find_all('td')[tx].text)  
            net.insert(nt,s_info.find_all('td')[nt].text)  
            eps.insert(ep,s_info.find_all('td')[ep].text)  
            divinded.insert(dp,s_info.find_all('td')[dp].text)

            i=i+1
            sal=sal+1
            expen=expen+1
            opr=opr+1
            op=op+1
            oincm=oincm+1
            intr=intr+1
            dep=dep+1
            pb=pb+1
            tx=tx+1
            nt=nt+1
            ep=ep+1
            dp=dp+1

    ins=0
    while(ins<key_length):    
        add_val="insert into {tname}_profit_loss values ('{k}','{r1}','{r2}','{r3}','{r4}','{r5}','{r6}','{r7}','{r8}','{r9}','{r10}','{r11}','{r12}')".format(tname=j, k=key[ins],r1=sales[ins],r2=expenses[ins],r3=oprofit[ins],r4=opm[ins],r5=oincome[ins],r6=intrest[ins],r7=Depreciation[ins],r8=pbt[ins],r9=tax[ins],r10=net[ins],r11=eps[ins],r12=divinded[ins])
        ins=ins+1
        print(add_val)
        # m_cursor.execute(add_val)
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