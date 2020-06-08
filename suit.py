import random
print('selamat datang di permainan suit')
print('Pilih gunting / batu / kertas')

while True:
    # while True:
    #     try:
    #         jawaban = int(input('masukkan pilihan anda:'))
    #         if jawaban != '0' and  jawaban != '1' and jawaban  != '2':
    #             print("inputnya 0,1,2 anjg")
    #         break
    #     except:
    #         print ('Angka 0,1,2 Anjg')

    while True:
        try:
            jawaban = input('masukkan pilihan anda:')
            if jawaban != 'gunting' and  jawaban != 'batu' and jawaban  != 'kertas':
                print("inputnya gunting, batu, kertas anjg")
            break
        except:
            print ('inputnya gunting, batu, kertas anjg')
            break

    pilihan_komputer = random.randint(0,3)
    if pilihan_komputer == 0:
        print ('pilihan piton gunting')
    elif pilihan_komputer == 1:
        print ('pilihan piton batu')
    elif pilihan_komputer == 2:
        print ('pilihan piton kertas')

    #if int(jawaban) == 0:
    if jawaban == 'gunting':
        if pilihan_komputer == 0:
            print('seri')
        elif pilihan_komputer == 1:
            print('Kamu Kalah')
        elif pilihan_komputer == 2:
            print('Kamu menang')
    #if int(jawaban) == 1:
    if jawaban == 'batu':
        if pilihan_komputer == 0:
            print('kamu menang')
        elif pilihan_komputer == 1:
            print('seri')
        elif pilihan_komputer == 2:
            print('kamu kalah')
    #if int(jawaban) == 2:
    if jawaban == 'kertas':
        if pilihan_komputer == 0:
            print('kamu kalah')
        elif pilihan_komputer == 1:
            print('Kamu menang')
        elif pilihan_komputer == 2:
            print('seri')   
    try:
        choice = input('Mau main lagi (yes/no)?:')
        if choice == 'yes':
            print('oke')
            continue
        else:
            print('Have a nice day!!')
            break
    except:
        break