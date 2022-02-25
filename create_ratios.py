# Import Block
from msvcrt import kbhit
import requests
from bs4 import BeautifulSoup
import mysql.connector as mysqlconnector
from nsetools import nse

stock_list = ["ABBOTINDIA","ADANIENT","ADANIGREEN","ADANIPORTS","ADANITRANS","ALKEM","AMBUJACEM","APOLLOHOSP","ASIANPAINT","AUROPHARMA","DMART","AXISBANK","BAJAJAUTO","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BANDHANBNK","BERGEPAINT","BPCL","BHARTIARTL","BIOCON","BOSCHLTD","BRITANNIA","CADILAHC","CIPLA","COALINDIA","COLPAL","DLF","DABUR","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GODREJPROP","GRASIM","HDFCAMC","HDFCBANK","HDFCLIFE","HAVELLS","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","ICICIBANK","ICICIGI","ICICIPRULI","ITC","IOC","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","JSWSTEEL","JUBLFOOD","KOTAKBANK","LTI","LT","LUPIN","MRF","MM","MARICO","MARUTI","MUTHOOTFIN","NMDC","NTPC","NESTLEIND","ONGC","PETRONET","PIDILITIND","PEL","POWERGRID","PGHH","PNB","SBILIFE","SHREECEM","SIEMENS","SBIN","SUNPHARMA","TCS","TATACONSUM","TATAMOTORS","TATASTEEL","TECHM","TITAN","TORNTPHARM","UPL","ULTRACEMCO","UBL","MCDOWELLN","VEDL","WIPRO","YESBANK"]

