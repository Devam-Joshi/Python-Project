import mysql.connector
from nsetools import Nse
import datetime

# Connection Of SQL
data = { 1: "Stock"}
mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="stock_quote"
)

# Main Data Of Stock Quote
nse = Nse()
m_cursor = mydb.cursor()

# for i in  data:
# while True:
quote = nse.get_quote('infy');

cur_date = str(0)
averagePrice = str(quote["averagePrice"])
buyQuantity1 = str(quote["buyQuantity1"])
buyQuantity2 = str(quote["buyQuantity2"])
buyQuantity3 = str(quote["buyQuantity3"])
buyQuantity4 = str(quote["buyQuantity4"])
buyQuantity5 = str(quote["buyQuantity5"])
closePrice = str(quote["closePrice"])
companyName= str("InfosysLimited")
dayHigh= str(quote["dayHigh"])
dayLow= str(quote["dayLow"])
deliveryQuantity= str(quote["deliveryQuantity"])
deliveryToTradedQuantity= str(quote["deliveryToTradedQuantity"])
faceValue= str(quote["faceValue"])
high52= str(quote["high52"])
lastPrice= str(quote["lastPrice"] )
low52= str(quote["low52"])
open1= str(quote["open"])
pChange= str(quote["pChange"])
previousClose= str(quote["previousClose"])
priceBand= str("noband")
pricebandlower= str(quote["pricebandlower"])
pricebandupper= str(quote["pricebandupper"])
quantityTraded= str(quote["quantityTraded"])
recordDate=  str(quote["recordDate"])
sellQuantity1= str(quote["sellQuantity1"])
sellQuantity2= str(quote["sellQuantity2"])
sellQuantity3= str(quote["sellQuantity3"])
sellQuantity4= str(quote["sellQuantity4"])
sellQuantity5= str(quote["sellQuantity5"])
symbol= str(quote["symbol"])
totalBuyQuantity= str(quote["totalBuyQuantity"])
totalSellQuantity= str(quote["totalSellQuantity"])
totalTradedValue= str(quote["totalTradedValue"])
totalTradedVolume= str(quote["totalTradedVolume"])

m_cursor = mydb.cursor()

# Insert Query 

q = """insert into infy (cur_date,averagePrice,buyQuantity1,buyQuantity2,buyQuantity3,buyQuantity4,buyQuantity5,closePrice,companyName,dayHigh,dayLow,deliveryQuantity,deliveryToTradedQuantity,faceValue,high52,lastPrice,low52,open1,pChange,previousClose,priceBand,pricebandlower,pricebandupper,quantityTraded,recordDate,sellQuantity1,sellQuantity2,sellQuantity3,sellQuantity4,sellQuantity5,symbol,totalBuyQuantity,totalSellQuantity,totalTradedValue,totalTradedVolume) values(""" 
q = q + cur_date + """,""" + averagePrice + """,""" + buyQuantity1 + """,""" + buyQuantity2 + """,""" + buyQuantity3 + """,""" + buyQuantity4 + """,""" + buyQuantity5 + """,""" + closePrice + """,""" + companyName + """,""" + dayHigh + """,""" + dayLow + """,""" + deliveryQuantity + ""","""+ deliveryToTradedQuantity + ""","""+ faceValue + ""","""+ high52 + """,""" + lastPrice + """,""" + low52 + ""","""+ open1 + """,""" + pChange + """,""" + previousClose + """,""" + priceBand + """,""" + pricebandlower + """,""" + pricebandupper + """,""" + quantityTraded + """,""" + recordDate + """,""" + sellQuantity1 + """,""" + sellQuantity2 + """,""" + sellQuantity3 + """,""" + sellQuantity4 + """,""" + sellQuantity5 + """,""" + symbol + """,""" + totalBuyQuantity + """,""" + totalSellQuantity + """,""" + totalTradedValue + """,""" + totalTradedVolume 
q = q + """)"""

# Print Query 

print(q)
# m_cursor.execute(q)
mydb.commit()