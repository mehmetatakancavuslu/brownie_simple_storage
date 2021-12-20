from brownie import accounts, SimpleStorage


def deploy_simple_storage():
    # Local Ganache account
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Real test account with brownie encrypted
    # account = accounts.load("test-account")
    print(simple_storage)


def main():
    deploy_simple_storage()
