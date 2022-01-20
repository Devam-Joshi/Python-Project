# Import Block
import requests
from bs4 import BeautifulSoup
import mysql.connector as mysqlconnector
from nsetools import nse

stock_list = ["ABBOTINDIA","ADANIENT","ADANIGREEN","ADANIPORTS","ADANITRANS","ALKEM","AMBUJACEM","APOLLOHOSP","ASIANPAINT","AUROPHARMA","DMART","AXISBANK","BAJAJ-AUTO","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BANDHANBNK","BERGEPAINT","BPCL","BHARTIARTL","BIOCON","BOSCHLTD","BRITANNIA","CADILAHC","CIPLA","COALINDIA","COLPAL","DLF","DABUR","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GLAND","GODREJPROP","GRASIM","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HAVELLS","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","HDFC","ICICIBANK","ICICIGI","ICICIPRULI","ITC","IOC","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INDIGO","JSWSTEEL","JUBLFOOD","KOTAKBANK","LTI","LT","LUPIN","MRF","M&M","MARICO","MARUTI","MUTHOOTFIN","NMDC","NTPC","NESTLEIND","ONGC","PETRONET","PIDILITIND","PEL","POWERGRID","PGHH","PNB","RELIANCE","SBICARD","SBILIFE","SHREECEM","SIEMENS","SBIN","SUNPHARMA","TCS","TATACONSUM","TATAMOTORS","TATASTEEL","TECHM","TITAN","TORNTPHARM","UPL","ULTRACEMCO","UBL","MCDOWELL-N","VEDL","WIPRO","YESBANK"]



url = ["https://www.screener.in/company/ABBOTINDIA/","https://www.screener.in/company/ADANIENT/consolidated/"]

for k in url:
    r=requests.get(k)

# Define Variables
soup= BeautifulSoup(r.text,'html.parser')

quat_table= soup.find('table',class_='data-table responsive-text-nowrap')

# Database Connection

mydb = mysqlconnector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="",
    database="stockmarket")

m_cursor = mydb.cursor()
# Create Table For Quaterly Result

def main_create_table(i):
    
    def create_table():
        q=("""create table """ + i + """_quaterlyresult""" +  """ (
                field_name VARCHAR(20),
                Dec_2018 VARCHAR(20),
                Mar_2019 VARCHAR(20),
                Jun_2019 VARCHAR(20),
                Sep_2019 VARCHAR(20),
                Dec_2019 VARCHAR(20),
                Mar_2020 VARCHAR(20),
                Jun_2020 VARCHAR(20),
                Sep_2020 VARCHAR(20),
                Dec_2020 VARCHAR(20),
                Mar_2021 VARCHAR(20),
                Jun_2021 VARCHAR(20),
                Sep_2021 VARCHAR(20) ) """ )
        print(q)     
        m_cursor.execute(q)
        mydb.commit()

    def get_Sales_data_web():
        stk_data =[]
        for s_info in quat_table.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=1
            while(i<=12):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)

            add_quaterly="""insert into """+j+"""_quaterlyresult(
                        field_name,Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                        values("sales",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            print(add_quaterly,stk_data)
            m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()
    
    def get_expenses_data_web():
        stk_data =[]
        for s_info in quat_table.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=14
            while(i<=25):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)
            add_quaterly="""insert into """+j+"""_quaterlyresult(
                        field_name,Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                        values("expense",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            print(add_quaterly,stk_data)
            m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()

    def get_oprofit_data_web():
        stk_data =[]
        for s_info in quat_table.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=27
            while(i<=38):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)

            add_quaterly="""insert into """+j+"""_quaterlyresult(
                        field_name,Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                        values("Operating Profit ",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            print(add_quaterly,stk_data)
            m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()

    def get_opm_data_web():
        stk_data =[]
        for s_info in quat_table.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=40
            while(i<=51):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)
            
            add_quaterly="""insert into """+j+"""_quaterlyresult(
                        field_name,Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                        values("OPM",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            print(add_quaterly,stk_data)
            m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()

    def get_oincome_data_web():
        stk_data =[]
        for s_info in quat_table.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=53
            while(i<=64):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)
        
            add_quaterly="""insert into """+j+"""_quaterlyresult(
                        field_name,Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                        values("Other Income",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            print(add_quaterly,stk_data)
            m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()

    def get_intrest_data_web():
        stk_data =[]
        for s_info in quat_table.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=66
            while(i<=77):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)
            add_quaterly="""insert into """+j+"""_quaterlyresult(
                        field_name,Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                        values("Intrest",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            print(add_quaterly,stk_data)
            m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()

    def get_depreciation_data_web():
        stk_data =[]
        for s_info in quat_table.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=79
            while(i<=90):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)
            add_quaterly="""insert into """+j+"""_quaterlyresult(
                        field_name,Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                        values("deprecation",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            print(add_quaterly,stk_data)
            m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()
        
    def get_pbt_data_web():
        stk_data =[]
        for s_info in quat_table.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=92
            while(i<=103):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)

            add_quaterly="""insert into """+j+"""_quaterlyresult(
                        field_name,Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                        values("Profit before text",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            print(add_quaterly,stk_data)
            m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()

    def get_tax_data_web():
        stk_data =[]
        for s_info in quat_table.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=105
            while(i<=116):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)
            add_quaterly="""insert into """+j+"""_quaterlyresult(
                        field_name,Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                        values("tax",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            print(add_quaterly,stk_data)
            m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()

    def get_netprofit_data_web():
        stk_data =[]
        for s_info in quat_table.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=118
            while(i<=129):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)
            add_quaterly="""insert into """+j+"""_quaterlyresult(
                        field_name,Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                        values("Net profit",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            print(add_quaterly,stk_data)
            m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()

    def get_eps_data_web():
        stk_data =[]
        for s_info in quat_table.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=131
            while(i<=142):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)

            add_quaterly="""insert into """+j+"""_quaterlyresult(
                        field_name,Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                        values("eps",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            print(add_quaterly,stk_data)
            m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()
    
    create_table()
    get_Sales_data_web()
    get_expenses_data_web()
    get_oprofit_data_web()
    get_opm_data_web()
    get_oincome_data_web()
    get_intrest_data_web()
    get_depreciation_data_web()
    get_pbt_data_web()
    get_tax_data_web()
    get_netprofit_data_web()
    get_eps_data_web()  
    
if __name__ == '__main__':
    
    for j in  stock_list:
        main_create_table(j)





    
