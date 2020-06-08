
import time
waktu = int(input('mau berapa lama?'))
for x in range (waktu):
    print (str(waktu-x))
    if time.sleep (1):
        print('mau lanjut?(y/n):')
        if time.sleep == 'y':
            continue
        else:
            break

