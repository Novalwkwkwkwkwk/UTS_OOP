class AkunBank:
    
    __nomor_rekening = ""
    __saldo = 0.0

    def get_nomor_rekening(self):
        return self.__nomor_rekening

    def set_nomor_rekening(self, nomor_rekening):
        if nomor_rekening.strip():  
            self.__nomor_rekening = nomor_rekening
        else:
            print("Nomor rekening tidak boleh kosong!")

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        if saldo >= 0:  
            self.__saldo = saldo
        else:
            print("Saldo tidak boleh negatif!")

akun = AkunBank()

akun.set_nomor_rekening("1234567890")
akun.set_saldo(500000.0)

print(f"Nomor Rekening: {akun.get_nomor_rekening()}") 
print(f"Saldo: Rp{akun.get_saldo():,.2f}")  

akun.set_saldo(-1000.0)  
