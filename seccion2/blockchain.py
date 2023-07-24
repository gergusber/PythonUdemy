genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'German'


def get_last_blockchain_value():
    """Returns the list of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender= owner, amount= 1.0):
    """Append new value as well as the last blockchain value to the block

    Arguments:
        :sender: the sender of the coins.
        :recipient: The recipient of the coins.
        :amount: the amount of coins sent(default = 1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
        }

    open_transactions.append(transaction)



def print_blockchain():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)


def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_recipient, tx_amount


def get_user_choice():
    return input('Make a choice please: ')


def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False

    return is_valid


def mine_block():
    last_block = blockchain[-1]
    hash_block = ''
    for key in last_block:
        value = last_block[key]
        hash_block = hash_block + str(value)

    print(hash_block)
    block = {
        'previous_hash': 'xyz',
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)


while True:
    print('Choose:')
    print('1- for add new transaction value')
    print('2- for output blockchain blocks')
    print('3- for break')
    print('4- mine new block')

    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print('---'*20)
        print('OpenTransactions')
        print(open_transactions)
    elif user_choice == '2':
        print_blockchain()
    elif user_choice == '4':
        mine_block()
    elif user_choice == 'q':
        break
    else:
        print('input is invalid')

else:
    print('User left')

print('Done')
