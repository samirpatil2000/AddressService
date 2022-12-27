
ZIPCODES = {
    "401503": {
        "city": "Palghar",
        "state": "Maharashtra"
    },
    "400083": {
        "city": "Mumbai",
        "state": "Maharashtra"
    },
    "400057": {
        "city": "Sion",
        "state": "Maharashtra"
    },
    # "400057": ["Sion", "Maharashtra"]
}


def is_valid_zipcode(zipcode):
    return zipcode in ZIPCODES

def get_city_details(zipcode):
    if is_valid_zipcode(zipcode):
        return ZIPCODES[zipcode]
    return []




