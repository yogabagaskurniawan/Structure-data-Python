# awal
a=10
b=30
# perkalian = a*b
# print(perkalian)

# dictionary
nama_mhs = {
    "nama" : "YOGA BAGAS KURNIAWAN",
    "alamat" : "Pekalongan",
    "nohp" : 856
}
print('------------------------')
print('|Nama Mahasiswa | Alamat | nohp')
print('------------------------')
print(nama_mhs['nama'], nama_mhs['alamat'], nama_mhs['nohp'])
print('------------------------')

# Array
from array import *
# simbol 'i' menandakan index(tipe data)
array1 = array('i',[10,20,30,40,50])

# mengambil data array
print(array1[0])
print(array1[2])
print()

# menambahkan index
array1.insert(1,60)

print('------------------------')
perkalian = array1[1] * array1[2]
print('Hasil Perkalian antara', array1[1] , ' dan ' , array1[2], " adalah ", perkalian )
print('------------------------')

# looping pangkat 2
for x in array1:
    # print(x**2)
    result = x**2
    # print(result)
    print('Bilangan awal ',x, 'Hasil pangkatnya adalah ',result)
    
# Penjumlahan matrik A dan B
a = array("i",[10,12,13])
b = array("i",[2,4,6])

for x in a:
    for y in b:
        penjumlahan = x+y
        perkalian = x*y
        
        print (x,'+',y,'=',penjumlahan, '', x,'x',y,'=',perkalian)

