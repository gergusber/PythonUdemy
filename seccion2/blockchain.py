blockchain = [[1]]


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(item):
    blockchain.append([get_last_blockchain_value(), item])


def print_blockchain():
    print(blockchain)


add_value(5.2)
add_value(5.4)

print_blockchain()
