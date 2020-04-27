path = "../Data/"
filename = "train_sample.csv"

import pandas as pd

df = pd.read_csv(path + filename)

from General_functions import weekday

weekday(df).weekday.value_counts().to_json("../Data/train_weekday_trip_counts.json")
