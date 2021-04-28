# Author: Joey_Cheng
# Date: 2021/4/28

import pandas as pd
import matplotlib.pyplot as plt

def breakdown(year):
    count = [0 for i in range(0, 48)]
    filePath = "../data/Special-Events-" + str(year) + ".csv"
    data = pd.read_csv(filePath)

    for index, row in data.iterrows():
        if row.DESCRIPTION != "MASS / MELNEA":
            continue
        for i in range(0, 48):
            time = int(i / 2) * 100 + 30 * (i % 2)
            if int(row.ENDTIME) < int(row.STARTTIME):
                if time <= int(row.ENDTIME) or time >= int(row.STARTTIME):
                    count[i] += 1
            else:
                if int(row.STARTTIME) <= time <= int(row.ENDTIME):
                    count[i] += 1

    return count

def plot_breakdown(year):
    count = breakdown(year)
    clocks = []
    for i in range(0, 48):
        time = int(i / 2) * 100 + 30 * (i % 2)
        clocks.append(str(int(time / 100)) + ":" + str(time % 100).zfill(2))

    plt.figure(figsize=(30, 10))

    bars = plt.bar(clocks, count, color=["sienna", "olive", "brown", "peru"])

    # add annotates
    for bar, label in zip(bars, count):
        plt.annotate(label, xy=(bar.get_x(), label), ha='left', va='bottom')

    plt.title("MASS / MELNEA OT Breakdown " + str(year))
    plt.ylabel("Records count")
    plt.xlabel("Time")
    plt.xlim(-1, 48)
    plt.tight_layout()
    plt.savefig("../img/MM_breakdown_" + str(year) + ".png")

if __name__ == '__main__':
    plot_breakdown(2019)
    plot_breakdown(2020)
