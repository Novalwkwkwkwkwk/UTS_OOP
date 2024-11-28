class Hewan:
    def suara(self):
        print("Hewan mengeluarkan suara.")

class Kucing(Hewan):
    def suara(self):
        print("Kucing mengeong.")

class Anjing(Hewan):
    def suara(self):
        print("Anjing menggonggong.")

hewan = Hewan()
kucing = Kucing()
anjing = Anjing()

hewan.suara() 
kucing.suara()  
anjing.suara()  
