from abc import ABC, abstractmethod

# Strategy Interface
class PaymentMode(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass


# Concrete Strategy - Credit Card
class CreditCard(PaymentMode):
    def make_payment(self, amount):
        print(f"₹{amount:.2f} paid successfully using Credit Card.")


# Concrete Strategy - Debit Card
class DebitCard(PaymentMode):
    def make_payment(self, amount):
        print(f"₹{amount:.2f} paid successfully using Debit Card.")


# Concrete Strategy - UPI
class UPI(PaymentMode):
    def make_payment(self, amount):
        print(f"₹{amount:.2f} paid successfully through UPI.")


# Concrete Strategy - Net Banking
class NetBanking(PaymentMode):
    def make_payment(self, amount):
        print(f"₹{amount:.2f} paid successfully using Net Banking.")


# Context Class
class PaymentGateway:
    def __init__(self):
        self.payment_method = None

    def choose_payment(self, payment_method):
        self.payment_method = payment_method

    def pay_now(self, amount):
        if self.payment_method:
            self.payment_method.make_payment(amount)
        else:
            print("No payment method selected!")


# Main Program
gateway = PaymentGateway()

while True:
    print("\n========== Online Payment System ==========")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI")
    print("4. Net Banking")
    print("5. Exit")

    try:
        option = int(input("Select payment option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if option == 5:
        print("Exiting Payment System... Thank You!")
        break

    if option not in [1, 2, 3, 4]:
        print("Invalid option! Try again.")
        continue

    amount = float(input("Enter amount to pay: "))

    methods = {
        1: CreditCard(),
        2: DebitCard(),
        3: UPI(),
        4: NetBanking()
    }

#comments
========== Online Payment System ==========
1. Credit Card
2. Debit Card
3. UPI
4. Net Banking
5. Exit
Select payment option: 3
Enter amount to pay: 2500

₹2500.00 paid successfully through UPI.

========== Online Payment System ==========
1. Credit Card
2. Debit Card
3. UPI
4. Net Banking
5. Exit
Select payment option: 1
Enter amount to pay: 5000

₹5000.00 paid successfully using Credit Card.
    gateway.choose_payment(methods[option])
    gateway.pay_now(amount)