url =["https://www.screener.in/company/ABBOTINDIA/",
        "https://www.screener.in/company/ADANIENT/consolidated/",
        "https://www.screener.in/company/ADANIGREEN/consolidated/",
        "https://www.screener.in/company/ADANIPORTS/consolidated/",
        "https://www.screener.in/company/ADANITRANS/consolidated/",
        "https://www.screener.in/company/ALKEM/consolidated/",
        "https://www.screener.in/company/AMBUJACEM/consolidated/",
        "https://www.screener.in/company/APOLLOHOSP/consolidated/",
        "https://www.screener.in/company/ASIANPAINT/consolidated/",
        "https://www.screener.in/company/AUROPHARMA/consolidated/",
        "https://www.screener.in/company/DMART/consolidated/",
        "https://www.screener.in/company/AXISBANK/consolidated/",
        "https://www.screener.in/company/BAJAJ-AUTO/consolidated/",
        "https://www.screener.in/company/BAJFINANCE/consolidated/",
        "https://www.screener.in/company/BAJAJFINSV/consolidated/",
        "https://www.screener.in/company/BAJAJHLDNG/consolidated/",
        "https://www.screener.in/company/BANDHANBNK/",
        "https://www.screener.in/company/BERGEPAINT/consolidated/",
        "https://www.screener.in/company/BPCL/consolidated/",
        "https://www.screener.in/company/BHARTIARTL/consolidated/",
        "https://www.screener.in/company/BIOCON/consolidated/",
        "https://www.screener.in/company/BOSCHLTD/",
        "https://www.screener.in/company/BRITANNIA/consolidated/",
        "https://www.screener.in/company/CADILAHC/consolidated/",
        "https://www.screener.in/company/CIPLA/consolidated/",
        "https://www.screener.in/company/COALINDIA/consolidated/",
        "https://www.screener.in/company/COLPAL/",
        "https://www.screener.in/company/DLF/consolidated/",
        "https://www.screener.in/company/DABUR/consolidated/",
        "https://www.screener.in/company/DIVISLAB/consolidated/",
        "https://www.screener.in/company/DRREDDY/consolidated/",
        "https://www.screener.in/company/EICHERMOT/consolidated/",
        "https://www.screener.in/company/GAIL/consolidated/",
        "https://www.screener.in/company/GODREJPROP/consolidated/",
        "https://www.screener.in/company/GRASIM/consolidated/",
        "https://www.screener.in/company/HDFCAMC/",
        "https://www.screener.in/company/HDFCBANK/consolidated/",
        "https://www.screener.in/company/HDFCLIFE/",
        "https://www.screener.in/company/HAVELLS/consolidated/",
        "https://www.screener.in/company/HEROMOTOCO/consolidated/",
        "https://www.screener.in/company/HINDALCO/consolidated/",
        "https://www.screener.in/company/HINDPETRO/consolidated/",
        "https://www.screener.in/company/HINDUNILVR/consolidated/",
        "https://www.screener.in/company/ICICIBANK/consolidated/",
        "https://www.screener.in/company/ICICIGI/",
        "https://www.screener.in/company/ICICIPRULI/",
        "https://www.screener.in/company/ITC/consolidated/",
        "https://www.screener.in/company/IOC/consolidated/",
        "https://www.screener.in/company/IGL/consolidated/",
        "https://www.screener.in/company/INDUSTOWER/consolidated/",
        "https://www.screener.in/company/INDUSINDBK/",
        "https://www.screener.in/company/NAUKRI/consolidated/",
        "https://www.screener.in/company/INFY/consolidated/",
        "https://www.screener.in/company/INDIGOPNTS/",
        "https://www.screener.in/company/JSWSTEEL/consolidated/",
        "https://www.screener.in/company/JUBLFOOD/consolidated/",
        "https://www.screener.in/company/KOTAKBANK/consolidated/",
        "https://www.screener.in/company/LTI/",
        "https://www.screener.in/company/LT/consolidated/",
        "https://www.screener.in/company/LUPIN/consolidated/",
        "https://www.screener.in/company/MRF/consolidated/",
        "https://www.screener.in/company/M&M/consolidated/",
        "https://www.screener.in/company/MARICO/consolidated/",
        "https://www.screener.in/company/MARUTI/consolidated/",
        "https://www.screener.in/company/MUTHOOTFIN/",
        "https://www.screener.in/company/NMDC/consolidated/",
        "https://www.screener.in/company/NTPC/consolidated/",
        "https://www.screener.in/company/NESTLEIND/",
        "https://www.screener.in/company/ONGC/consolidated/",
        "https://www.screener.in/company/PETRONET/",
        "https://www.screener.in/company/PIDILITIND/consolidated/",
        "https://www.screener.in/company/PEL/consolidated/",
        "https://www.screener.in/company/POWERGRID/consolidated/",
        "https://www.screener.in/company/PGHH/",
        "https://www.screener.in/company/PNBHOUSING/",
        "https://www.screener.in/company/RELIANCE/consolidated/",
        "https://www.screener.in/company/SBICARD/",
        "https://www.screener.in/company/SBILIFE/",
        "https://www.screener.in/company/SHREECEM/",
        "https://www.screener.in/company/SIEMENS/consolidated/",
        "https://www.screener.in/company/SBIN/consolidated/",
        "https://www.screener.in/company/SUNPHARMA/consolidated/",
        "https://www.screener.in/company/TCS/consolidated/",
        "https://www.screener.in/company/TATACONSUM/consolidated/",
        "https://www.screener.in/company/TATAMOTORS/consolidated/",
        "https://www.screener.in/company/TATASTEEL/consolidated/",
        "https://www.screener.in/company/TECHM/consolidated/",
        "https://www.screener.in/company/TITAN/consolidated/",
        "https://www.screener.in/company/TORNTPHARM/consolidated/",
        "https://www.screener.in/company/UPL/consolidated/",
        "https://www.screener.in/company/ULTRACEMCO/consolidated/",
        "https://www.screener.in/company/UBL/consolidated/",
        "https://www.screener.in/company/MCDHOLDING/",
        "https://www.screener.in/company/VEDL/consolidated/",
        "https://www.screener.in/company/WIPRO/consolidated/",
        "https://www.screener.in/company/YESBANK/"
        ]

# Database Connection

mydb = mysqlconnector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="",
    database="stockmarket")

m_cursor = mydb.cursor()
# Create Table For Quaterly Result
def main_create_table(j):
    def create_table():
        q=("""create table """ + j + """_ratios""" +  """ (
                Year VARCHAR(20),
                Debator_days VARCHAR(20),
                Inventory_days VARCHAR(20),
                Days_payable VARCHAR(20),
                Cash_conversion_cycle VARCHAR(20),
                Working_capital_days VARCHAR(20),
                ROCE VARCHAR(20)) """ )
        print(q)     
        m_cursor.execute(q)
        mydb.commit()
    create_table()

if __name__ == '__main__':

    for j in stock_list:
        main_create_table(j)