import pandas as pd
from over_reported_OT import read_special_events_data

# Extract the data entries that entry[column_name] = code
def extract_data(column_name, code):
    """
    :param column_name: the name of the column, type: string
    :param code: the key looking for
    :return: a length 6 list, each element is a dataframe containing that year's data
    """
    filePaths = ["../data/Special Events 2015 - present - 2015.csv",
                 "../data/Special Events 2015 - present - 2016.csv",
                 "../data/Special Events 2015 - present - 2017.csv",
                 "../data/Special Events 2015 - present - 2018.csv",
                 "../data/Special Events 2015 - present - 2019.csv",
                 "../data/Special Events 2015 - present - 2020.csv"]

    output_data = []

    for path in filePaths:
        data = read_special_events_data(path)
        target_data = data[data[column_name] == code]
        output_data.append(target_data)

    return output_data


def calculate_average_OT(data):
    """
    :param data: list of data in dataframe by year
    :return: length 6 list, each element represents the result of that year
    """
    res = []
    for d in data:
        res.append(d.OTHOURS.mean())
    return res


def calculate_sum_OT(data):
    res = []
    for d in data:
        res.append(d.OTHOURS.sum())
    return res


if __name__ == '__main__':
    data = extract_data("OTCODE", 462)
    print(calculate_sum_OT(data))


