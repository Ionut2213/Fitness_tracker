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

    @classmethod
    def add_entry(cls, date, amount_of_km, category, note):
        new_data_added = {
            'date': date,
            'amount_of_km': amount_of_km,
            'category' : category,
            'note' : note
        }

        with open(cls.CSV_FILE, "a", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_data_added)
        print("Your new entry has been successfully added")







CSV.initializing_csv()
CSV.add_entry("22-03-205", 15, "walk", "outdoor walk")
