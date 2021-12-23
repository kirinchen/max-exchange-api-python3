class Position:

    def __init__(self, currency: str, balance: float, locked: float, type: str, **kwargs):
        self.currency: str = currency
        self.balance: float = balance
        self.locked: float = locked
        self.type: str = type
