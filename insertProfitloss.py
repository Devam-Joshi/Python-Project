import time
from datetime import datetime
from turtle import pos
import requests
from bs4 import BeautifulSoup
import mysql.connector as mysqlconnector
from nsetools import nse

stock_list = ["ACC"]

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

    key_length=0
    i=1
    k=1

    for ploss in profitloss.find_all('table',class_='data-table responsive-text-nowrap'):
        head=profitloss.find('tr')
        # print(len(head))
        print(head)
        while(k<=12):
            key.insert(k,ploss.find_all('th')[k].text)
            k=k+1
    key_length=len(key)
    print(key_length)
    print(key)


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