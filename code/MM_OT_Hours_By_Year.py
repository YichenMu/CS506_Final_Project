# Author: Joey_Cheng
# Date: 2021 / 4 / 26

import pandas as pd
import matplotlib.pyplot as plt

OTHours, years = [], []

for i in range(2015, 2021):
    data = pd.read_csv("../data/Special-Events-" + str(i) + ".csv")
    OTHours.append(data.loc[data["DESCRIPTION"] == "MASS / MELNEA"]["OTHOURS"].sum())
    years.append(i)

bars = plt.barh(years, OTHours, color=["sienna", "olive", "brown", "peru"])

# add annotates
for bar, label in zip(bars, OTHours):
    plt.annotate(label, xy=(label, bar.get_y() + 0.4), ha='left', va='center')

plt.title("OT Hours for Mass/Melnea by Year")
plt.ylabel("Year")
plt.xlabel("OT Hours")
plt.xlim((0, 48000))
plt.tight_layout()
plt.savefig("../img/OT Hours for MassMelnea by Year.png")
