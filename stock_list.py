from nsetools import Nse

stock_list = ["ABBOTINDIA","ADANIENT","ADANIGREEN","ADANIPORTS","ADANITRANS","ALKEM","AMBUJACEM","APOLLOHOSP","ASIANPAINT","AUROPHARMA","DMART","AXISBANK","BAJAJ-AUTO","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BANDHANBNK","BERGEPAINT","BPCL","BHARTIARTL","BIOCON","BOSCHLTD","BRITANNIA","CADILAHC","CIPLA","COALINDIA","COLPAL","DLF","DABUR","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GLAND","GODREJPROP","GRASIM","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HAVELLS","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","HDFC","ICICIBANK","ICICIGI","ICICIPRULI","ITC","IOC","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INDIGO","JSWSTEEL","JUBLFOOD","KOTAKBANK","LTI","LT","LUPIN","MRF","M&M","MARICO","MARUTI","MUTHOOTFIN","NMDC","NTPC","NESTLEIND","ONGC","PETRONET","PIDILITIND","PEL","POWERGRID","PGHH","PNB","RELIANCE","SBICARD","SBILIFE","SHREECEM","SIEMENS","SBIN","SUNPHARMA","TCS","TATACONSUM","TATAMOTORS","TATASTEEL","TECHM","TITAN","TORNTPHARM","UPL","ULTRACEMCO","UBL","MCDOWELL-N","VEDL","WIPRO","YESBANK"]

def checklow_Largecap():
    print("\n This All Stocks Are Low Cap Stocks")
    # This Function Is For Low Cap Stock
    nse = Nse()
    for i in  stock_list:
        quote = nse.get_quote(i);

        l52 = quote["low52"];   
        h52 = quote["high52"];
        cur_val = quote["lastPrice"];
        if(cur_val <= 1.10 * l52):
            print(i+": "+ "low52: "+ str(l52) + " high52: " + str(h52) + " cur_val: " + str(cur_val))
        # print(quote)
    
def checkhigh_Largecap():
    print("\n This All Stocks Are High Cap Stocks")
    nse = Nse()
    for i in stock_list:
        quote = nse.get_quote(i)  
    
        lo52= quote["low52"]
        hi52= quote["high52"]
        cur_val= quote["lastPrice"]

        if(cur_val >= 0.9 * hi52):
              print(i+": "+ "low52: "+ str(lo52) + " high52: " + str(hi52) + " cur_val: " + str(cur_val))
    # print(quote)

if __name__ == '__main__':

    checklow_Largecap()
    checkhigh_Largecap()
