from datetime import datetime

data_format = "%d-%m-%Y"

CATEGORIES = {
    "W": "Walk",
    "IB": "Inside Bike"
}


def get_date_from(prompt, allow_default = True):
    data_str = input(prompt)
    if allow_default and not data_str:
        return datetime.today().strftime(data_format)
    
    try:
        valid_date = datetime.strptime(data_str, data_format)
        return valid_date.strftime(data_format)
    except ValueError:
        print("You entered a wrong data format. Please enter the date in this format dd-mm-yyyy")
        return get_date_from(prompt, allow_default)
    



def get_amount_of_km():
    try:
        amount_of_km = float(input("Enter the amount of km: "))
        if amount_of_km <= 0:
            raise ValueError("Amount of km must be a positive number or greater then 0")
        return amount_of_km
    except ValueError as e:
        print(e)
        return get_amount_of_km()