class Mahasiswa:
    nama = ""
    nim = ""
    program_studi = ""

    def info(self):
        print(f"Mahasiswa: {self.nama}, NIM: {self.nim}, Program Studi: {self.program_studi}")

class StatusMahasiswa(Mahasiswa): 
   
    def aktif(self):
        print(f"{self.nama} adalah mahasiswa aktif di program studi {self.program_studi}.")

mahasiswa1 = StatusMahasiswa()

mahasiswa1.nama = "Alan Jaya"
mahasiswa1.nim = "202311002"
mahasiswa1.program_studi = "Teknik Informatika"

mahasiswa1.info()
mahasiswa1.aktif()
