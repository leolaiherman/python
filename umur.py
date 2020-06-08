import datetime

print('\n SELAMAT DATANG DI KALKULATOR UMUR\n')

tanggal = int(input('Tanggal Berapakah anda lahir? :'))
bulan = int(input('Bulan apakah anda lahir? :'))
tahun  = int(input('Anda lahir tahun berapa? :'))

tanggals = datetime.date.today()
years = tanggals.year - tahun
months = tanggals.month - bulan
days = tanggals.day - tanggal

if months < 0 or days < 0:
    #years -= 1
    print(f'Jadi Umur anda sekarang adalah {abs(years)} tahun, kurang {abs(months)} bulan, kurang {abs(days)} hari')

elif months > 0 or days > 0:
    print(f'Jadi Umur anda sekarang adalah {abs(years)} tahun, lebih {abs(months)} bulan, lebih {abs(days)} hari')

elif months == 0 or days == 0:
    print(f'Happy {years} Birthday!!!')



