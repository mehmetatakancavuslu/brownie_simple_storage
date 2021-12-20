from brownie import accounts, SimpleStorage


def deploy_simple_storage():
    # Local Ganache account
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Real test account with brownie encrypted
    # account = accounts.load("test-account")
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    # Wait for transaction to confirm
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    deploy_simple_storage()
