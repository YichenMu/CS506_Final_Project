#-*- coding=utf-8 -*- 
#@Time:2021/2/28 10:21 PM
#@Author:Yichen Mu
#@File:Visualization_6_subplot.py
#@Software:PyCharm

import numpy as np
import matplotlib.pyplot as plt
from calculate_data_by_year import calculate_all_sum_OT, calculate_sum_OT, extract_data

values_OTdescription = calculate_all_sum_OT("DESCRIPTION")
code_list = []
value_list = []  # OT data every year by OTdescription
values_list = []  # 6 lists of OT data by year
new_values_list=[] # store the top10 OT
new_code_list=[]   # store the top10 OTdescription
years_list = [2015, 2016, 2017, 2018, 2019, 2020]
for key, value in values_OTdescription.items():
    code_list.append(key)
    value_list.append(value)
print(code_list)
# Initialize the lists
for i in range(6):
    values_list.append([])
for i in range(6):
    new_code_list.append([])
# Extract OT from the original data which is classified by OTCODE to store them according to the year.
for i in range(6):  # 6 years
    for j in range(len(value_list)):
        values_list[i].append(value_list[j][i])
# Sort the OT in every year to select the top 10 length of OT.
for i in range(len(values_list)):
    new_values_list.append(sorted(values_list[i],reverse=True)[:10])
# Select the OTCODE according to the sorted top10 OT array.
for i in range(len(new_values_list)):
    for j in range(len(new_values_list[i])):
        new_code_list[i].append(code_list[values_list[i].index(new_values_list[i][j])])
print(new_values_list)
new_values_list=np.array(new_values_list)
#print(type(new_values_list),type(new_values_list[0]))
print(new_code_list)
fig=plt.figure(figsize=(80,50))
fig.suptitle('Top 10 event types in every year',fontsize=30)
ax1=fig.add_subplot(2,3,1)
bars1=plt.barh(new_code_list[0],new_values_list[0],label='description')
for bar, label in zip(bars1, new_code_list[0]):
    width = bar.get_width()
    plt.annotate(width, xy=(width, bar.get_y() + 0.4), ha='left', va='center',size=15)
plt.title('2015',size=30)
plt.xlabel('Time',fontdict={'family' : 'Times New Roman', 'size': 30})
plt.ylabel('OTevent',fontdict={'family' : 'Times New Roman', 'size': 30})
plt.xticks(fontproperties = 'Times New Roman', size = 15)
plt.yticks(fontproperties = 'Times New Roman', size = 15)
plt.legend()
ax2=fig.add_subplot(2,3,2)
bars2=plt.barh(new_code_list[1],new_values_list[1],label='description')
for bar, label in zip(bars2, new_code_list[1]):
    width = bar.get_width()
    plt.annotate(width, xy=(width, bar.get_y() + 0.4), ha='left', va='center',size=15)
plt.title('2016',size=30)
plt.xlabel('Time',fontdict={'family' : 'Times New Roman', 'size': 30})
plt.ylabel('OTevent',fontdict={'family' : 'Times New Roman', 'size': 30})
plt.xticks(fontproperties = 'Times New Roman', size = 15)
plt.yticks(fontproperties = 'Times New Roman', size = 15)
plt.legend()
ax3=fig.add_subplot(2,3,3)
bars3=plt.barh(new_code_list[2],new_values_list[2],label='description')
for bar, label in zip(bars3, new_code_list[2]):
    width = bar.get_width()
    plt.annotate(width, xy=(width, bar.get_y() + 0.4), ha='left', va='center',size=15)
plt.title('2017',size=30)
plt.xlabel('Time',fontdict={'family' : 'Times New Roman', 'size': 30})
plt.ylabel('OTevent',fontdict={'family' : 'Times New Roman', 'size': 30})
plt.xticks(fontproperties = 'Times New Roman', size = 15)
plt.yticks(fontproperties = 'Times New Roman', size = 15)
plt.legend()
ax4=fig.add_subplot(2,3,4)
bars4=plt.barh(new_code_list[3],new_values_list[3],label='description')
for bar, label in zip(bars4, new_code_list[3]):
    width = bar.get_width()
    plt.annotate(width, xy=(width, bar.get_y() + 0.4), ha='left', va='center',size=15)
plt.title('2018',size=30)
plt.xlabel('Time',fontdict={'family' : 'Times New Roman', 'size': 30})
plt.ylabel('OTevent',fontdict={'family' : 'Times New Roman', 'size': 30})
plt.xticks(fontproperties = 'Times New Roman', size = 15)
plt.yticks(fontproperties = 'Times New Roman', size = 15)
plt.legend()
ax5=fig.add_subplot(2,3,5)
bars5=plt.barh(new_code_list[4],new_values_list[4],label='description')
for bar, label in zip(bars5, new_code_list[4]):
    width = bar.get_width()
    plt.annotate(width, xy=(width, bar.get_y() + 0.4), ha='left', va='center',size=15)
plt.title('2019',size=30)
plt.xlabel('Time',fontdict={'family' : 'Times New Roman', 'size': 30})
plt.ylabel('OTevent',fontdict={'family' : 'Times New Roman', 'size': 30})
plt.xticks(fontproperties = 'Times New Roman', size = 15)
plt.yticks(fontproperties = 'Times New Roman', size = 15)
plt.legend()
ax6=fig.add_subplot(2,3,6)
bars6=plt.barh(new_code_list[5],new_values_list[5],label='description')
for bar, label in zip(bars6, new_code_list[5]):
    width = bar.get_width()
    plt.annotate(width, xy=(width, bar.get_y() + 0.4), ha='left', va='center',size=15)
plt.title('2020',size=30)
plt.xlabel('Time',fontdict={'family' : 'Times New Roman', 'size': 30})
plt.ylabel('OTevent',fontdict={'family' : 'Times New Roman', 'size': 30})
plt.xticks(fontproperties = 'Times New Roman', size = 15)
plt.yticks(fontproperties = 'Times New Roman', size = 15)
plt.legend()
fig.tight_layout(pad=13.0, w_pad=3.0, h_pad=3.0)
plt.savefig('../img/every_year_top10_subplots.png')
plt.show()