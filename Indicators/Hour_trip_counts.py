path = "Data/"
filename = "train_sample.csv"

import pandas as pd

df = pd.read_csv(path + filename)

from General_functions import check_hour, hour

hour(df).hour.apply(lambda x: check_hour(x)).value_counts().to_json("Data/train_hour_trip_count.json")
