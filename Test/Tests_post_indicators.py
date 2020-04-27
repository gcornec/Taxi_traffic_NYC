import unittest
import json
import pandas as pd


class TestIndicators(unittest.TestCase):

    #On vérifie que les clés du dictionaire correspondent bien aux jours de la semaine
    #On les trie pour pouvoir comparer exactement les listes
    def test_keys(self):
        path = "Data/"
        for filename in ["train_weekday_trip_counts.json", "train_weekday_km.json"]:
            data = json.loads(open(path + filename).read())
            self.assertEqual(sorted(list(data.keys())), ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday'])

    #ON vérifie que la vitesse calculée l'indicateur ne dépasse pas 100km/h, ce qui semblerait un peu louche
    def test_speed(self):
        path = "Data/"
        df = pd.read_csv(path + "train_speed.csv")
        self.assertEqual(len(df[df["speed"] > 100]), 0)


if __name__ == "__main__":

    unittest.main()
