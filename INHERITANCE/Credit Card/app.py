from creditcard import CreditCard
from predatorycreditcard import PredatoryCreditCard
class App:
    def run(self):
        wallet = []

        wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
        wallet.append(CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500))
        wallet.append(CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000))
        wallet.append(PredatoryCreditCard('John Bowman', 'California Predatory', '5489 0399 1122 3344', 3000, 0.0825))

        for val in range(1, 17):
            wallet[0].charge(val)
            wallet[1].charge(2 * val)
            wallet[2].charge(3 * val)
            wallet[3].charge(2.5 * val)

        for card in wallet:
            print("Customer:", card.get_customer())
            print("Bank:", card.get_bank())
            print("Account:", card.get_account())
            print("Limit:", card.get_limit())
            print("Balance:", round(card.get_balance(), 2), "\n")

        if isinstance(card, PredatoryCreditCard):
            card.process_month()
            print("Balance after interest:", round(card.get_balance(), 2))

        while card.get_balance() > 100:
            card.make_payment(100)
            print("New balance after payment:", round(card.get_balance(), 2))
        print()
