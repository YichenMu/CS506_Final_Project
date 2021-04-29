# Author: Shuohe_Ren
# Date: 2021 / 4 / 28

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
OTHours, years = [], []

for i in range(2015, 2021):
    data = pd.read_csv("../data/Special-Events-" + str(i) + ".csv")
    OTHours.append(int(data.loc[:,['OTHOURS']].sum()))
    years.append(i)

#years = np.int(years)
#vector = np.vectorize(np.float)
#OTHours = vector(OTHours)

bars = plt.barh(years, OTHours, color='black')


plt.title("OT Hours each Year")
plt.ylabel("Year")
plt.xlabel("OT Hours")
plt.xlim((60000, 170000))
plt.tight_layout()
plt.savefig("../img/OT Hours by Year.png")