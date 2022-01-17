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
m_cursor = mydb.cursor()
# Create Table For Quaterly Result

def create_table(str):
    

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
    mydb.commit()
   
# Create Tbale For Profit And Loss 

def create_table_profit_loss(str):

    q=("""create table """ + str + """_profit_loss""" +  """ (
            Mar_2010 varchar(20),
            Mar_2011 varchar(20),
            Mar_2012 varchar(20),
            Mar_2013 varchar(20),
            Mar_2014 varchar(20),
            Mar_2015 varchar(20),
            Mar_2016 varchar(20),
            Mar_2017 varchar(20),
            Mar_2018 varchar(20),
            Mar_2019 varchar(20),
            Mar_2020 varchar(20),
            Mar_2021 varchar(20),
            TTM varchar(20) ) """ )
    print(q)     
    m_cursor.execute(q)
    mydb.commit()


# Create Table For balance Sheet

def create_table_Balance_Sheet(str):
    q=("""create table """ + str + """_balance_sheet""" +  """ (
            Mar_2010 VARCHAR(20),
            Mar_2011 VARCHAR(20),
            Mar_2012 VARCHAR(20),
            Mar_2013 VARCHAR(20),
            Mar_2014 VARCHAR(20),
            Mar_2015 VARCHAR(20),
            Mar_2016 VARCHAR(20),
            Mar_2017 VARCHAR(20),
            Mar_2018 VARCHAR(20),
            Mar_2019 VARCHAR(20),
            Mar_2020 VARCHAR(20),
            Mar_2021 VARCHAR(20),
            Sep_2021 VARCHAR(20) ) """ )
    print(q)     
    m_cursor.execute(q)
    mydb.commit()
    
# Create Table For Cash Flows

def create_table_Cash_Flows(str):
    q=("""create table """ + str + """_cash_flows""" +  """ (
            Mar_2010 varchar(20),
            Mar_2011 varchar(20),
            Mar_2012 varchar(20),
            Mar_2013 varchar(20),
            Mar_2014 varchar(20),
            Mar_2015 varchar(20),
            Mar_2016 varchar(20),
            Mar_2017 varchar(20),
            Mar_2018 varchar(20),
            Mar_2019 varchar(20),
            Mar_2020 varchar(20),
            Mar_2021 varchar(20)) """ )
    print(q)     
    m_cursor.execute(q)
    mydb.commit()
    
# Create Table For Ratios

def create_table_Ratios(str):

    q=("""create table """ + str + """_Ratios""" +  """ (
            Mar_2010 varchar(20),
            Mar_2011 varchar(20),
            Mar_2012 varchar(20),
            Mar_2013 varchar(20),
            Mar_2014 varchar(20),
            Mar_2015 varchar(20),
            Mar_2016 varchar(20),
            Mar_2017 varchar(20),
            Mar_2018 varchar(20),
            Mar_2019 varchar(20),
            Mar_2020 varchar(20),
            Mar_2021 varchar(20) ) """ )
    print(q)     
    m_cursor.execute(q)
    mydb.commit()

# Create Table For ShareHolding Problem

def create_table_Shareholding_Problem(str):
    q=("""create table """ + str + """_shareholidng_problem""" +  """ (
            Dec_2018 varchar(20),
            Mar_2019 varchar(20),
            Jun_2019 varchar(20),
            Sep_2019 varchar(20),
            Dec_2019 varchar(20),
            Mar_2020 varchar(20),
            Jun_2020 varchar(20),
            Sep_2020 varchar(20),
            Dec_2020 varchar(20),
            Mar_2021 varchar(20),
            Jun_2021 varchar(20),
            Sep_2021 varchar(20) ) """ )
    print(q)     
    m_cursor.execute(q)
    mydb.commit()

# Main Function

if __name__ == '__main__':
    # create_table('pidilitind')
    # create_table_profit_loss('adanigreen')
    # create_table_Balance_Sheet('pidilitind')
    # create_table_Cash_Flows('pidilitind')
    # create_table_Ratios('pidilitind')
    create_table_Shareholding_Problem('adanigreen')

