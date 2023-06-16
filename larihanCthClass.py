# membuat class matematika 
# 4 parameter description
# 3 fungsi 
#  penjumlahan 2 parameter (5,6) = 11
#  perkalian 3 parameter (3,2,1) = 6
#  pengurangan 4 parameter (10,3,2,1) = 5

class Matematika:
    def __init__(self, angka1, angka2, angka3, angka4):
        self.angka1 = angka1
        self.angka2 = angka2
        self.angka3 = angka3
        self.angka4 = angka4

    def penjumlahan(self, a, b):
        result = a + b
        return result

    def perkalian(self, a, b, c):
        result = a * b * c
        return result

    def pengurangan(self, a, b, c, d):
        result = a - b - c - d
        return result


operasi = Matematika('angka1', 'angka2', 'angka3', 'angka4')
hasil_penjumlahan = operasi.penjumlahan(5, 6)
hasil_perkalian = operasi.perkalian(3, 2, 1)
hasil_pengurangan = operasi.pengurangan(10, 3, 2, 1)

print(f"Hasil Penjumlahan : {hasil_penjumlahan}")
print(f"Hasil Perkalian : {hasil_perkalian}")
print(f"Hasil Pengurangan : {hasil_pengurangan}")
