import mysql.connector
from nsetools import nse

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="stock_quote"
)
m_cursor = mydb.cursor()

m_cursor.execute("""create table infy(
        cur_date DATE,
        averagePrice varchar(20) not null,
        buyQuantity1 varchar(20)not null,
        buyQuantity2 varchar(20) not null,
        buyQuantity3 varchar(20) not null,
        buyQuantity4 varchar(20) not null,
        buyQuantity5 varchar(20) not null,
        closePrice varchar(20) not null,
        companyName varchar(20) not null,
        dayHigh varchar(20) not null,
        dayLow varchar(20) not null,
        deliveryQuantity varchar(25) not null,
        deliveryToTradedQuantity varchar(20) not null,
        faceValue varchar(20) not null,
        high52 varchar(20) not null,
        lastPrice varchar(20) not null,
        low52 varchar(20) not null,
        open1 varchar(20) not null,
        pChange varchar(20) not null,
        previousClose varchar(20) not null,
        priceBand varchar(20) not null,
        pricebandlower varchar(20) not null,
        pricebandupper varchar(20) not null, 
        quantityTraded varchar(30) not null,
        recordDate  DATE not null,
        sellQuantity1 varchar(20) not null,
        sellQuantity2 varchar(20) not null, 
        sellQuantity3 varchar(20) not null,
        sellQuantity4 varchar(20) not null,
        sellQuantity5 varchar(20) not null,
        symbol varchar(20) not null,
        totalBuyQuantity varchar(20) not null,
        totalSellQuantity varchar(20) not null,
        totalTradedValue varchar(30) not null,
        totalTradedVolume varchar(20) not null) """)

m_cursor.close()
mydb.commit()
mydb.close()