from array import *

array1 = array('i',[10,20,30,40,50])

# menambahkan index 1 angka 60
array1.insert(1,60)
print(array1)

# menghapus angka 40
array1.remove(40)
print(array1)

# for x in array1:
#     print(x)

# mencari index yang ditulis
print(array1.index(50))

# menambahkan index
array1[4] = 60
print(array1)

# menentukan nilai random
Days=set(['a','b','c','d','e','f'])
Monts =set(['ab','bc','cd'])
Dates =set ([1,23,45,2,100])
print(Days)
print(Monts)
print(Dates)

# menggunakan kurng kurawal
himpunan_mhsuniss = {'faqih','ageng','filla','viki'}
print(himpunan_mhsuniss)

# mengoversi list kedalam set 
himpunan_buah = set(['mangga','apel','jeruk','melon'])
print(himpunan_buah)

# set dengan tipe data yang berbeda-beda
set_campuran = {'menulis','hewan',5,True,('A','B')}
print(set_campuran)

# menambahkan set baru
print('menambahkan set baru')
himpunan_abjad = {'a','b','c'}

# menambahkan satu satu
himpunan_abjad.add('d')
himpunan_abjad.add('e')

# menambahkan lebih dari satu anggota sekaligus 
himpunan_abjad.update({'f','g'})
# bisa juga menggunakan list
himpunan_abjad.update(['h','i'])
print(himpunan_abjad)
