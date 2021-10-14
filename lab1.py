import seaborn as sn
import numpy as np
import pandas as pd
import statsmodels.api as sm
import csv

import matplotlib.pyplot as plt

df = pd.read_csv("GLB.Ts_dSST.csv",  header=1, low_memory=True)
# next(f)

# print(df["Year"])
# d = {}
# print(3)
# for i in df["J-d"]:
#     j = df['Year']
#     print(i, j)
#     print(2)
# print(len(df["Year"]))
# print(len(df["J-D"]))

# df.plot(df["Year"], df["Year"])
# print(df["Year"])
# print(df["J-D"])
x = list(df["Year"])
y = list(df["J-D"])
aver = np.average(y[0:19])
# print(x)
# print(y)
print(aver)
plt.title("Year/temperature")
plt.plot(x, y, "ro", label="Annual Global Surface Temperature")

x2 = df["Year"][24], df["Year"][64], df["Year"][118], df["Year"][134], df["Year"][135], df["Year"][136], df["Year"][137]
y2 = df["J-D"][24], df["J-D"][64], df["J-D"][118], df["J-D"][134], df["J-D"][135], df["J-D"][136], df["J-D"][137]
year_list = [1904, 1944, 1998, 2014, 2015, 2016, 2017]


plt.plot(x2, y2, "ro", marker='o', color='black', label='Marked years')
for year in range(len(year_list)):
    plt.annotate(year_list[year], (x2[year], y2[year]))

plt.axhline(y=aver, color='black', linestyle='-', label="Average temperature 1880-1899 ")
plt.legend()
plt.show()
