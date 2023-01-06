import csv, json


def csv_to_json():
    stores = ""
    file = open("growwdata.csv")
    csvreader = csv.reader(file)
    new_file = open("stores.json", "w")
    fields = list(next(csvreader))
    fields[0] = "domain"
    for row in csvreader:
        store_object = {}
        for i in range(len(fields)):
            store_object[fields[i]] = row[i]

        stores += json.dumps(store_object)
        stores += "\n"
    file.close()
    new_file.write(stores)
    new_file.close()
    return stores

print(csv_to_json())