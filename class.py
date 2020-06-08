class Flower:
    def __init__(self):
        self.name = nama_bunga
        self.petals_number = banyak_kelopak
        self.price = harga_bunga
    
    def kalimat (self):
            return f'Jadi nama bunganya adalah bunga {self.name} punya{self.petals_number} kelopak, harganya {self.price} '

# a = Flower()
# print(a.kalimat())

while True:
    nama_bunga = input('Masukin nama bunganya:')
    banyak_kelopak = int(input('Masukin banyak kelopaknya:'))
    harga_bunga = int(input('Masukin harga bunganya:'))

    another = input('mau tambah bunga lagi? (yes/no):')
    if another == 'yes':
        continue
    else:
        break

a = Flower()
print(a.kalimat())
