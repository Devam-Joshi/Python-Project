import requests
from bs4 import BeautifulSoup
import mysql.connector as mysqlconnector
from nsetools import nse



stock_list =["GODREJPROP","GRASIM","HDFCAMC","HDFCBANK","HDFCLIFE","HAVELLS","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","ICICIBANK","ICICIGI","ICICIPRULI","ITC","IOC","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","JSWSTEEL","JUBLFOOD","KOTAKBANK","LTI","LT","LUPIN","MRF","MM","MARICO","MARUTI","MUTHOOTFIN","NMDC","NTPC"]


url =["https://www.screener.in/company/GODREJPROP/consolidated/",
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
        "https://www.screener.in/company/NTPC/consolidated/"]

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