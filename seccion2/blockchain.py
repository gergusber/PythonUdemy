blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(item, last_transaction=[1]):
    blockchain.append([last_transaction, item])


def print_blockchain():
    print(blockchain)


add_value(5.90)
add_value(5.2, get_last_blockchain_value())
add_value(5.4, get_last_blockchain_value())

print_blockchain()
