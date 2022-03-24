# Import Block

import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import mysql.connector as mysqlconnector
from nsetools import nse

# Define Stock List

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


# Main Insertion Function

def insert_main(r,j):

    # Define List For Store The Scrap Data

    key= []
    debtor_days=[]
    inventory_days=[]
    days_payable=[]
    cash_conversion_cycle=[]
    working_capital_days=[]
    roc=[]

    # Finding Section Using Web Scrap

    soup= BeautifulSoup(r.text,'html.parser')
    ratios= soup.find('section', id='ratios')

    key_length=0
    i=1
    k=1

    # This Loop For Finding the head of particular section means its found year

    for stock_list in ratios.find_all('thead'):
        head=ratios.find_all('th')
        print(head)
        while(k < len(head)):
            key.insert(k,stock_list.find_all('th')[k].text)
            k=k+1  
            print(key)
        key_length=len(key)
        # print(key_length)
    
    # This Loop For Findind Data Of Section 

    for s_info in ratios.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=1
        id=key_length+2
        dp=key_length*2+3
        cc=key_length*3+4
        wd=key_length*4+5
        ro=key_length*5+6
        
        # its run when length of key is less than I

        while(i<=key_length):
            debtor_days.insert(i,s_info.find_all('td')[i].text)
            inventory_days.insert(id,s_info.find_all('td')[id].text)                
            days_payable.insert(dp,s_info.find_all('td')[dp].text)                
            cash_conversion_cycle.insert(cc,s_info.find_all('td')[cc].text)  
            working_capital_days.insert(wd,s_info.find_all('td')[wd].text)  
            roc.insert(ro,s_info.find_all('td')[ro].text)  

            dp=dp+1
            id=id+1
            i=i+1
            cc=cc+1
            wd=wd+1
            ro=ro+1
        print(cc)
        print(debtor_days,inventory_days,days_payable,cash_conversion_cycle,working_capital_days,roc)

    ins=0

    # its run when length of key is less than ins

    while(ins<key_length):  
        # add val is stored the query of data insertion in this we use formator for data insert.   
        add_val="insert into {tname}_ratios values ('{k}', '{deb_days}','{inv_days}','{d_pay}','{cash_con}','{wor_cap}','{ro}')".format(tname=j, k=key[ins],deb_days=debtor_days[ins],inv_days=inventory_days[ins],d_pay=days_payable[ins],cash_con=cash_conversion_cycle[ins],wor_cap=working_capital_days[ins],ro=roc[ins])
        ins=ins+1
        print(add_val)
        m_cursor.execute(add_val) # Execute the Query
        mydb.commit()  
     

# Main Function

if __name__ == '__main__':
    
    i=0
    while(i<len(stock_list)):
        url=base_url+stock_list[i]+postf # concate the url with base url
        time.sleep(4) # sleep for 4 second
        r=requests.get(url) # send request to the url
        print(url)
        print(r)
        insert_main(r,stock_list[i]) # call Function
        i=i+1