blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(item, last_transaction=None):
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, item])


def print_blockchain():
    print(blockchain)


def get_transaction_value():
    return float(input('Your transaction amount please: '))


def get_user_choice():
    return int(input('Make a choice please: '))


tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('Coose:')
    print('1- for add new transaction value')
    print('2- for output blockchain blocks')
    user_choice = get_user_choice()

    if(user_choice == 1 ):
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
        for block in blockchain:
            print('outputting block')
            print(block)
    else:
        print_blockchain()

