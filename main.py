import pandas as pd
import csv
from datetime import datetime
import matplotlib as plt

# import all the functions from data_entry.py file

from data_entry import get_date_from, get_amount_of_km, get_the_category, get_note


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







def add_date():
    CSV.initializing_csv()

    date = get_date_from("Enter the date in this format (dd-mm-yyyy): ", allow_default=True)
    amount_of_km = get_amount_of_km()
    category = get_the_category()
    note = get_note()
    CSV.add_entry(date, amount_of_km, category, note)
