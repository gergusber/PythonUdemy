blockchain = []


def get_last_blockchain_value():
    """Returns the list of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=None):
    """Append new value as well as the last blockchain value to the block

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction.
    """

    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def print_blockchain():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)


def get_transaction_value():
    return float(input('Your transaction amount please: '))


def get_user_choice():
    return input('Make a choice please: ')

def verify_chain():
    is_valid = True
    block_index = 0

    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == block[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


while True:
    print('Choose:')
    print('1- for add new transaction value')
    print('2- for output blockchain blocks')
    print('3- for break')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain()
    elif user_choice == 'q':
        break
    else:
        print('input is invalid')

    if not verify_chain():
        print('Invalid Blockchain')
        break
else:
    print('User left')

print('Done')
