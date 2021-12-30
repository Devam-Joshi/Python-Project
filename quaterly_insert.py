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

quat_table= soup.find('table',class_='data-table responsive-text-nowrap')

# print(quat_table)
# Retrive data from website
def get_Sales_data_web():
    for s_info in quat_table.find_all('tbody'):
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

        add_quaterly="""insert into infy_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()

def get_expenses_data_web():
    for s_info in quat_table.find_all('tbody'):
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

        add_quaterly="""insert into infy_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()

def get_oprofit_data_web():
    for s_info in quat_table.find_all('tbody'):
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

        add_quaterly="""insert into infy_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        # m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()
# mydb.close()      
# print(soup)

def get_opm_data_web():
    for s_info in quat_table.find_all('tbody'):
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

        add_quaterly="""insert into infy_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        # m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()

def get_oincome_data_web():
    for s_info in quat_table.find_all('tbody'):
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

        add_quaterly="""insert into infy_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()

def get_intrest_data_web():
    for s_info in quat_table.find_all('tbody'):
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

        add_quaterly="""insert into infy_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()

def get_depreciation_data_web():
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        p1=s_info.find_all('td')[79].text
        p2 = s_info.find_all('td')[80].text
        p3 = s_info.find_all('td')[81].text
        p4 = s_info.find_all('td')[82].text
        p5 = s_info.find_all('td')[83].text
        p6 = s_info.find_all('td')[84].text
        p7 = s_info.find_all('td')[85].text
        p8 = s_info.find_all('td')[86].text
        p9 = s_info.find_all('td')[87].text
        p10 = s_info.find_all('td')[88].text
        p11 = s_info.find_all('td')[89].text
        p12 = s_info.find_all('td')[90].text
        print(p1)

        add_quaterly="""insert into infy_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        # m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()
    
def get_pbt_data_web():
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        p1=s_info.find_all('td')[92].text
        p2 = s_info.find_all('td')[93].text
        p3 = s_info.find_all('td')[94].text
        p4 = s_info.find_all('td')[95].text
        p5 = s_info.find_all('td')[96].text
        p6 = s_info.find_all('td')[97].text
        p7 = s_info.find_all('td')[98].text
        p8 = s_info.find_all('td')[99].text
        p9 = s_info.find_all('td')[100].text
        p10 = s_info.find_all('td')[101].text
        p11 = s_info.find_all('td')[102].text
        p12 = s_info.find_all('td')[103].text
        print(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)

        add_quaterly="""insert into infy_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()

def get_tax_data_web():
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        p1=s_info.find_all('td')[105].text
        p2 = s_info.find_all('td')[106].text
        p3 = s_info.find_all('td')[107].text
        p4 = s_info.find_all('td')[108].text
        p5 = s_info.find_all('td')[109].text
        p6 = s_info.find_all('td')[110].text
        p7 = s_info.find_all('td')[111].text
        p8 = s_info.find_all('td')[112].text
        p9 = s_info.find_all('td')[113].text
        p10 = s_info.find_all('td')[114].text
        p11 = s_info.find_all('td')[115].text
        p12 = s_info.find_all('td')[116].text
        print(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)

        add_quaterly="""insert into infy_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()

def get_netprofit_data_web():
    for s_info in quat_table.find_all('tbody'):
        rows= s_info.find_all('tr')
        p1=s_info.find_all('td')[118].text
        p2 = s_info.find_all('td')[119].text
        p3 = s_info.find_all('td')[120].text
        p4 = s_info.find_all('td')[121].text
        p5 = s_info.find_all('td')[122].text
        p6 = s_info.find_all('td')[123].text
        p7 = s_info.find_all('td')[124].text
        p8 = s_info.find_all('td')[125].text
        p9 = s_info.find_all('td')[126].text
        p10 = s_info.find_all('td')[127].text
        p11 = s_info.find_all('td')[128].text
        p12 = s_info.find_all('td')[129].text
        print(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)

        add_quaterly="""insert into infy_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()

def get_eps_data_web():
    for s_info in quat_table.find_all('div',id="profit-loss"):
        rows= s_info.find_all('td')
        p1=s_info.find_all('td')[131].text
        p2 = s_info.find_all('td')[132].text
        p3 = s_info.find_all('td')[133].text
        p4 = s_info.find_all('td')[134].text
        p5 = s_info.find_all('td')[135].text
        p6 = s_info.find_all('td')[136].text
        p7 = s_info.find_all('td')[137].text
        p8 = s_info.find_all('td')[138].text
        p9 = s_info.find_all('td')[139].text
        p10 = s_info.find_all('td')[140].text
        p11 = s_info.find_all('td')[141].text
        p12 = s_info.find_all('td')[142].text
        print(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)

        add_quaterly="""insert into infy_quaterly_result(
                    Dec_2018,Mar_2019,Jun_2019,Sep_2019,Dec_2019,Mar_2020,Jun_2020,Sep_2020,Dec_2020,Mar_2021,Jun_2021,Sep_2021)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        quat_info=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12)
        print(add_quaterly,quat_info)

        # m_cursor.execute(add_quaterly,quat_info)
        mydb.commit()

if __name__ == '__main__':
    # get_Sales_data_web()
    # get_expenses_data_web()
    # get_oprofit_data_web()
    # get_opm_data_web()
    # get_oincome_data_web()
    # get_intrest_data_web()
    # get_depreciation_data_web()
    # get_pbt_data_web()
    # get_tax_data_web()
    # get_netprofit_data_web()
    get_eps_data_web()
