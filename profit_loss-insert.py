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

url = "https://www.screener.in/company/INFY/consolidated/"

r = requests.get(url)

# Define Variables
m_cursor = mydb.cursor()

soup = BeautifulSoup(r.text, 'html.parser')

profit_loss = soup.find('section', id='profit-loss')


def first_row():
    for i in profit_loss.find_all('tbody'):
        rows = i.find_all('tr')
        p1 = i.find_all('td')[1].text
        p2 = i.find_all('td')[2].text
        p3 = i.find_all('td')[3].text
        p4 = i.find_all('td')[4].text
        p5 = i.find_all('td')[5].text
        p6 = i.find_all('td')[6].text
        p7 = i.find_all('td')[7].text
        p8 = i.find_all('td')[8].text
        p9 = i.find_all('td')[9].text
        p10 = i.find_all('td')[10].text
        p11 = i.find_all('td')[11].text
        p12 = i.find_all('td')[12].text
        p13 = i.find_all('td')[13].text

        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)

        query = """insert into infosys_profit_loss
                ( Mar_2010,	Mar_2011, Mar_2012, Mar_2013, Mar_2014,	Mar_2015, Mar_2016,	Mar_2017, Mar_2018, Mar_2019, Mar_2020, Mar_2021, TTM ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        profit_loss_query = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        print(query, profit_loss_query)

        m_cursor.execute(query, profit_loss_query)
        mydb.commit()

def second_row():
    for i in profit_loss.find_all('tbody'):
        rows = i.find_all('tr')
        p1 = i.find_all('td')[15].text
        p2 = i.find_all('td')[16].text
        p3 = i.find_all('td')[17].text
        p4 = i.find_all('td')[18].text
        p5 = i.find_all('td')[19].text
        p6 = i.find_all('td')[20].text
        p7 = i.find_all('td')[21].text
        p8 = i.find_all('td')[22].text
        p9 = i.find_all('td')[23].text
        p10 = i.find_all('td')[24].text
        p11 = i.find_all('td')[25].text
        p12 = i.find_all('td')[26].text
        p13 = i.find_all('td')[27].text

        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)

        query = """insert into infosys_profit_loss
                ( Mar_2010,	Mar_2011, Mar_2012, Mar_2013, Mar_2014,	Mar_2015, Mar_2016,	Mar_2017, Mar_2018, Mar_2019, Mar_2020, Mar_2021, TTM ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        profit_loss_query = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        print(query, profit_loss_query)

        m_cursor.execute(query, profit_loss_query)
        mydb.commit()


def third_row():
    for i in profit_loss.find_all('tbody'):
        rows = i.find_all('tr')
        p1 = i.find_all('td')[29].text
        p2 = i.find_all('td')[30].text
        p3 = i.find_all('td')[31].text
        p4 = i.find_all('td')[32].text
        p5 = i.find_all('td')[33].text
        p6 = i.find_all('td')[34].text
        p7 = i.find_all('td')[35].text
        p8 = i.find_all('td')[36].text
        p9 = i.find_all('td')[37].text
        p10 = i.find_all('td')[38].text
        p11 = i.find_all('td')[39].text
        p12 = i.find_all('td')[40].text
        p13 = i.find_all('td')[41].text

        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)

        query = """insert into infosys_profit_loss  
                ( Mar_2010,	Mar_2011, Mar_2012, Mar_2013, Mar_2014,	Mar_2015, Mar_2016,	Mar_2017, Mar_2018, Mar_2019, Mar_2020, Mar_2021, TTM ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        profit_loss_query = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        print(query, profit_loss_query)

        m_cursor.execute(query, profit_loss_query)
        mydb.commit()


def fourth_row():
    for i in profit_loss.find_all('tbody'):
        rows = i.find_all('tr')
        p1 = i.find_all('td')[43].text
        p2 = i.find_all('td')[44].text
        p3 = i.find_all('td')[45].text
        p4 = i.find_all('td')[46].text
        p5 = i.find_all('td')[47].text
        p6 = i.find_all('td')[48].text
        p7 = i.find_all('td')[49].text
        p8 = i.find_all('td')[50].text
        p9 = i.find_all('td')[51].text
        p10 = i.find_all('td')[52].text
        p11 = i.find_all('td')[53].text
        p12 = i.find_all('td')[54].text
        p13 = i.find_all('td')[55].text

        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)

        query = """insert into infosys_profit_loss  
                ( Mar_2010,	Mar_2011, Mar_2012, Mar_2013, Mar_2014,	Mar_2015, Mar_2016,	Mar_2017, Mar_2018, Mar_2019, Mar_2020, Mar_2021, TTM ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        profit_loss_query = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        print(query, profit_loss_query)

        m_cursor.execute(query, profit_loss_query)
        mydb.commit()


def fifth_row():
    for i in profit_loss.find_all('tbody'):
        rows = i.find_all('tr')
        p1 = i.find_all('td')[57].text
        p2 = i.find_all('td')[58].text
        p3 = i.find_all('td')[59].text
        p4 = i.find_all('td')[60].text
        p5 = i.find_all('td')[61].text
        p6 = i.find_all('td')[62].text
        p7 = i.find_all('td')[63].text
        p8 = i.find_all('td')[64].text
        p9 = i.find_all('td')[65].text
        p10 = i.find_all('td')[66].text
        p11 = i.find_all('td')[67].text
        p12 = i.find_all('td')[68].text
        p13 = i.find_all('td')[69].text

        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)

        query = """insert into infosys_profit_loss  
                ( Mar_2010,	Mar_2011, Mar_2012, Mar_2013, Mar_2014,	Mar_2015, Mar_2016,	Mar_2017, Mar_2018, Mar_2019, Mar_2020, Mar_2021, TTM ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        profit_loss_query = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        print(query, profit_loss_query)

        m_cursor.execute(query, profit_loss_query)
        mydb.commit()


def sixth_row():
    for i in profit_loss.find_all('tbody'):
        rows = i.find_all('tr')
        p1 = i.find_all('td')[71].text
        p2 = i.find_all('td')[72].text
        p3 = i.find_all('td')[73].text
        p4 = i.find_all('td')[74].text
        p5 = i.find_all('td')[75].text
        p6 = i.find_all('td')[76].text
        p7 = i.find_all('td')[77].text
        p8 = i.find_all('td')[78].text
        p9 = i.find_all('td')[79].text
        p10 = i.find_all('td')[80].text
        p11 = i.find_all('td')[81].text
        p12 = i.find_all('td')[82].text
        p13 = i.find_all('td')[83].text

        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)

        query = """insert into infosys_profit_loss  
                ( Mar_2010,	Mar_2011, Mar_2012, Mar_2013, Mar_2014,	Mar_2015, Mar_2016,	Mar_2017, Mar_2018, Mar_2019, Mar_2020, Mar_2021, TTM ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        profit_loss_query = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        print(query, profit_loss_query)

        m_cursor.execute(query, profit_loss_query)
        mydb.commit()


def seventh_row():
    for i in profit_loss.find_all('tbody'):
        rows = i.find_all('tr')
        p1 = i.find_all('td')[85].text
        p2 = i.find_all('td')[86].text
        p3 = i.find_all('td')[87].text
        p4 = i.find_all('td')[88].text
        p5 = i.find_all('td')[89].text
        p6 = i.find_all('td')[90].text
        p7 = i.find_all('td')[91].text
        p8 = i.find_all('td')[92].text
        p9 = i.find_all('td')[93].text
        p10 = i.find_all('td')[94].text
        p11 = i.find_all('td')[95].text
        p12 = i.find_all('td')[96].text
        p13 = i.find_all('td')[97].text

        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)

        query = """insert into infosys_profit_loss  
                ( Mar_2010,	Mar_2011, Mar_2012, Mar_2013, Mar_2014,	Mar_2015, Mar_2016,	Mar_2017, Mar_2018, Mar_2019, Mar_2020, Mar_2021, TTM ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        profit_loss_query = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        print(query, profit_loss_query)

        m_cursor.execute(query, profit_loss_query)
        mydb.commit()


def eighth_row():
    for i in profit_loss.find_all('tbody'):
        rows = i.find_all('tr')
        p1 = i.find_all('td')[99].text
        p2 = i.find_all('td')[100].text
        p3 = i.find_all('td')[101].text
        p4 = i.find_all('td')[102].text
        p5 = i.find_all('td')[103].text
        p6 = i.find_all('td')[104].text
        p7 = i.find_all('td')[105].text
        p8 = i.find_all('td')[106].text
        p9 = i.find_all('td')[107].text
        p10 = i.find_all('td')[108].text
        p11 = i.find_all('td')[109].text
        p12 = i.find_all('td')[110].text
        p13 = i.find_all('td')[111].text

        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)

        query = """insert into infosys_profit_loss  
                ( Mar_2010,	Mar_2011, Mar_2012, Mar_2013, Mar_2014,	Mar_2015, Mar_2016,	Mar_2017, Mar_2018, Mar_2019, Mar_2020, Mar_2021, TTM ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        profit_loss_query = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        print(query, profit_loss_query)

        m_cursor.execute(query, profit_loss_query)
        mydb.commit()

def ningth_row():
    for i in profit_loss.find_all('tbody'):
        rows = i.find_all('tr')
        p1 = i.find_all('td')[113].text
        p2 = i.find_all('td')[114].text
        p3 = i.find_all('td')[115].text
        p4 = i.find_all('td')[116].text
        p5 = i.find_all('td')[117].text
        p6 = i.find_all('td')[118].text
        p7 = i.find_all('td')[119].text
        p8 = i.find_all('td')[120].text
        p9 = i.find_all('td')[121].text
        p10 = i.find_all('td')[122].text
        p11 = i.find_all('td')[123].text
        p12 = i.find_all('td')[124].text
        p13 = i.find_all('td')[125].text

        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)

        query = """insert into infosys_profit_loss  
                ( Mar_2010,	Mar_2011, Mar_2012, Mar_2013, Mar_2014,	Mar_2015, Mar_2016,	Mar_2017, Mar_2018, Mar_2019, Mar_2020, Mar_2021, TTM ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        profit_loss_query = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        print(query, profit_loss_query)

        m_cursor.execute(query, profit_loss_query)
        mydb.commit()

def tenth_row():
    for i in profit_loss.find_all('tbody'):
        rows = i.find_all('tr')
        p1 = i.find_all('td')[127].text
        p2 = i.find_all('td')[128].text
        p3 = i.find_all('td')[129].text
        p4 = i.find_all('td')[130].text
        p5 = i.find_all('td')[131].text
        p6 = i.find_all('td')[132].text
        p7 = i.find_all('td')[133].text
        p8 = i.find_all('td')[134].text
        p9 = i.find_all('td')[135].text
        p10 = i.find_all('td')[136].text
        p11 = i.find_all('td')[137].text
        p12 = i.find_all('td')[138].text
        p13 = i.find_all('td')[139].text

        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)

        query = """insert into infosys_profit_loss  
                ( Mar_2010,	Mar_2011, Mar_2012, Mar_2013, Mar_2014,	Mar_2015, Mar_2016,	Mar_2017, Mar_2018, Mar_2019, Mar_2020, Mar_2021, TTM ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        profit_loss_query = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        print(query, profit_loss_query)

        m_cursor.execute(query, profit_loss_query)
        mydb.commit()


def eleventh_row():
    for i in profit_loss.find_all('tbody'):
        rows = i.find_all('tr')
        p1 = i.find_all('td')[141].text
        p2 = i.find_all('td')[142].text
        p3 = i.find_all('td')[143].text
        p4 = i.find_all('td')[144].text
        p5 = i.find_all('td')[145].text
        p6 = i.find_all('td')[146].text
        p7 = i.find_all('td')[147].text
        p8 = i.find_all('td')[148].text
        p9 = i.find_all('td')[149].text
        p10 = i.find_all('td')[150].text
        p11 = i.find_all('td')[151].text
        p12 = i.find_all('td')[152].text
        p13 = i.find_all('td')[153].text

        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)

        query = """insert into infosys_profit_loss  
                ( Mar_2010,	Mar_2011, Mar_2012, Mar_2013, Mar_2014,	Mar_2015, Mar_2016,	Mar_2017, Mar_2018, Mar_2019, Mar_2020, Mar_2021, TTM ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        profit_loss_query = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        print(query, profit_loss_query)

        m_cursor.execute(query, profit_loss_query)
        mydb.commit()


def twelth_row():
    for i in profit_loss.find_all('tbody'):
        rows = i.find_all('tr')
        p1 = i.find_all('td')[155].text
        p2 = i.find_all('td')[156].text
        p3 = i.find_all('td')[157].text
        p4 = i.find_all('td')[158].text
        p5 = i.find_all('td')[159].text
        p6 = i.find_all('td')[160].text
        p7 = i.find_all('td')[161].text
        p8 = i.find_all('td')[162].text
        p9 = i.find_all('td')[163].text
        p10 = i.find_all('td')[164].text
        p11 = i.find_all('td')[165].text
        p12 = i.find_all('td')[166].text
        p13 = i.find_all('td')[167].text

        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)

        query = """insert into infosys_profit_loss  
                ( Mar_2010,	Mar_2011, Mar_2012, Mar_2013, Mar_2014,	Mar_2015, Mar_2016,	Mar_2017, Mar_2018, Mar_2019, Mar_2020, Mar_2021, TTM ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        profit_loss_query = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        print(query, profit_loss_query)

        m_cursor.execute(query, profit_loss_query)
        mydb.commit()


if __name__ == '__main__':
    # first_row()
    # second_row()
    # third_row()
    # fourth_row()
    # fifth_row()
    # sixth_row()
    # seventh_row()
    # eighth_row()
    # ningth_row()
    # tenth_row()
    # eleventh_row()
    twelth_row()