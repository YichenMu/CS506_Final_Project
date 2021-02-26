import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("../data/Special Events 2015 - present - 2018.csv")
    for _, row in data.iterrows():
        if row['WRKDHRS'] - row['OTHOURS'] != 0:
            print(row)
