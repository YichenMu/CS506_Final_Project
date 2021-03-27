"""
Joshua Cominelli
CS506
top_n_officers.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib; matplotlib.get_backend()

# n: Number of officers to display
def find_top_officers(n):

    # Iterate each year 2015-2020
    all_years = []
    for i in range(15,21):
        df = pd.read_csv('../data/Special-Events-20'+str(i)+'.csv')[['NAME','OTDATE','OTHOURS']]
        df.set_index(['NAME'])
        all_years.append(df)

        df_20xx = df.groupby(['NAME']).sum()
        df_20xx = df_20xx.sort_values(by=['OTHOURS'],ascending=False)
        df_20xx = df_20xx[:n]

        df_20xx = df_20xx.iloc[::-1]

        pd.set_option('display.max_rows', n)
        #plt.rcParams["figure.figsize"] = [10, 18]
        matplotlib.rc('font', size=25, weight='bold')

        print('\n~~ BEGIN 20'+str(i)+' ~~')
        print(df_20xx.head(n))
        print('\n~~ END 20'+str(i)+' ~~')

        plt.figure(figsize=(50, 180))
        plt.ylim((-1, 101))
        bars = plt.barh(df_20xx.index.to_list(), df_20xx.OTHOURS, height=0.8, color=["sienna", "olive", "brown", "peru"])
        for bar, label in zip(bars, df_20xx.OTHOURS):
            width = bar.get_width()
            plt.annotate(width, xy=(width, bar.get_y() + 0.4), ha='left', va='center')
        #df_20xx.plot(kind='barh')
        plt.title("BPD Special Event Overtime Hours: 20"+str(i),
                  fontdict={'fontsize': 50, 'fontweight': "bold"})
        plt.ylabel("Officer Name", fontdict={'fontsize': 50, 'fontweight': "bold"})
        plt.xlabel("Overtime Hours", fontdict={'fontsize': 50, 'fontweight': "bold"})
        plt.tight_layout()
        plt.savefig("../img/top 100 OT officers - 20" + str(i) + ".png")

    # Show total 2015-2020
    df_total = pd.concat(all_years, ignore_index=True) 
    df_total.set_index(['NAME'])
    df_total = df_total.groupby(['NAME']).sum()
    df_total = df_total.sort_values(by=['OTHOURS'],ascending=False)
    df_total = df_total[:n]

    pd.set_option('display.max_rows', n)
    # plt.rcParams["figure.figsize"] = [17, 8]

    print('\n~~ BEGIN 2015-2020 ~~')
    print(df_total.head(n))
    print('\n~~ END 2015-2020 ~~')

    # df_total.plot(kind='bar')
    # plt.title("BPD Special Event Overtime Hours: Total 2015-2020")
    # plt.ylabel("Officer Name")
    # plt.xlabel("Overtime Hours")
    # plt.tight_layout()
    # plt.show()
    plt.figure(figsize=(50, 180))
    plt.ylim((-1, 101))
    bars = plt.barh(df_total.index.to_list(), df_total.OTHOURS, height=0.8, color=["sienna", "olive", "brown", "peru"])
    for bar, label in zip(bars, df_total.OTHOURS):
        width = bar.get_width()
        plt.annotate(width, xy=(width, bar.get_y() + 0.4), ha='left', va='center')
    # df_20xx.plot(kind='barh')
    plt.title("BPD Special Event Overtime Hours: Total 2015-2020",
              fontdict={'fontsize': 50, 'fontweight': "bold"})
    plt.ylabel("Officer Name", fontdict={'fontsize': 50, 'fontweight': "bold"})
    plt.xlabel("Overtime Hours", fontdict={'fontsize': 50, 'fontweight': "bold"})
    plt.tight_layout()
    plt.savefig("../img/top 100 OT officers - 2015-2020.png")

find_top_officers(100)
