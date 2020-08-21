from abi import *

contract =web3.eth.contract(address=address,abi=abi)


def display():
    return contract.functions.getDeployedCampaigns().call()
