path = "../Data/"
filename = "train_sample.csv"

import pandas as pd

df = pd.read_csv(path + filename)

from General_functions import haversine_distance, speed_estimate

speed_estimate(df).to_csv('../Data/train_speed.csv')
