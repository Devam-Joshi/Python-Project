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

stock_list = ["ABBOTINDIA","ADANIENT","ADANIPORTS","ALKEM","AMBUJACEM"]

url =["https://www.screener.in/company/ABBOTINDIA/",
        "https://www.screener.in/company/ADANIENT/consolidated/",
        "https://www.screener.in/company/ADANIPORTS/consolidated/",
        "https://www.screener.in/company/ALKEM/consolidated/",
        "https://www.screener.in/company/AMBUJACEM/consolidated/"]

# Define Variables
m_cursor = mydb.cursor()


def insert_ratios(r,j):
    soup= BeautifulSoup(r.text,'html.parser')
    ratios= soup.find('section', id='ratios')
    def get_debator_day_data_web():
        stk_data =[]
        for s_info in ratios.find_all('tbody'):
            rows2= s_info.find_all('tr')
            rows = s_info.find('th')
            print(rows)
            i=1
            while(i<=len(rows)):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)

            add_quaterly="""insert into """+j+"""_ratios(rows) values(rows)"""
            print(add_quaterly,stk_data)
            # m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()

    def get_Inventor_Days_data_web():
        stk_data =[]
        rows=[]
        c=0
        stk_length = len(stk_data)

        for stock_list in ratios.find_all('thead'):
                row1= stock_list.find_all('th')
                while(c<=len(rows)):
                    if(len(rows)==0):
                        # rows.insert(c,"field_name")
                        rows.insert(c,stock_list.find_all('th')[0].text)
                        print(len(rows))
                        c=c+1
                        print(c)
                    else:
                        while(c<=len(rows)):
                            rows.insert(c,stock_list.find_all('th')[c].text)
                            c=c+1
                            print(rows)
        for stock_list in ratios.find_all('tbody'):
                row1= stock_list.find_all('tr')
                i=14
                while(i<=23):
                    stk_data.insert(i,stock_list.find_all('td')[i].text)
                    i=i+1
                    print(stk_data)
            
                add_quaterly="""insert into """+j+"""_ratios("""+str(rows)+""" ) values("InventorDays","""+str(stk_data)+""" )"""
                print(add_quaterly,stk_data)
                # m_cursor.execute(add_quaterly,stk_data)
                mydb.commit()

    def get_days_payable_data_web():
        stk_data =[]
        for s_info in ratios.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=1
            while(i<=len(rows)):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)
        
            add_quaterly="""insert into """+j+"""_ratios(
                            rows)
                        values(rows)
                        """
            print(add_quaterly,stk_data)
            # m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()

    def get_ccCycle_data_web():
        stk_data =[]
        
        for s_info in ratios.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=1
            while(i<="\n"): 
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)
            

            add_quaterly="""insert into """+j+"""_ratios(
                            rows)
                        values(rows)
                        """
            print(add_quaterly,stk_data)
            # m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()
            
    def get_Working_Capitald_data_web():
        stk_data =[]
        for s_info in ratios.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=1
            while(i<=len(rows)):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)
            

            add_quaterly="""insert into """+j+"""_ratios(
                            rows)
                        values(rows)
                        """
            print(add_quaterly,stk_data)
            # m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()

    def get_Roce_data_web():
        stk_data =[]
        for s_info in ratios.find_all('tbody'):
            rows= s_info.find_all('tr')
            i=1
            while(i<=len(rows)):
                stk_data.insert(i,s_info.find_all('td')[i].text)
                i=i+1
                print(stk_data)
            

            add_quaterly="""insert into """+j+"""_ratios(
                            rows)
                        values(rows)
                        """
            print(add_quaterly,stk_data)
            # m_cursor.execute(add_quaterly,stk_data)
            mydb.commit()

    get_Inventor_Days_data_web()
    # get_days_payable_data_web()
    # get_ccCycle_data_web()
    # get_Working_Capitald_data_web()
    # get_Roce_data_web()

if __name__ == '__main__':
    
    i=0
    while(i<len(stock_list)):
        r=requests.get(url[i])
        print(url[i])
        print(r)
        insert_ratios(r,stock_list[i])
        i=i+1   
   
