class Wallet:

    def __init__(self, currency: str, balance: str, locked: str, type: str, **kwargs):
        self.currency: str = currency
        self.balance: float = float(balance)
        self.locked: float = float(locked)
        self.type: str = type
