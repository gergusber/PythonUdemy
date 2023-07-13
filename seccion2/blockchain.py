blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(item, last_transaction=None):
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, item])


def print_blockchain():
    print(blockchain)


def get_user_input():
    return float(input('Your transaction amount please: '))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())


tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print_blockchain()
