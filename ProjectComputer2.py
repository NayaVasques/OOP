"""

Object-Oriented Programming

"""

class Computer:
    monitor = 1
    
    def __init__(self, brand, hdd_size, ram_size, system, price, discount, discount_price=None):
        self.brand = brand
        self.hdd_size = hdd_size
        self.ram_size = ram_size
        self.system = system
        self.price = price
        self.discount = discount
        self.discount_price = discount_price
        self.CPU_cores = 5
        
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
            return f"{self.brand} computer with {self.hdd_size}GB HDD, {self.ram_size}GB RAM, {self.system} system, {self.CPU_cores} cores, priced at ${self.price} with {self.discount}% discount, discounted price: ${self.discount_price}."
        else:
            return f"{self.brand} computer with {self.hdd_size}GB HDD, {self.ram_size}GB RAM, {self.system} system, {self.CPU_cores} cores, priced at ${self.price} with {self.discount}% discount."



C01 = Computer.with_discount('Dell', 500, 16, 'Windows', 1000, 10)
C02 = Computer.with_discount_price('Lenovo', 256, 8, 'Linux', 800, 750)
C03 = Computer('HP', 1000, 32, 'Windows', 1500, 15, 1275)

C01.set_cores(7)
C02.set_cores(3)

print(C01.current_CPU_cores())  # Output: 7
print(C02.current_CPU_cores())  # Output: 3

print(C03.monitor)  # Output: 1

print(C01)  # Output: Dell computer with 500GB HDD, 16GB RAM, Windows system, 7 cores, priced at $1000 with 10% discount.
print(C02)  # Output: Lenovo computer with 256GB HDD, 8GB RAM, Linux system, 3 cores, priced at $800 with 0% discount, discounted price: $750.
print(C03)  # Output: HP computer with 1000GB HDD, 32GB RAM, Windows system, 5 cores, priced at $1500 with 15% discount, discounted price: $1275.



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
            return f"{self.brand} computer with {self.hdd_size}GB HDD, {self.ram_size}GB RAM, {self.system} system, {self.CPU_cores} cores, priced at ${self.price} with {self.discount}% discount, discounted price: ${self.discount_price}."
        else:
            return f"{self.brand} computer with {self.hdd_size}GB HDD, {self.ram_size}GB RAM, {self.system} system, {self.CPU_cores} cores, priced at ${self.price} with {self.discount}% discount."


def create_computer():
    brand = input("Enter brand: ")
    hdd_size = int(input("Enter HDD size (GB): "))
    ram_size = int(input("Enter RAM size (GB): "))
    system = input("Enter system: ")
    price = int(input("Enter price: "))
    discount = int(input("Enter discount: "))
    C = Computer.with_discount(brand, hdd_size, ram_size, system, price, discount)
    print("Computer added.")
    return C

def display_all_computers(computers):
    for c in computers:
        print(c)
        
def display_affordable_computers(computers, max_price=1500):
    affordable_computers = [c for c in computers if c.discount_price is not None and c.discount_price <= max_price]
    for c in affordable_computers:
        print(c)


def main():
    while True:
        print("What do you want to do?")
        print("1. Enter new computers.")
        print("2. Display all computers.")
        print("3. Display all computers under $1,500.")
        print("4. Quit.")
        choice = input("Please enter your choice: ")
        
        if choice == "1":
            C = create_computer()
        elif choice == "2":
            display_all_computers(Computer.computers)
        elif choice == "3":
            display_affordable_computers(Computer.computers)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    

if __name__ == '__main__':
