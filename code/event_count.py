# Author: Joey_Cheng
# Date: 2021/3/21

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def most_frequent_events():
    events = []
    counts = []

    for y in range(15, 21):
        data = pd.read_csv("../data/Special-Events-20" + str(y) + ".csv")

        events.append(data.DESCRIPTION.value_counts().idxmax())
        counts.append(data.DESCRIPTION.value_counts().max())

    return events, counts

# Return the top n events index and occurrence time
def most_frequent_event_total(n):
    DESCRIPTION = pd.Series()

    for y in range(15, 21):
        data = pd.read_csv("../data/Special-Events-20" + str(y) + ".csv")
        DESCRIPTION = pd.concat([DESCRIPTION, data.DESCRIPTION], ignore_index=True)

    return DESCRIPTION.value_counts()[:n].index.values, DESCRIPTION.value_counts()[:n].values

def least_frequent_events():
    events = []
    counts = []

    for y in range(15, 21):
        data = pd.read_csv("../data/Special-Events-20" + str(y) + ".csv")

        vc = data.DESCRIPTION.value_counts()
        events.append(vc[vc == vc.min()].index.values)
        counts.append(vc.min())

    return events, counts

def plot_most_frequent_events():
    events, counts = most_frequent_events()
    plt.figure(figsize=(20, 7))
    bars = plt.barh(range(2015, 2021), counts, color = ["sienna", "olive", "brown"])

    for bar, label in zip(bars, events):
        width = bar.get_width()

        plt.annotate(label, xy=(300, bar.get_y() + 0.4), ha='left', va='center')
        plt.annotate(width, xy=(width, bar.get_y() + 0.4), ha='left', va='center')
    plt.xlabel("OT times")
    plt.ylabel("Year")
    plt.title("Most frequent OT events by year")
    plt.savefig('../img/Most frequent OT events by year.png')
    plt.show()


def plot_most_frequent_events_total(n):
    events, counts = most_frequent_event_total(n)
    # print(events, counts)

    plt.figure(figsize=(20, 7))
    bars = plt.barh(events.astype(str), counts, color=["sienna", "olive", "brown", "peru"])

    for bar, label in zip(bars, events):
        width = bar.get_width()
        plt.annotate(width, xy=(width, bar.get_y() + 0.4), ha='left', va='center')

    plt.xlabel("OT times")
    plt.ylabel("Event Description")
    plt.title("Most frequent OT events 2015-2020")
    plt.savefig('../img/Most frequent OT events 2015-2020.png')
    plt.show()

if __name__ == '__main__':
    # most_frequent_events()
    # least_frequent_events()
    plot_most_frequent_events()
    plot_most_frequent_events_total(10)