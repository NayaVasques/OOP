'''

Author: Nayara

'''

class Computer:
    monitor = 1
    computers = []
    
    def __init__(self, brand, hdd_size, ram_size, system, price, discount, discount_price=None):
        self.brand = brand
        self.hdd_size = hdd_size
        self.ram_size = ram_size
        self.system = system
        self.price = price
        self.discount = discount
        self.discount_price = discount_price
        self.CPU_cores = 5
        Computer.computers.append(self)
        
    def current_CPU_cores(self):
        return self.CPU_cores
    
    def set_cores(self, CPU_cores):
        self.CPU_cores = CPU_cores
        
    def get_discount(self):
        return self.discount
    
    def set_discount(self, discount):
        self.discount = discount
    
    def set_discount_price(self, discount_price):
        self.discount_price = discount_price
        
    @classmethod
    def with_discount(cls, brand, hdd_size, ram_size, system, price, discount):
        return cls(brand, hdd_size, ram_size, system, price, discount)
    
    @classmethod
    def with_discount_price(cls, brand, hdd_size, ram_size, system, price, discount_price):
        return cls(brand, hdd_size, ram_size, system, price, None, discount_price)
    
    def __str__(self):
        if self.discount_price is not None:
            return f"The {self.brand} computer has {self.hdd_size}GB HDD, {self.ram_size}GB RAM, the system with {self.system}, {self.CPU_cores} cores, with the regular price of ${self.price}, and with {self.discount}% discount, has the discounted price of ${self.discount_price}."
        else:
            return f"The {self.brand} computer has {self.hdd_size}GB HDD, {self.ram_size}GB RAM, the system with {self.system}, {self.CPU_cores} cores, with the regular price of ${self.price}  and with {self.discount}% discount."

C01 = Computer("APPLE", 500, 16, 64, 1800.99, 10, 1620.89)
C02 = Computer("SAMSUNG", 1000, 12, 64, 2000.99, 10, 1800.99)
C03 = Computer("DELL", 1000, 8, 32, 1200.99, 12, 1056.88)
C04 = Computer("HP", 500, 8, 64, 1400.99, 15, 1190.84)

C01.set_cores(7)
C02.set_cores(3)

print(f'The current CPU cores of Computer C01 is', C01.current_CPU_cores())
print(f'The current CPU cores of Computer C02 is', C02.current_CPU_cores())

print(f'The value of the Monitor for C03 is', C03.monitor)

