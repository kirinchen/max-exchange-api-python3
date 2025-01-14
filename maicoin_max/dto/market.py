from typing import List
from datetime import datetime, timedelta

from maicoin_max.utils import reflection_util


class Candlestick:

    def __init__(self, period: int, v_list: List[float]):
        self.openAt = datetime.fromtimestamp(v_list[0])
        self.closeAt = self.openAt + timedelta(seconds=period * 60)
        self.open = v_list[1]
        self.high = v_list[2]
        self.low = v_list[3]
        self.close = v_list[4]
        self.volume = v_list[5]


class Trade:

    def __init__(self, price: str, volume: str, funds: str, **kwargs):
        """
                {'id': 35999070, 'price': '1064830.0', 'volume': '0.001613', 'funds': '1717.5', 'market': 'btctwd',
         'market_name': 'BTC/TWD', 'created_at': 1646029285, 'created_at_in_ms': 1646029285402, 'side': 'bid'}
        """
        self.id: int = None
        self.price: float = float(price)
        self.volume = float(volume)
        self.funds = float(funds)
        self.market: str = None
        self.market_name: str = None
        self.created_at: int = None
        self.created_at_in_ms: int = None
        self.side: str = None
        reflection_util.merge(kwargs, self)


class MarketInfo:

    def __init__(self, **kwargs):
        """
  {
    "id": "btctwd",
    "name": "BTC/TWD",
    "base_unit": "btc",
    "base_unit_precision": 5,
    "min_base_amount": 0.0015,
    "quote_unit": "twd",
    "quote_unit_precision": 1,
    "min_quote_amount": 26
  }
        """
        self.id: str = None
        self.name: str = None
        self.base_unit: str = None
        self.base_unit_precision: int = None
        self.min_base_amount: float = None
        self.quote_unit: str = None
        self.quote_unit_precision: int = None
        self.min_quote_amount: int = None
        reflection_util.merge(kwargs, self)
