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

cash_flow= soup.find('section', id='cash-flow')

def get_cCoperatingActivity_data_web(sname):
    stk_data =[]
    for s_info in cash_flow.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=1
        while(i<=12):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)
        add_quaterly="""insert into """+sname+"""_cash_flows(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_cInvestingActivity_data_web(sname):
    stk_data =[]
    for s_info in cash_flow.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=14
        while(i<=25):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)
        
        add_quaterly="""insert into """+sname+"""_cash_flows(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_cFinancingActivity_data_web(sname):
    stk_data =[]
    for s_info in cash_flow.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=27
        while(i<=38):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_cash_flows(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_NetCashFlow_data_web(sname):
    stk_data =[]
    for s_info in cash_flow.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=40
        while(i<=51):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_cash_flows(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()


if __name__ == '__main__':
    get_cCoperatingActivity_data_web("adanient")
    get_cInvestingActivity_data_web("adanient")
    get_cFinancingActivity_data_web("adanient")
    get_NetCashFlow_data_web("adanient")
