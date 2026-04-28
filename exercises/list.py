angka = [1, 2, 3, 4, 5]
print(angka[0])
print(angka[1])

buah = ["apel", "pisang"]
for f in buah:
    print(f)

class Orang:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
    
    def salam(self):
        print(f"Halo, {self.nama}")

class Mahasiswa(Orang):
    def __init__(self, nama, usia, nim):
        super().__init__(nama, usia)
        self.nim = nim
    
    def salam(self):
        print(f"Halo, {self.nama}, NIM: {self.nim}")

mhs = Mahasiswa("Budi", 20, "12345")
mhs.salam()
                    