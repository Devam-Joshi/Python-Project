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

profit_loss= soup.find('section', id='profit-loss')

def get_sales_data_web(sname):
    stk_data =[]
    for s_info in profit_loss.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=1
        while(i<=6):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_profit_loss(
                        Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,TTM)
                    values(%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_expenses_data_web(sname):
    stk_data =[]
    for s_info in profit_loss.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=8
        while(i<=13):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_profit_loss(
                        Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,TTM)
                    values(%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_oprofit_data_web(sname):
    stk_data =[]
    for s_info in profit_loss.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=15
        while(i<=20):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_profit_loss(
                        Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,TTM)
                    values(%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_opm_data_web(sname):
    stk_data =[]
    for s_info in profit_loss.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=22
        while(i<=27):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_profit_loss(
                        Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,TTM)
                    values(%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_oincome_data_web(sname):
    stk_data =[]
    for s_info in profit_loss.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=29
        while(i<=34):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_profit_loss(
                        Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,TTM)
                    values(%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_intrest_data_web(sname):
    stk_data =[]
    for s_info in profit_loss.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=36
        while(i<=41):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_profit_loss(
                        Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,TTM)
                    values(%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_depreciation_data_web(sname):
    stk_data =[]
    for s_info in profit_loss.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=43
        while(i<=48):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_profit_loss(
                        Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,TTM)
                    values(%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_pbt_data_web(sname):
    stk_data =[]
    for s_info in profit_loss.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=50
        while(i<=55):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_profit_loss(
                        Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,TTM)
                    values(%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_tax_data_web(sname):
    stk_data =[]
    for s_info in profit_loss.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=57
        while(i<=61):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_profit_loss(
                        Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021)
                    values(%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_net_data_web(sname):
    stk_data =[]
    for s_info in profit_loss.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=64
        while(i<=69):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_profit_loss(
                        Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,TTM)
                    values(%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_eps_data_web(sname):
    stk_data =[]
    for s_info in profit_loss.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=71
        while(i<=76):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_profit_loss(
                        Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,TTM)
                    values(%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()


def get_divinded_data_web(sname):
    stk_data =[]
    for s_info in profit_loss.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=79
        while(i<=83):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_profit_loss(
                        Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021)
                    values(%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

if __name__ == "__main__":
    get_sales_data_web("adanigreen")
    get_expenses_data_web("adanigreen")
    get_oprofit_data_web("adanigreen")
    get_opm_data_web("adanigreen")
    get_oprofit_data_web("adanigreen")
    get_intrest_data_web("adanigreen")
    get_depreciation_data_web("adanigreen")
    get_pbt_data_web("adanigreen")
    get_tax_data_web("adanigreen")
    get_net_data_web("adanigreen")
    get_eps_data_web("adanigreen")
    get_divinded_data_web("adanigreen")