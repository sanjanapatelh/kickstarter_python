from  abi import *

def validation(contract_address,my_address):
    address = web3.toChecksumAddress(contract_address)
    my_address = web3.toChecksumAddress(my_address)
    contract =web3.eth.contract(address=address,abi=abi1)
    if my_address!=contract.functions.manager().call():
        return False
    else:
        return True


def createRequest(description,value,recipient,contract_address):
    contract =web3.eth.contract(address=contract_address,abi=abi1)
    recipient_address = web3.toChecksumAddress(recipient)
    tx_hash=contract.functions.createRequest(description,value,recipient_address).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)

def finalizeRequest(index_value,contract_address):
    contract =web3.eth.contract(address=contract_address,abi=abi1)
    tx_hash=contract.functions.finalizeRequest(index_value).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)

def getSummary(contract_address):
    contract =web3.eth.contract(address=contract_address,abi=abi1)
    return contract.functions.getSummary().call()

def request_details(index_value,contract_address):
    contract =web3.eth.contract(address=contract_address,abi=abi1)
    return contract.functions.requests(index_value).call()
