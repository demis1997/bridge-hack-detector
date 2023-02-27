import requests
import json

# API endpoints
L1_API_ENDPOINT = 'https://api.etherscan.io/api'
L2_API_ENDPOINT = 'https://api-optimistic.etherscan.io/api'

# API keys
ETHERSCAN_API_KEY = 'UX33KV3H6CNV4KEG3J2EWG6BY9E4WRVKKG'

# Sample transaction hashes
L1_TX_HASH = '0xabcdef0123456789'
L2_TX_HASH = '0x0123456789abcdef'

# Retrieve layer 1 transaction data
l1_params = {
    'module': 'transaction',
    'action': 'gettxreceiptstatus',
    'txhash': L1_TX_HASH,
    'apikey': ETHERSCAN_API_KEY,
}
l1_response = requests.get(L1_API_ENDPOINT, params=l1_params)
l1_data = json.loads(l1_response.text)

# Retrieve layer 2 transaction data
l2_params = {
    'module': 'transaction',
    'action': 'gettxreceiptstatus',
    'txhash': L2_TX_HASH,
    'apikey': ETHERSCAN_API_KEY,
}
l2_response = requests.get(L2_API_ENDPOINT, params=l2_params)
l2_data = json.loads(l2_response.text)

# Compare wallet addresses
l1_wallet = l1_data['result']['from']
l2_wallet = l2_data['result']['from']
if l1_wallet.lower() == l2_wallet.lower():
    print('Wallet addresses match')
else:
    print('Wallet addresses do not match')