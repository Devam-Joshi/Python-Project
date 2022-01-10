import requests
from bs4 import BeautifulSoup
import mysql.connector as mysqlconnector
from nsetools import nse
# Connection Of Database

mydb = mysqlconnector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="",
    database="stock_market")

url="https://www.screener.in/company/ADANIGREEN/consolidated/"

r=requests.get(url)

# Define Variables
m_cursor = mydb.cursor()
soup= BeautifulSoup(r.text,'html.parser')

quat_table= soup.find('table',class_='data-table responsive-text-nowrap')

# print(quat_table)
# Retrive data from website
def get_Sales_data_web(sname):
    stk_data =[]
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=1
        while(i<=12):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_expenses_data_web(sname):
    stk_data =[]
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=14
        while(i<=25):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)
        add_quaterly="""insert into """+sname+"""_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_oprofit_data_web(sname):
    stk_data =[]
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=27
        while(i<=38):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_opm_data_web(sname):
    stk_data =[]
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=40
        while(i<=51):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)
        
        add_quaterly="""insert into """+sname+"""_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_oincome_data_web(sname):
    stk_data =[]
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=53
        while(i<=64):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)
    
        add_quaterly="""insert into infy_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_intrest_data_web(sname):
    stk_data =[]
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=66
        while(i<=77):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)
        add_quaterly="""insert into infy_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_depreciation_data_web(sname):
    stk_data =[]
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=79
        while(i<=90):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)
        add_quaterly="""insert into """+sname+"""_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()
    
def get_pbt_data_web(sname):
    stk_data =[]
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=92
        while(i<=103):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_tax_data_web(sname):
    stk_data =[]
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=105
        while(i<=116):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)
        add_quaterly="""insert into """+sname+"""_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_netprofit_data_web(sname):
    stk_data =[]
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=118
        while(i<=129):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)
        add_quaterly="""insert into """+sname+"""_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_eps_data_web(sname):
    stk_data =[]
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=131
        while(i<=142):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

if __name__ == '__main__':
    get_Sales_data_web("adanigreen")
    get_expenses_data_web("adanigreen")
    get_oprofit_data_web("adanigreen")
    get_opm_data_web("adanigreen")
    get_oincome_data_web("adanigreen")
    get_intrest_data_web("adanigreen")
    get_depreciation_data_web("adanigreen")
    get_pbt_data_web("adanigreen")
    get_tax_data_web("adanigreen")
    get_netprofit_data_web("adanigreen")
    get_eps_data_web("adanigreen")
