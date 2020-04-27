import pandas as pd
import numpy as np
import datetime

#Il s'agit de la distance great cricle / alternative à la geodesic
def haversine_distance(lat1, lon1, lat2, lon2):

    r = 6371
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) *   np.sin(delta_lambda / 2)**2
    res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res,5)*1000


#Crée un colonne distance dans un dataframe à partir des latitudes et longitudes des pointsde départ de d'arrivée
#Permet ensuite de calcluler la vitesse en km/h
def speed_estimate(df):

    #On crée d'abord la variable distance
    df["distance"] = df.apply(lambda x: haversine_distance(x["pickup_latitude"], x["pickup_longitude"], x["dropoff_latitude"], x["dropoff_longitude"]), axis = 1)
    df["speed"] = (df["distance"] / df["trip_duration"]) * 3.6

    return df


#Permet de transformer une date au format str au jour de la semaine correspondant
def weekday(df):

    ISOWeekDays = ("NoZeroInISOWeek","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    df["weekday"] = df["pickup_datetime"].apply(lambda x: ISOWeekDays[datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S').isoweekday()] if type(x) == str else x)

    return df


def check_hour(x):
    if 0 <= x < 4:
        return '0-4'
    elif 4 <= x < 8:
        return '4-8'
    elif 8 <= x < 12:
        return '8-12'
    elif 12 <= x < 16:
        return '12-16'
    elif 16 <= x < 20:
        return '16-20'
    else:
        return '20-24'

#Permet d'extraire l'heure de la course à partir d'une date au format str
def hour(df):

    df["hour"] =  df["pickup_datetime"].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S').hour if type(x) == str else x)

    return (df)
