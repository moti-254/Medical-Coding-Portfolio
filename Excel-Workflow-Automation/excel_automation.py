import pandas as pd

# Load Excel file
df = pd.read_excel('patient_data.xlsx')

# Flag missing codes
df['Code_Missing'] = df['Code'].isnull()
print("Rows with missing codes:")
print(df[df['Code_Missing']])

# Sum Amount per Patient
totals = df.groupby('PatientID')['Amount'].sum()
print("\nTotal Amount per Patient:")
print(totals)
