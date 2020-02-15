from web3 import Web3,HTTPProvider
url="https://mainnet.infura.io/v3/2013927bf7434d74af7ee38e7137249e"
web31=Web3(HTTPProvider(url))
print(web31.isAddress(url))


