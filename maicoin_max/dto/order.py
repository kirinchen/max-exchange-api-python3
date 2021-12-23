from maicoin_max.utils import reflection_util


class Order:

    def __init__(self, **kwargs):
        self.id: int = None
        self.client_oid: str = None
        self.side: str = None
        self.ord_type: str = None
        self.price: str = None
        self.stop_price: str = None
        self.avg_price: str = None
        self.state: str = None
        self.market: str = None
        self.created_at: int = None
        self.created_at_in_ms: int = None
        self.updated_at: int = None
        self.updated_at_in_ms: int = None
        self.volume: str = None
        self.remaining_volume: str = None
        self.executed_volume: str = None
        self.trades_count: int = None
        self.group_id: int = None
        reflection_util.merge(kwargs, self)
