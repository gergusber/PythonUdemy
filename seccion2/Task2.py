
Names = ['German', 'Bruno', 'Camila', 'Maru']


for i in range(len(Names)):
    name = Names[i]
    amount_letters = len(name)
    print(f'the name: {name}, has {amount_letters} letters')
    if amount_letters > 5:
        print(f'the name: {name}, has more than 5 letters')
    
    if 'n' in name or 'N' in name:
        print(f'the name: {name}, has n or N')

while True:
    if len(Names) > 0:
        print(f'Remove {Names[0]}')
        Names.pop(0)
    else:
        break
