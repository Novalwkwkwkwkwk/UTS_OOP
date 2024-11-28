class Laptop:
   
    merk = ""
    ram = 0  
    processor = ""

    def info(self):
        print(f"Laptop {self.merk} dengan RAM {self.ram}GB dan prosesor {self.processor}.")

laptop1 = Laptop()
laptop1.merk = "Dell"
laptop1.ram = 16
laptop1.processor = "Intel Core i7"

laptop2 = Laptop()
laptop2.merk = "Asus"
laptop2.ram = 8
laptop2.processor = "AMD Ryzen 5"

laptop1.info()  
laptop2.info()  
