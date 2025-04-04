import pandas as pd
import csv
from datetime import datetime
import matplotlib as plt



# Class that handle the CSV file

class CSV:
    # Variables 
    CSV_FILE = 'fitness_tracker'
    COLUMNS = ["date", "amount_of_km", "category", "note"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initializing_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)







CSV.initializing_csv()
