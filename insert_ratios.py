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

url="https://www.screener.in/company/INFY/consolidated/"

r=requests.get(url)

# Define Variables
m_cursor = mydb.cursor()
soup= BeautifulSoup(r.text,'html.parser')

ratios= soup.find('section', id='ratios')

def get_debator_day_data_web():
    for s_info in ratios.find_all('tbody'):
        rows= s_info.find_all('tr')
        p1=s_info.find_all('td')[1].text
        p2 = s_info.find_all('td')[2].text
        p3 = s_info.find_all('td')[3].text
        p4 = s_info.find_all('td')[4].text
        p5 = s_info.find_all('td')[5].text
        p6 = s_info.find_all('td')[6].text
        p7 = s_info.find_all('td')[7].text
        p8 = s_info.find_all('td')[8].text
        p9 = s_info.find_all('td')[9].text
        p10 = s_info.find_all('td')[10].text
        p11 = s_info.find_all('td')[11].text
        p12 = s_info.find_all('td')[12].text
        print(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)

        add_quaterly="""insert into infy_ratios(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()

def get_Inventor_Days_data_web():
    for s_info in ratios.find_all('tbody'):
        rows= s_info.find_all('tr')
        p1=s_info.find_all('td')[14].text
        p2 = s_info.find_all('td')[15].text
        p3 = s_info.find_all('td')[16].text
        p4 = s_info.find_all('td')[17].text
        p5 = s_info.find_all('td')[18].text
        p6 = s_info.find_all('td')[19].text
        p7 = s_info.find_all('td')[20].text
        p8 = s_info.find_all('td')[21].text
        p9 = s_info.find_all('td')[22].text
        p10 = s_info.find_all('td')[23].text
        p11 = s_info.find_all('td')[24].text
        p12 = s_info.find_all('td')[25].text
        print(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)

        add_quaterly="""insert into infy_ratios(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()

def get_days_payable_data_web():
    for s_info in ratios.find_all('tbody'):
        rows= s_info.find_all('tr')
        p1=s_info.find_all('td')[27].text
        p2 = s_info.find_all('td')[28].text
        p3 = s_info.find_all('td')[29].text
        p4 = s_info.find_all('td')[30].text
        p5 = s_info.find_all('td')[31].text
        p6 = s_info.find_all('td')[32].text
        p7 = s_info.find_all('td')[33].text
        p8 = s_info.find_all('td')[34].text
        p9 = s_info.find_all('td')[35].text
        p10 = s_info.find_all('td')[36].text
        p11 = s_info.find_all('td')[37].text
        p12 = s_info.find_all('td')[38].text
        print(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)

        add_quaterly="""insert into infy_ratios(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()

def get_ccCycle_data_web():
    for s_info in ratios.find_all('tbody'):
        rows= s_info.find_all('tr')
        p1=s_info.find_all('td')[40].text
        p2 = s_info.find_all('td')[41].text
        p3 = s_info.find_all('td')[42].text
        p4 = s_info.find_all('td')[43].text
        p5 = s_info.find_all('td')[44].text
        p6 = s_info.find_all('td')[45].text
        p7 = s_info.find_all('td')[46].text
        p8 = s_info.find_all('td')[47].text
        p9 = s_info.find_all('td')[48].text
        p10 = s_info.find_all('td')[49].text
        p11 = s_info.find_all('td')[50].text
        p12 = s_info.find_all('td')[51].text
        print(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)

        add_quaterly="""insert into infy_ratios(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()
        
def get_Working_Capitald_data_web():
    for s_info in ratios.find_all('tbody'):
        rows= s_info.find_all('tr')
        p1=s_info.find_all('td')[53].text
        p2 = s_info.find_all('td')[54].text
        p3 = s_info.find_all('td')[55].text
        p4 = s_info.find_all('td')[56].text
        p5 = s_info.find_all('td')[57].text
        p6 = s_info.find_all('td')[58].text
        p7 = s_info.find_all('td')[59].text
        p8 = s_info.find_all('td')[60].text
        p9 = s_info.find_all('td')[61].text
        p10 = s_info.find_all('td')[62].text
        p11 = s_info.find_all('td')[63].text
        p12 = s_info.find_all('td')[64].text
        print(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)

        add_quaterly="""insert into infy_ratios(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()

def get_Roce_data_web():
    for s_info in ratios.find_all('tbody'):
        rows= s_info.find_all('tr')
        p1=s_info.find_all('td')[66].text
        p2 = s_info.find_all('td')[67].text
        p3 = s_info.find_all('td')[68].text
        p4 = s_info.find_all('td')[69].text
        p5 = s_info.find_all('td')[70].text
        p6 = s_info.find_all('td')[71].text
        p7 = s_info.find_all('td')[72].text
        p8 = s_info.find_all('td')[73].text
        p9 = s_info.find_all('td')[74].text
        p10 = s_info.find_all('td')[75].text
        p11 = s_info.find_all('td')[76].text
        p12 = s_info.find_all('td')[77].text
        print(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)

        add_quaterly="""insert into infy_ratios(
                        Mar_2010,Mar_2011,Mar_2012,Mar_2013,Mar_2014,Mar_2015,Mar_2016,Mar_2017,Mar_2018,Mar_2019,Mar_2020,Mar_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()

if __name__ == '__main__':
    # get_debator_day_data_web()
    # get_Inventor_Days_data_web()
    # get_days_payable_data_web()
    # get_ccCycle_data_web()
    # get_Working_Capitald_data_web()
    get_Roce_data_web()
