class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        # Initialize a new credit card account
        self.customer = customer
        self.bank = bank
        self.account = acnt
        self.limit = limit
        self.balance = 0  

    def get_customer(self):
        # Return the customer's name
        return self.customer

    def get_bank(self):
        # Return the bank's name
        return self.bank

    def get_account(self):
        # Return the account number
        return self.account

    def get_limit(self):
        # Return the credit limit
        return self.limit

    def get_balance(self):
        # Return the current balance
        return self.balance

    def charge(self, price):
        # Charge the given price to the card if within the limit
        if price + self.balance > self.limit:
            return False  # Charge denied
        else:
            self.balance += price
            return True  # Charge accepted

    def make_payment(self, amount):
        # Reduce balance by the given payment amount
        self.balance -= amount
