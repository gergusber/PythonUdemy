genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'German'
participants = {'German'}

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
    participants.add(sender)
    participants.add(recipient)



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


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def verify_chain():
    for (index, block) in enumerate(blockchain):
        if(index == 0):
            continue  #the genesis block

        if(block['previous_hash'] != blockchain[index-1]):
            return False
    return True



def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print(hashed_block)

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
    print('5-  output participants')

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
    elif user_choice == '5':
        print(participants)
    elif user_choice == 'q':
        break
    elif user_choice == 'h':
        if(len(blockchain)>=1):
            blockchain[0]={
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender':'CRIS', 'recipient': 'German', 'amount': 100}]
            }
    else:
        print('input is invalid')
    if not verify_chain():
        print_blockchain()
        print('invalid blockchain')
else:
    print('User left')

print('Done')
