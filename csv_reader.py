import csv


def import_zip():
    ZIPCODES = {}
    file = open("zipcodes.csv")
    new_python_file = open("zipcode_data.py", "w")
    csvreader = csv.reader(file)
    PINCODE, CITY, STATE = 1, 8, 9
    next(csvreader)
    for row in csvreader:
        ZIPCODES[row[PINCODE]] = {
            "city": row[CITY],
            "state": row[STATE]
        }
    file.close()
    new_python_file.write("ZIPCODES"+ " = "+ str(ZIPCODES))
    new_python_file.close()

import_zip()