import pandas as pd

def faneuil_hall():
    file = ["FANEIUL_HALL_MERCHANTS_ASSOC.csv",
            "FANEUIL_HALL_MERCHANT_ASSOC_.csv",
            "FANEUIL_HALL_MERCHANTS_ASSOC.csv",
            "FANEUIL_HALL_MERCHANTS_ASSOC_.csv",
            "FANUEIL_HALL_MERCHANT_ASSOCIAT.csv"]


    fan0 = pd.read_csv("../data/event_type_clusterings/" + file[0])
    fan1 = pd.read_csv("../data/event_type_clusterings/" + file[1])
    fan2 = pd.read_csv("../data/event_type_clusterings/" + file[2])
    fan3 = pd.read_csv("../data/event_type_clusterings/" + file[3])
    fan4 = pd.read_csv("../data/event_type_clusterings/" + file[4])

    df = pd.concat([fan0, fan1, fan2, fan3, fan4])

    df.to_csv("../data/event_clusterings_small/FANEIUL_HALL_MERCHANTS_ASSOCIATION")

if __name__ == '__main__':
    faneuil_hall()