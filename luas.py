class Luas():

    def __init__(self):
        self.panjang = int(input('masukin panjang persegi panjang lu (cm):'))
        self.lebar   = int(input('masukin lebar persegi panjang lu (cm):'))
        # def luas (self):
        self.luas = self.panjang * self.lebar
    
    def kalimat (self):
        return f'Jadi luas persegi panjang lu adalah {self.luas} cm persegi'

a = Luas()
print (a.kalimat())