import random
while True:
    angka = random.randint(0,11)
    while True:
        try:
            a = int(input('Berapa besar hidung Keane (cm) dalam range (1 - 10):'))
            if int(a) > angka:
                print ('Kegedean, lu kira Gajah')
            elif int(a) < angka:
                print ('Kekecilan ')
            elif int(a) == angka:
                print ('Selamat kamu gabut')
                break         
        except:
            print('pilihanny 1-10')
            break
#    while True:
    choice = input('mau main lagi? (yes/no):')
    if choice == 'yes':
        print('lanjut')
        
    elif choice == 'no':
        print('ok have a nice day')
        break
    else:
        print('pilihannya yes or no Goblok')