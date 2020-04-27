path = "Data/"
filename = "train_sample.csv"

import pandas as pd

df = pd.read_csv(path + filename)

from General_functions import haversine_distance, weekday

#On construit le jour de la semaine à partie de la data au format str
df = weekday(df)

#On fait une estimation de la distance effectuée (en mètres) lors de chaque trajet
df["distance"] = df.apply(lambda x: haversine_distance(x["pickup_latitude"], x["pickup_longitude"], x["dropoff_latitude"], x["dropoff_longitude"]), axis = 1)

#On agrège les distances parcourues par jour et on divise par 1000 pour avoir la distance en km 
(df.groupby("weekday")["distance"].sum()/1000).to_json("Data/train_weekday_km.json")
