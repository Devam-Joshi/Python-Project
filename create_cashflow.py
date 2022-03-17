# Import Block
from msvcrt import kbhit
import requests
from bs4 import BeautifulSoup
import mysql.connector as mysqlconnector
from nsetools import nse


# Define Stock List

stock_list = ["ACC","ADANIENT","ADANIGREEN","ADANIPORTS","ADANITRANS","ALKEM","AMBUJACEM","APOLLOHOSP","AUROPHARMA","DMART","BAJAJHLDNG","BANDHANBNK","BERGEPAINT","BIOCON","BOSCHLTD","CADILAHC","CIPLA","CHOLAFIN","COLPAL","DLF","DABUR","GAIL","GLAND","HDFCAMC","HAVELLS","HINDPETRO","ICICIGI","ICICIPRULI","IGL","INDUSTOWER","NAUKRI","INDIGO","JINDALSTEL","JUBLFOOD","LTI","LUPIN","MARICO","MUTHOOTFIN","NMDC","PIIND","PIDILITIND","PEL","PGHH","PNB","SBICARD","SIEMENS","SAIL","TORNTPHARM","MCDOWELLN","VEDL","YESBANK"]


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
        q=("""create table """ + j + """_cash_flows""" +  """ (
                Year VARCHAR(20),
                coa VARCHAR(20),
                cia VARCHAR(20),
                cfa VARCHAR(20),
                ncf VARCHAR(20))""" )
        print(q)     
        m_cursor.execute(q)
        mydb.commit()
    create_table()

# Main Function

if __name__ == '__main__':

    for j in stock_list:
        main_create_table(j) # Call Function