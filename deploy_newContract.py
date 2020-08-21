from abi import *

contract =web3.eth.contract(address=address,abi=abi)


def createNewContract(minimum_contribution,description,my_address):
    my_address_varified = web3.toChecksumAddress(my_address)
    tx_hash=contract.functions.createCampaign(minimum_contribution,description).transact({ 'from':my_address_varified})
    web3.eth.waitForTransactionReceipt(tx_hash)
    return contract.functions.getDeployedCampaigns().call()[-1]
