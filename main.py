from matplotlib import pyplot as pl
import pandas as pd

# 从iris.csv读取数据
data = pd.read_csv("iris.csv")
# 中文显示
font = {'family': 'SimSun',
        'weight': 'bold',
        'size': '16'}
pl.rc('font', **font)
pl.rc('axes', unicode_minus=False)
# 计算萼片和花瓣大小，为散点图做数据准备
data["sepal_size"] = data["sepal_length (cm)"] * data["sepal_width (cm)"]
data["petal_size"] = data["petal_length (cm)"] * data["petal_width (cm)"]
# 定义画图区域，准备画布，并确定画图位置
pl.figure(figsize=(20, 15))
pos = 1
# 1号散点图，alpha值为点的透明度，color即点的颜色
pl.subplot(2, 2, pos)
pl.scatter(data['sepal_size'], data['petal_size'], alpha=0.8, color="red")
# x和y轴标签
pl.xlabel("萼片大小 (cm²)")
pl.ylabel('花瓣大小 (cm²)')
pl.title("萼片大小与花瓣大小的关系 - 散点图")
pos += 1


pl.savefig("Figure.png", dpi=200)
pl.show()
