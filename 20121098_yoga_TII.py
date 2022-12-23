# Tugas terstruktur II 

# Jawaban Soal pertama

nama_mhs = {
    'NIM' : '20121098',
    'Nama' : 'Yoga Bagas Kurniawan',
    'Kelas' : 'TI 3 A',
    'Alamat' : 'Jalan urip sumoharjo pringlangu Gg 3 Pekalongan'
}

print('nama_mhs = ',nama_mhs)

# Jawaban soal kedua

print('-----------------------------------------------------------')
print('       Aplikasi sederhan menggunakan String dan Array      ')
print('-----------------------------------------------------------')
print('NIM    : ',nama_mhs['NIM'])
print('Nama   : ',nama_mhs['Nama'])
print('Kelas  : ',nama_mhs['Kelas'])
print('Alamat : ',nama_mhs['Alamat'])
print('----------------------------------------------------------')

# Jawaban soal ketiga

kalimat = ['UNISS','di','belajar','pada','Mahasiswa','data','ruang','lab','struktur','semester','tema','Array','String','dan','di','dengan','Batang','3']

# Mahasiswa semester 3 di UNISS Batang belajar struktur data pada ruang lab dengan tema String dan Array

print(kalimat[4],kalimat[9],kalimat[17],kalimat[1],kalimat[0],kalimat[16],kalimat[2],kalimat[8],kalimat[5],kalimat[3],kalimat[6],kalimat[7],kalimat[15],kalimat[10],kalimat[12],kalimat[13],kalimat[11])

# jawaban soal nomer keempat

from array import *
Nilai = array('i',[1,3,4,5,10,15,20])

print('-------------------------------------------------')
print('    Aplikasi Sederhan menggunakan Array          ')
print('-------------------------------------------------')
print(Nilai[4], ' + ',Nilai[1], ' x ', Nilai[5], ' = ',Nilai[4]+Nilai[1]*Nilai[5])
print(Nilai[1], ' x ',Nilai[2], ' : 2 = ',Nilai[1]*Nilai[2]/2)
print(Nilai[5],'^2 x ',Nilai[1], ' + ',Nilai[3],' = ',Nilai[5]**2 *Nilai[1]+Nilai[3])
print(Nilai[5], ' - ',Nilai[3], ' x ', Nilai[2], ' = ',Nilai[5]-Nilai[3]*Nilai[2])

