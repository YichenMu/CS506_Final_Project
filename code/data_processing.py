# Author: Joey_Cheng
# Date: 2021/3/21

import pandas as pd

# extract police earning data from all employees
def extract_police_earning():

    for y in range(11, 21):
        original_data = pd.read_csv("../data/employee-earnings-report-20" + str(y) + ".csv", encoding='latin-1')
        police_data = original_data[original_data[original_data.columns[1]].str.contains('police', case=False)]
        print(police_data.head())

        police_data.to_csv("../data/Police-Earnings-Report-20" + str(y) + ".csv", index=False)


def extract_special_events_2020():
    data = pd.read_csv("../data/Special-Events-2020.csv")
    special_events_data = data.loc[data["CHARGED"] == "SPECIAL EVENTS"]
    print(special_events_data.head())
    special_events_data.to_csv("../data/Special-Events-2020-updated.csv")


if __name__ == '__main__':
    extract_special_events_2020()
