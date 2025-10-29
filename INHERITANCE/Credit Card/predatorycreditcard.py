from creditcard import CreditCard
class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance."""
        super().__init__(customer, bank, acnt, limit)
        self.apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit."""
        success = super().charge(price)
        if not success:
            self.balance += 5  # assess penalty
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self.balance > 0:
            monthly_factor = pow(1 + self.apr, 1 / 12)
            self.balance *= monthly_factor
