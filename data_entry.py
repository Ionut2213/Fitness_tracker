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