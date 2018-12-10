from ibapi.wrapper import *
from ibapi.client import *
import datetime


class QuantBody(EWrapper, EClient):
    def __init__(self, contract: Contract, account: str):
        EWrapper.__init__(self)
        EClient.__init__(self, wrapper=self)

        self.contract = contract                            # 交易标的
        self.account = account                              # 账户名称

        self.next_orderID = 0                               # 下一个订单orderID
        self.orderID_ready = True                           # 为True表示orderId已经申请成功,可以直接使用
        self.lastOrderDone = True                           # 上一个订单已经成交标志位，为True表示上一订单已成交

        self.positionQuantity = 0                           # 持仓量
        self.priceAsk = 0.0                                 # 当前卖价
        self.priceBid = 0.0                                 # 当前买价
        self.realizedPnL = 0.0                              # 已实现盈利
        self.unrealizedPnL = 0.0                            # 未实现盈利

        self.long_or_short = 0                              # 初始持仓的多空方向，1多头，-1空头，0空仓
        self.long_or_short_ready = False                    # 当前持仓状态是否更新完毕标志位，完毕为1，没完毕为0

        self.last_price_time = datetime.datetime.now()      # 上一次刷新价格时间

    def nextValidId(self, orderId: int):
        EWrapper.nextValidId(self, orderId)

    def position(self, account: str, contract: Contract, position: float, avgCost: float):
        EWrapper.position(self, account, contract, position, avgCost)

    def tickPrice(self, reqId: TickerId , tickType: TickType, price: float, attrib:TickAttrib):
        EWrapper.tickPrice(self, reqId, tickType, price, attrib)
        print(reqId, price, tickType)
