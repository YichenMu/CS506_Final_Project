"""
Joshua Cominelli
CS506
top_officers_2020_comparison.py

Takes the 10 highest earning officers of 2020 and compares their pay from 2011-2020
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():

    # First find the top 10 officers using overtime in 2020 for special events
    df = pd.read_csv('../data/Special-Events-2020.csv')[['NAME','OTHOURS']]
    df.set_index(['NAME'])

    df_hours = df.groupby(['NAME']).sum()
    df_hours = df_hours.sort_values(by=['OTHOURS'],ascending=False)
    df_hours = df_hours[:10]
    df_hours = df_hours.sort_values(by=['NAME'])
    names = df_hours.index.tolist()

    # Next, compare their overtime pay from backwards from 2020 to 2011 to see if covid had an impact
    for i in range(20,14,-1):
        df_all = pd.read_csv('../data/Police-Earnings-Report-20'+str(i)+'.csv')
        df_names = df_all.iloc[:, 0]
        df_pay = df_all.iloc[:, 6]

        df_join = pd.concat([df_names,df_pay], axis=1)
        df_join.columns = ['NAME', 'OVERTIME']

        df_20xx = df_join.loc[df_join['NAME'].isin(names)]
        df_20xx = df_20xx.sort_values(by=['NAME'],ascending=False)

        df_20xx['OVERTIME'] = df_20xx['OVERTIME'].str.replace(',', '')
        df_20xx['OVERTIME'] = df_20xx['OVERTIME'].str.replace('$', '')
        df_20xx['OVERTIME'] = df_20xx['OVERTIME'].astype(float)

        print(df_20xx)
        print()

        name_list = df_20xx['NAME'].tolist()
        pay_list = df_20xx['OVERTIME'].tolist()

        plt.figure(figsize=(15, 8))

        plt.barh(name_list,pay_list)

        plt.title('Top Special Events Overtime Users 2020 - Overtime Pay in 20'+str(i))

        for index, value in enumerate(pay_list):
            plt.text(value, index, str(value))

        plt.xlabel('Overtime Pay (in $)')

        plt.tight_layout()
        plt.savefig("../img/top_overtime_users_2020_pay_in_20"+str(i)+".png")
        plt.show()
        


main()