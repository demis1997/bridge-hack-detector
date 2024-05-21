import pip._vendor.requests 
from requests import get
from datetime import datetime

#NOTE: It may take up to 7 days for a transaction to go through, I did not add a limit of 7 days and this could trigger falsely due to delays on the smart contracts' side but I have not tested it and may not end up being the case


API_KEY = "my secret key"
address = "0x99C9fc46f92E8a1c0deC1b1747d010903E884bE1"
BASE_URL = "https://api.etherscan.io/api"
OPT_BASE_URL = "https://api-optimistic.etherscan.io/api"

def make_api_url(module, action, address , **kwargs):
    url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={API_KEY}"

    for key, value in kwargs.items():
        url+= f"&{key}={value}"

        return url

def get_normal_transactions(address):
    get_normal_transactions_url = make_api_url("account", "txlist", address, startblock=0, endblock = 99999999, page=1, offset = 10000, sort="asc")
    response = get(get_normal_transactions_url)
    normaltransactions = response.json()["result"]
    get_internal_transactions_url = make_api_url("account", "txlistinternal", address, startblock=0, endblock = 2702578, page=1, offset = 10000, sort="asc")
    response2 = get(get_internal_transactions_url)
    internaltransactions = response2.json()["result"]
    get_erc20_transactions_url = make_api_url("account", "tokentx", address, startblock=0, endblock = 27025780, page=1, offset = 10000, sort="asc")
    response3 = get(get_erc20_transactions_url)
    erc20transactions = response3.json()["result"]   

    # Just to show the wallet from and to address and  timestamp for normal transactions
    for tx in normaltransactions:
        to = tx["to"]
        from_addr = tx["from"]
        time = datetime.fromtimestamp(int(tx['timeStamp']))
        print ("To:", to)
        print ("From:", from_addr)
        print ("Time:", time)

     # Just to show the wallet from and to address and  timestamp for internal transactions
    for tx in internaltransactions:
        to = tx["to"]
        from_addr = tx["from"]
        time = datetime.fromtimestamp(int(tx['timeStamp']))
        print ("To:", to)
        print ("From:", from_addr)
        print ("Time:", time)

    # Just to show the wallet from and to address and  timestamp for erc20 transactions
    for tx in erc20transactions:
        to = tx["to"]
        from_addr = tx["from"]
        time = datetime.fromtimestamp(int(tx['timeStamp']))
        print ("To:", to)
        print ("From:", from_addr)
        print ("Time:", time)
   
    if tx in internaltransactions != tx in normaltransactions: 
        print ("Withdrawal without deposit") 

    elif tx in erc20transactions != tx in normaltransactions: 
        print ("Cannot find tx") 
    
    elif from_addr in erc20transactions != from_addr in normaltransactions: 
        print ("New Address found") 
    
    elif to in internaltransactions != from_addr in normaltransactions: 
        print ("New EOA") 
    else: 
        print ("We are still good")
    
get_normal_transactions(address)


