#-*- coding=utf-8 -*- 
#@Time:2021/2/28 9:36 PM
#@Author:Yichen Mu
#@File:visualization_sum_OTcode.py
#@Software:PyCharm
import matplotlib.pyplot as plt
from calculate_data_by_year import calculate_all_sum_OT, calculate_sum_OT, extract_data

values_OTCODE = calculate_all_sum_OT("DESCRIPTION")
code_list = []
value_list = []  # OT data every year by OTcode
#values_list = []  # 6 lists of OT data by year
years_list = [2015, 2016, 2017, 2018, 2019, 2020]
for key, value in values_OTCODE.items():
    code_list.append(key)
    value_list.append(value)

for i in range(len(value_list)):
    sum=0
    for j in range(len(value_list[i])):
        sum+=value_list[i][j]
    value_list[i]=sum
# print(len(value_list),value_list)
# visualize the data after sorting
new_code_list=[]
new_value_list=sorted(value_list,reverse=True)
for i in range(len(new_value_list)):
    new_code_list.append(code_list[value_list.index(new_value_list[i])])
plt.figure(figsize=(80,80))
plt.ylim((-1, 59))
bars=plt.barh(new_code_list,new_value_list,label='description')
for bar, label in zip(bars, new_code_list):
    width = bar.get_width()
    plt.annotate(width, xy=(width, bar.get_y() + 0.4), ha='left', va='center',size=30)
# print(new_code_list,new_value_list)
# visualize the data without sorting the OT
# plt.bar(range(len(value_list)),value_list,width=0.9,label='OT',tick_label=code_list)
plt.xlabel('Time',fontdict={'family' : 'Times New Roman', 'size': 40})
plt.ylabel('OTevent',fontdict={'family' : 'Times New Roman', 'size': 40})
plt.xticks(fontproperties = 'Times New Roman', size = 30)
plt.yticks(fontproperties = 'Times New Roman', size = 30)
plt.title('2015-2020 total OT sorted by OTCODE',size=50)
# plt.tick_params(axis='x',which='major',labelsize=6)
plt.legend()
plt.tight_layout()
plt.savefig('../img/Sorted OT by event code from 2015 to 2020.png')
#plt.savefig('sum_year_OT.png')
plt.show()