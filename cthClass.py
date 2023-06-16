class Bagas:
  #class atribut
  suku = 'Jawa'
  
  def __init__(self, name, age, alamat):
      self.name = name
      self.age = age
      self.alamat = alamat
      
  def biodata(self):
    return f"{self.name} is {self.age} years old"
  
  def alamatSaya(self):
    return f"Tempat tinggal {self.name} di {self.alamat}"
  
tes_bagas = Bagas('Bagas', 19, 'Pekalongan')
print(tes_bagas.biodata())
print(tes_bagas.alamatSaya())
print(tes_bagas.suku)

