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

balance_sheet= soup.find('section', id='balance-sheet')

def get_sc_data_web(sname):
    stk_data =[]
    for s_info in balance_sheet.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=1
        while(i<=13):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_balance_sheet(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_Reserves_data_web(sname):
    stk_data =[]
    for s_info in balance_sheet.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=15
        while(i<=27):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)
        

        add_quaterly="""insert into """+sname+"""_balance_sheet(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_borrowings_data_web(sname):
    stk_data =[]
    for s_info in balance_sheet.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=29
        while(i<=41):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_balance_sheet(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()
    
def get_oliablities_data_web(sname):
    stk_data =[]
    for s_info in balance_sheet.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=43
        while(i<=55):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_balance_sheet(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_tliablities_data_web(sname):
    stk_data =[]
    for s_info in balance_sheet.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=57
        while(i<=69):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)
        
        add_quaterly="""insert into """+sname+"""_balance_sheet(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_fassests_data_web(sname):
    stk_data =[]
    for s_info in balance_sheet.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=71
        while(i<=83):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_balance_sheet(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_cwip_data_web(sname):
    stk_data =[]
    for s_info in balance_sheet.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=85
        while(i<=97):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_balance_sheet(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_investments_data_web(sname):
    stk_data =[]
    for s_info in balance_sheet.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=99
        while(i<=111):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)
        
        add_quaterly="""insert into """+sname+"""_balance_sheet(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_oassests_data_web(sname):
    stk_data =[]
    for s_info in balance_sheet.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=113
        while(i<=125):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)
        
        add_quaterly="""insert into """+sname+"""_balance_sheet(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

def get_tassests_data_web(sname):
    stk_data =[]
    for s_info in balance_sheet.find_all('tbody'):
        rows= s_info.find_all('tr')
        i=127
        while(i<=139):
            stk_data.insert(i,s_info.find_all('td')[i].text)
            i=i+1
            print(stk_data)

        add_quaterly="""insert into """+sname+"""_balance_sheet(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        print(add_quaterly,stk_data)
        m_cursor.execute(add_quaterly,stk_data)
        mydb.commit()

if __name__ == '__main__':
    get_sc_data_web("adanient")
    get_Reserves_data_web("adanient")
    get_borrowings_data_web("adanient")
    get_oliablities_data_web("adanient")
    get_tliablities_data_web("adanient")
    get_fassests_data_web("adanient")
    get_cwip_data_web("adanient")
    get_investments_data_web("adanient")
    get_oassests_data_web("adanient")
    get_tassests_data_web("adanient")
