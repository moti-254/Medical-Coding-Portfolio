import csv

with open('patient_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        errors = []
        for field in ['PatientID', 'Name', 'DOB', 'ServiceDate', 'Code', 'Amount']:
            if not row[field]:
                errors.append(field)
        if errors:
            print(f"Row {row['PatientID']} has missing fields: {errors}")
        else:
            print(f"Row {row['PatientID']} is valid.")
