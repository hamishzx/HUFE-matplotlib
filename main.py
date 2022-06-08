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


# 2号折线图
avg_plot = [0, 0, 0]

for species in data['species'].unique():
    for i in range(50):
        avg_plot[species] += data['sepal_size'][i + species * 50]

# 平均数
for i in range(3):
    avg_plot[i] /= 50
    avg_plot[i] = round(avg_plot[i], 2)

pl.subplot(2, 2, pos)
pl.plot(data['species'].unique(), avg_plot)
for a, b in zip(data['species'].unique(), avg_plot):
    pl.text(a, b, b, ha='center', va='bottom', fontsize=20)
pl.xticks([0, 1, 2])
pl.title("萼片大小平均值与种类关系 - 折线图")
pl.xlabel("种类")
pl.ylabel('萼片大小平均值 (cm²)')
pos += 1

# 3号条形图
avg_bar = [0, 0, 0]

for species in data['species'].unique():
    for i in range(50):
        avg_bar[species] += data['petal_size'][i + species * 50]

# 平均数
for i in range(3):
    avg_bar[i] /= 50
    avg_bar[i] = round(avg_bar[i], 2)

pl.subplot(2, 2, pos)
pl.bar(data['species'].unique(), avg_bar)
for a, b in zip(data['species'].unique(), avg_bar):
    pl.text(a, b, b, ha='center', va='bottom', fontsize=20)
pl.xticks([0, 1, 2])
pl.title("花瓣大小平均值与种类关系 - 条形图")
pl.xlabel("种类")
pl.ylabel('花瓣大小平均值 (cm²)')
pos += 1

# 4号饼状图
sum_pie = [0, 0, 0]

for species in data['species']:
    sum_pie[species] += 1

pl.subplot(2, 2, pos)
pl.pie(sum_pie,
       labels=[0, 1, 2],
       autopct='%.2f%%'
       )
pl.title("种类占比 - 饼状图")

pl.savefig("Figure.png", dpi=200)
pl.show()
