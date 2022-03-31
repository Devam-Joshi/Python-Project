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
    detail=[]
    i=0
    soup= BeautifulSoup(r.text,'html.parser')
    basic_detail=soup.find('div', class_="company-ratios")

    for s_info in basic_detail.find_all('ul',id="top-ratios"):
        rows= s_info.find_all('li')
        data=s_info.find_all('span',class_="number")
        # print(data)
        while(i<len(data)):
            detail.insert(i,s_info.find_all('span',class_="number")[i].text)
            i=i+1
        # print(data)
        print(detail)

    len_detail=len(detail)
    ins=0
       
    add_val= """INSERT INTO """ + j + """_company_ratios (market_cap, current_price, high,low, stock_pe,book_value,divinded,roce,roe,face_value) 
                                VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s) """
    ins=ins+1
    print(add_val,detail)
    # m_cursor.execute(add_val,detail)
    mydb.commit()  

if __name__ == '__main__':
    
    i=0
    while(i<len(stock_list)):
        url=base_url+stock_list[i]+postf
        time.sleep(10)
        r=requests.get(url)
        print(url)
        print(r)
        insert_main(r,stock_list[i])
        i=i+1