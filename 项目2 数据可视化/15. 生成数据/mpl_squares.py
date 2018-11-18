import matplotlib.pyplot as plt

# 遗留问题，中文乱码情况
# import matplotlib.font_manager as pltFont
# chinfo = pltFont.FontProperties(fname='C:/Windows/Fonts/Microsoft YaHei UI.ttc')
# plt.title("林晓舜测试", fontsize=24, fontproperties=chinfo)

squares = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]
plt.plot(input_values, squares, linewidth=5)

# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()