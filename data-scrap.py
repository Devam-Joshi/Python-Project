# Import Part
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

if __name__ == '__main__':
    # get_Sales_data_web()
    # get_expenses_data_web()
    get_oprofit_data_web()