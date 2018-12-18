import matplotlib.pyplot as plt
import numpy as np
import matplotlib

data_file_path = "I:/froex_trainning/EURUSD.txt"

f = open(data_file_path, 'r')
lines = f.readlines()
f.close()

data_init = []
for i in range(1, len(lines)):
    data_init.append(float(lines[i].split(',')[4]))

data = data_init[-700::1]
"""
绘制直方图
data:必选参数，绘图数据
bins:直方图的长条形数目，可选项，默认为10
facecolor:长条形的颜色
edgecolor:长条形边框的颜色
alpha:透明度
"""
plt.hist(data, bins=40, facecolor="blue", edgecolor="black", alpha=0.7)
# 显示横轴标签
plt.xlabel("price")
# 显示纵轴标签
plt.ylabel("times")
# 显示图标题
plt.title("his")

print("AVG:", np.average(data))
print("STD:", np.std(data))
plt.show()
