from nsetools import Nse

def checklow_Largecap(stk):
    nse = Nse()
    quote = nse.get_quote(stk);
    l52 = quote["low52"];
    h52 = quote["high52"];
    cur_val = quote["lastPrice"];
    if(cur_val <= 1.10 * l52):
        print(l52 + "\t" + h52 + "\t" + cur_val)



checklow_Largecap('infy')
