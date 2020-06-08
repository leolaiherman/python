username1 = 'leo'
password1 = 12345
username2 = 'duE'
password2 = 321

print('Kesempatan lu buat masukin password hanya 3 kali salah')
for x in range(3):
    try:
        masukin =input('Masukin username lu:')
        passwords = int(input('Masukin password lu:'))
        if masukin == username1 and passwords == password1:
            print('oke kamu benar, silahkan masuk')
            break
        elif masukin == username2 and passwords == password2:
            print('oke kamu benar, silahkan masuk')
            break
        else:
            print('username/password lu salah goblok')
    except:
        print('masukin yang bener')
print('GoBLOK')