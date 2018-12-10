import ibapi.contract
import ibapi.order


def contract_EURUSD():
    # 欧元美元外汇合约
    contract = ibapi.contract.Contract()
    contract.symbol = "EUR"
    contract.currency = "USD"
    contract.secIdType = "CASH"
    contract.exchange = "IDEALPRO"
    return contract


def contract_EURJPY():
    # 欧元日元外汇合约
    contract = ibapi.contract.Contract()
    contract.symbol = "EUR"
    contract.currency = "JPY"
    contract.secIdType = "CASH"
    contract.exchange = "IDEALPRO"
    return contract


def order_limit(action:str, quantity:float, lmtPrice:float):
    # 限价单
    order = ibapi.order.Order()
    order.action = action
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = lmtPrice
    order.transmit = True
    return order


def order_stop_market(action:str, quantity:float, stopPrice:float):
    # 止损限价单
    order = ibapi.order.Order()
    order.action = action
    order.orderType = "STP LMT"
    order.totalQuantity = quantity
    order.auxPrice = stopPrice
    order.transmit = True
    return order


def order_stop_limit(action:str, quantity:float, stopPrice:float, lmtPrice:float):
    # 止损限价单
    order = ibapi.order.Order()
    order.action = action
    order.orderType = "STP LMT"
    order.totalQuantity = quantity
    order.auxPrice = stopPrice
    order.lmtPrice = lmtPrice
    order.transmit = True
    return order


def order_trail_stop_market():
    # 追踪止损市价单
    pass


def order_trail_stop_limit():
    # 追踪止损限价单
    pass
