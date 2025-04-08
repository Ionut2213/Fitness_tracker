import pandas as pd
import csv
from datetime import datetime
import matplotlib.pyplot as plt

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

    @classmethod
    def get_data_from_csv(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df['amount_of_km'] = pd.to_numeric(df['amount_of_km'], errors='coerce')

        df.columns = df.columns.str.lower()

        df['date'] = pd.to_datetime(df['date'], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filered_df = df.loc[mask]


        if filered_df.empty:
            print("No entries found in your specified range.")
        else:
            print(f"Entries from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}:")
            print(filered_df.to_string(index=False, formatters={'date': lambda x: x.strftime(CSV.FORMAT)}))

            total_walk = filered_df[filered_df["category"] == "Walk"]["amount_of_km"].sum()
            total_inside_bike = filered_df[filered_df["category"] == "Inside Bike"]["amount_of_km"].sum()

            print("-------------------------------------------------------------")
            print('\nSummary: ')
            print(f"Total Walk: {total_walk:.2f}")
            print(f"Total Inside Bike: {total_inside_bike:.2f}")
        return filered_df
        








def add_date():
    CSV.initializing_csv()

    date = get_date_from("Enter the date in this format (dd-mm-yyyy): ", allow_default=True)
    amount_of_km = get_amount_of_km()
    category = get_the_category()
    note = get_note()
    CSV.add_entry(date, amount_of_km, category, note)

# Part to generate chart
def get_data_plot_pie(df):

    total_walk = df[df['category'] == 'Walk']['amount_of_km'].sum()
    total_inside_bike = df[df['category'] == 'Inside Bike']['amount_of_km'].sum()

    labels = ['Walk', 'Inside Bike']
    sizes = [total_walk, total_inside_bike]
    colors = ['green', 'red']

    plt.figure(figsize = (7, 7))
    plt.pie(sizes, labels=labels, autopct = '%1.1f%%', colors=colors, startangle=90, wedgeprops= {'edgecolor': 'black'})
    plt.title("Walk vs Inside Bike")
    plt.show()





# main() we handle the app functionality

def main():
    while True:
        print("\n1. Add a new record")
        print("2. View all records")
        print("3. Exit the program")

        choice = input("Hello! Plese enter your choice (1-3): ")

        if choice == '1':
            add_date()
        elif choice == '2':
            start_date = get_date_from("Please enter the start date of your search (dd-mm-yyyy): ")
            end_date = get_date_from("Enter last day of your search (dd-mm-yyyy): ")
            df = CSV.get_data_from_csv(start_date, end_date)
            if input("Do you want to plot this data ? (y/n): ").lower() == 'y':
                get_data_plot_pie(df)
        elif choice == '3':
            print("Have a good day!! Exit the program....")
            break
        else:
            print("Your choice is not an option!! Pick one from 1 to 3 ")








if __name__ == "__main__":
    main()



