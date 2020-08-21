from abi import *

contract =web3.eth.contract(address=address,abi=abi)

def to_contribute(contract_address,contributor,value_to_contribute):

    address = web3.toChecksumAddress(contract_address)
    small_contract=web3.eth.contract(address=contract_address,abi=abi1)
    address = web3.toChecksumAddress(contributor)
    tx_hash=small_contract.functions.contribute().transact({ 'value':value_to_contribute ,'from':address})
    web3.eth.waitForTransactionReceipt(tx_hash)

def to_approve(contract_address,contributor,index):
    small_contract=web3.eth.contract(address=contract_address,abi=abi1)
    address = web3.toChecksumAddress(contributor)
    tx_hash=small_contract.functions.approveRequest(index).transact({'from':address})
    web3.eth.waitForTransactionReceipt(tx_hash)
