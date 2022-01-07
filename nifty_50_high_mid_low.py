from nsetools import Nse

stock_list = ["ACC","ADANIENT","ADANIGREEN","ADANIPORTS","ADANITRANS","ALKEM","AMBUJACEM","APOLLOHOSP","AUROPHARMA","DMART","BAJAJHLDNG","BANDHANBNK","BERGEPAINT","BIOCON","BOSCHLTD","CADILAHC","CIPLA","CHOLAFIN","COLPAL","DLF","DABUR","GAIL","GLAND","HDFCAMC","HAVELLS","HINDPETRO","ICICIGI","ICICIPRULI","IGL","INDUSTOWER","NAUKRI","INDIGO","JINDALSTEL","JUBLFOOD","LTI","LUPIN","MARICO","MUTHOOTFIN","NMDC","PIIND","PIDILITIND","PEL","PGHH","PNB","SBICARD","SIEMENS","SAIL","TORNTPHARM","MCDOWELL-N","VEDL","YESBANK"]

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
