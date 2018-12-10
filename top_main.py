import initial_encapsulation.wrapper_redefine
import initial_encapsulation.contract_and_order

# 账户设置
account = "DU859178"
contract = initial_encapsulation.contract_and_order.contract_EURUSD()

# 交易主体实例化
my_app = initial_encapsulation.wrapper_redefine.QuantBody(contract, account)

# 启动client与TWS/IB Gateway之间的链接
my_app.connect("127.0.0.1", 7496, clientId=0)

# 提交request
my_app.reqMktData(110, contract, "221", False, False, [])

# 开始对TWS/IB Gateway的监听
my_app.run()
