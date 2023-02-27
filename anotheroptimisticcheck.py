
api_key = "UX33KV3H6CNV4KEG3J2EWG6BY9E4WRVKKG"


mint_tx_hash = "MINT_TX_HASH_HERE"


optimism_bridge_address = "0x99C9fc46f92E8a1c0deC1b1747d010903E884bE1"

# Replace with the endpoint for the Etherscan API you want to use
etherscan_endpoint = "https://api.etherscan.io/api"

# Call the Etherscan API to get the details of the mint transaction
params = {
    "module": "proxy",
    "action": "eth_getTransactionByHash",
    "txhash": mint_tx_hash,
    "apikey": api_key,
}

response = requests.get(etherscan_endpoint, params=params)
data = response.json()

# Get the "from" address of the mint transaction
mint_tx_from = data["result"]["from"]

# Call the Etherscan API to get the list of transactions sent to the Optimism bridge contract
params = {
    "module": "account",
    "action": "txlist",
    "address": optimism_bridge_address,
    "apikey": api_key,
}

response = requests.get(etherscan_endpoint, params=params)
data = response.json()

# Loop through the transactions sent to the Optimism bridge contract
for tx in data["result"]:
    # Check if the transaction is a contract creation transaction (i.e., it creates a new EOA)
    if tx["to"] == None and tx["input"] == "0x":
        # Get the "from" address of the contract creation transaction
        eoa_address = tx["from"]
        # Check if the "from" address matches the "from" address of the mint transaction
        if mint_tx_from.lower() == eoa_address.lower():
            print(f"Mint transaction {mint_tx_hash} was triggered by a new EOA for the Optimism bridge: {eoa_address}")
            break
else:
    print(f"Mint transaction {mint_tx_hash} was not triggered by a new EOA for the Optimism bridge.")