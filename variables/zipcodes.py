try:
    from zipcode_data import ZIPCODES
except:
    ZIPCODES = {}


def is_valid_zipcode(zipcode):
    return zipcode in ZIPCODES


def get_city_details(zipcode):
    if is_valid_zipcode(zipcode):
        return ZIPCODES[zipcode]
    return {}
