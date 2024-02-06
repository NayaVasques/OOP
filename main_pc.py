'''

Author: Nayara

'''

from ProjectComputer import Computer

def create_computer():
    brand = input("Please, enter the brand: ")
    hdd_size = int(input("Now enter the HDD size (GB): "))
    ram_size = int(input("Enter RAM size (GB): "))
    system = int(input("And now enter the system architecture: "))
    price = int(input("What is the price: "))
    discount = int(input("Has some discount: "))
    C = Computer.with_discount(brand, hdd_size, ram_size, system, price, discount)
    print("Computer added with sucess.")
    return C

def display_all_computers(computers):
    for c in computers:
        print(c)
        
def display_cheap_computers(computers, max_price=1500):
    cheap_computers = [c for c in computers if c.discount_price is not None and c.discount_price <= max_price]
    for c in cheap_computers:
        print(c)


def main():
    while True:
        print("What do you want to do?")
        print("1. Enter new computers.")
        print("2. Display all computers.")
        print("3. Display all computers under $1,500.")
        print("4. Quit.")
        choice = input("Please, enter your choice: ")
        
        if choice == "1":
            C = create_computer()
        elif choice == "2":
            display_all_computers(Computer.computers)
        elif choice == "3":
            display_cheap_computers(Computer.computers)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("It is not a valid number. Please try again.")

if __name__ == '__main__':
    main()
    

