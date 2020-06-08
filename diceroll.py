import random
print('=================')
print('DICE ROLL SIMULATOR')
print('=================')
while True:
    choice = input('Wanna Roll?(yes/no):')
    acak = random.randint(1,7)
    try:
        if choice == 'yes':
            print(f'You have rolled {acak}')
            print('Oke Bye!!!')
            
        else:
            print('Pilihannya yes/no anjg')
            continue
    except:
        print('Pilihannya yes/no anjg')
        continue
    try:
        choice = input('Mau main lagi (yes/no)?:')
        if choice == 'yes':
            print('oke')
            continue
        else:
            print('Oke Bye!!! Have a nice day')
            break
    except:
        break

