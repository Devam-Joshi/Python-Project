import requests
from bs4 import BeautifulSoup
import mysql.connector as mysqlconnector
from nsetools import nse
import aiohttp
import asyncio

stock_list = ["ABBOTINDIA","ADANIENT","ADANIGREEN","ADANIPORTS","ADANITRANS","ALKEM","AMBUJACEM","APOLLOHOSP","ASIANPAINT","AUROPHARMA","DMART","AXISBANK","BAJAJAUTO","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BANDHANBNK","BERGEPAINT","BPCL","BHARTIARTL","BIOCON","BOSCHLTD","BRITANNIA","CADILAHC","CIPLA","COALINDIA","COLPAL","DLF","DABUR","DIVISLAB","DRREDDY","EICHERMOT","GAIL"]

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
        "https://www.screener.in/company/GAIL/consolidated/"]
# Database Connection

mydb = mysqlconnector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="",
    database="stockmarket")

m_cursor = mydb.cursor()


def insert_main(r,j):
        soup= BeautifulSoup(r.text,'html.parser')
        # print(soup)
        quat_table= soup.find('div',class_='responsive-holder fill-card-width')    
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
    
    i=0
    while(i<len(stock_list)):
        r=requests.get(url[i])
        print(url[i])
        print(r)
        insert_main(r,stock_list[i])
        i=i+1   