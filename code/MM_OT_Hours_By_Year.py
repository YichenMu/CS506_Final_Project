# Author: Joey_Cheng
# Date: 2021 / 4 / 26

import pandas as pd

OTHours = []

for i in range(2015, 2021):
    data = pd.read_csv("../data/Special-Events-" + str(i) + ".csv")
    OTHours.append(data.loc[data["DESCRIPTION"] == "MASS / MELNEA"]["OTHOURS"].sum())

print(OTHours)
