# Import Block

import mysql.connector
from nsetools import nse

# Database Connection

mydb = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="",
    database="stock_market")

# Create Table For Quaterly Result

def create_table(str):
    m_cursor = mydb.cursor()

    q=("""create table """ + str + """_quaterly_result""" +  """ (
            Dec_2018 VARCHAR(20),
            Mar_2019 VARCHAR(20),
            Jun_2019 VARCHAR(20),
            Sep_2019 VARCHAR(20),
            Dec_2019 VARCHAR(20),
            Mar_2020 VARCHAR(20),
            Jun_2020 VARCHAR(20),
            Sep_2020 VARCHAR(20),
            Dec_2020 VARCHAR(20),
            Mar_2021 VARCHAR(20),
            Jun_2021 VARCHAR(20),
            Sep_2021 VARCHAR(20) ) """ )
    print(q)     
    m_cursor.execute(q)
    m_cursor.close()
    mydb.commit()
    mydb.close()

# Create Table For Peetr Comparision

def create_table_Peer_Comparision(str):
    m_cursor = mydb.cursor()

    q=("""create table """ + str + """_Peer_Comparision""" +  """ (
            SNO DECIMAL(3),
            Name varchar(20),
            CMPRs DECIMAL(20),
            PE DECIMAL(10,2),
            Mar_Cap_Rs_Cr DECIMAL(20,2),
            Div_Yld DECIMAL(20,2),
            NP_Qtr_Rs_Cr DECIMAL(20,4),
            Qtr_Profit_Var DECIMAL(20,4),
            Sales_Qtr_Rs_Cr DECIMAL(20,4),
            Qtr_Sales_Var DECIMAL(20,4),
            ROCE DECIMAL(20,4) ) """ )
    print(q)     
    m_cursor.execute(q)
    m_cursor.close()
    mydb.commit()
    mydb.close()

# Create Tbale For Profit And Loss 

def create_table_profit_loss(str):
    m_cursor = mydb.cursor()

    q=("""create table """ + str + """_profit_loss""" +  """ (
            Mar_2010 DECIMAL(20,2),
            Mar_2011 DECIMAL(20,2),
            Mar_2012 DECIMAL(20,2),
            Mar_2013 DECIMAL(20,2),
            Mar_2014 DECIMAL(20,2),
            Mar_2015 DECIMAL(20,2),
            Mar_2016 DECIMAL(20,2),
            Mar_2017 DECIMAL(20,2),
            Mar_2018 DECIMAL(20,2),
            Mar_2019 DECIMAL(20,2),
            Mar_2020 DECIMAL(20,2),
            Mar_2021 DECIMAL(20,2),
            TTM DECIMAL(20,2) ) """ )
    print(q)     
    m_cursor.execute(q)
    m_cursor.close()
    mydb.commit()
    mydb.close()

# Create Table For balance Sheet

def create_table_Balance_Sheet(str):
    m_cursor = mydb.cursor()

    q=("""create table """ + str + """_balance_sheet""" +  """ (
            Mar_2010 DECIMAL(20,2),
            Mar_2011 DECIMAL(20,2),
            Mar_2012 DECIMAL(20,2),
            Mar_2013 DECIMAL(20,2),
            Mar_2014 DECIMAL(20,2),
            Mar_2015 DECIMAL(20,2),
            Mar_2016 DECIMAL(20,2),
            Mar_2017 DECIMAL(20,2),
            Mar_2018 DECIMAL(20,2),
            Mar_2019 DECIMAL(20,2),
            Mar_2020 DECIMAL(20,2),
            Mar_2021 DECIMAL(20,2),
            Sep_2021 DECIMAL(20,2) ) """ )
    print(q)     
    m_cursor.execute(q)
    m_cursor.close()
    mydb.commit()
    mydb.close()

# Create Table For Cash Flows

def create_table_Cash_Flows(str):
    m_cursor = mydb.cursor()

    q=("""create table """ + str + """_cash_flows""" +  """ (
            Mar_2010 DECIMAL(20,2),
            Mar_2011 DECIMAL(20,2),
            Mar_2012 DECIMAL(20,2),
            Mar_2013 DECIMAL(20,2),
            Mar_2014 DECIMAL(20,2),
            Mar_2015 DECIMAL(20,2),
            Mar_2016 DECIMAL(20,2),
            Mar_2017 DECIMAL(20,2),
            Mar_2018 DECIMAL(20,2),
            Mar_2019 DECIMAL(20,2),
            Mar_2020 DECIMAL(20,2),
            Mar_2021 DECIMAL(20,2)) """ )
    print(q)     
    m_cursor.execute(q)
    m_cursor.close()
    mydb.commit()
    mydb.close()

# Create Table For Ratios

def create_table_Ratios(str):
    m_cursor = mydb.cursor()

    q=("""create table """ + str + """_Ratios""" +  """ (
            Mar_2010 DECIMAL(20),
            Mar_2011 DECIMAL(20),
            Mar_2012 DECIMAL(20),
            Mar_2013 DECIMAL(20),
            Mar_2014 DECIMAL(20),
            Mar_2015 DECIMAL(20),
            Mar_2016 DECIMAL(20),
            Mar_2017 DECIMAL(20),
            Mar_2018 DECIMAL(20),
            Mar_2019 DECIMAL(20),
            Mar_2020 DECIMAL(20),
            Mar_2021 DECIMAL(20) ) """ )
    print(q)     
    m_cursor.execute(q)
    m_cursor.close()
    mydb.commit()
    mydb.close()

# Create Table For ShareHolding Problem

def create_table_Shareholding_Problem(str):
    m_cursor = mydb.cursor()

    q=("""create table """ + str + """_shareholidng_problem""" +  """ (
            Dec_2018 DECIMAL(20,2),
            Mar_2019 DECIMAL(20,2),
            Jun_2019 DECIMAL(20,2),
            Sep_2019 DECIMAL(20,2),
            Dec_2019 DECIMAL(20,2),
            Mar_2020 DECIMAL(20,2),
            Jun_2020 DECIMAL(20,2),
            Sep_2020 DECIMAL(20,2),
            Dec_2020 DECIMAL(20,2),
            Mar_2021 DECIMAL(20,2),
            Jun_2021 DECIMAL(20,2),
            Sep_2021 DECIMAL(20,2) ) """ )
    print(q)     
    m_cursor.execute(q)
    m_cursor.close()
    mydb.commit()
    mydb.close()


# Main Function

if __name__ == '__main__':
    # create_table('infy')
    # create_table_Peer_Comparision('infy')
    # create_table_profit_loss('infy')
    # create_table_Balance_Sheet('infy')
    # create_table_Cash_Flows('infy')
    create_table_Ratios('infy')
    # create_table_Shareholding_Problem('infy')

