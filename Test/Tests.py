#On test la longueur du dataframe
def test_columns_len(df):
    assert len(df.columns) == 11, "Should be 11"

#On test les types des colonnes correspondant à des coordonnées
#Impératif qu'ils soient en float si on veut pouvoir calculer la distance associée au trajet
def test_columns_types(df):
    import numpy
    for col in ["pickup_latitude", "pickup_longitude", "dropoff_latitude", "dropoff_longitude"]:
        assert type(df.pickup_latitude.iloc[0]) == numpy.float64

if __name__ == "__main__":
    import pandas as pd
    path = "Data/"
    filename = "train_sample.csv"
    df = pd.read_csv(path + filename, index_col = 0 )
    print("1 - input lenght")
    test_columns_len(df)
    print("2 - coordinates types")
    test_columns_types(df)

    print("Everything passed")
