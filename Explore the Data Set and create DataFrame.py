import pandas as pd
import ssl
# for certified ssl
ssl._create_default_https_context = ssl._create_unverified_context

dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"

df = pd.read_csv(dataset_url)


# Find out the number of rows and columns
num_rows, num_cols = df.shape
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)

#Identify the data types of each Columns:
print (df.dtypes)

# Calculate the mean age of survey participants
mean_age = df['Age'].mean()
print("Mean age of survey participants:", mean_age)
print (df['Age'].dtypes)

# Find the number of unique countries in the 'Country' column
unique_countries_count = df['Country'].nunique()
print("Number of unique countries in the 'Country' column:", unique_countries_count)


#  Find how many duplicate rows exist in the dataframe.
duplicate_rows_count = df.duplicated().sum()
print("Number of duplicate rows in the DataFrame:", duplicate_rows_count)

# Remove the duplicate rows from the dataframe.
df.drop_duplicates(inplace=True)

# Find the missing values for all columns.
missing_values = df.isnull().sum()
print("Missing values for each column:")
print(missing_values)

# Find out how many rows are missing in the column 'WorkLoc'
missing_values1 = df['WorkLoc'].isnull().sum()
print("Missing values for WorkLoc column:", missing_values1)

# Find the value counts for the column WorkLoc.
workloc_value_counts = df['WorkLoc'].value_counts()
print("Value counts for the 'WorkLoc' column:", workloc_value_counts)

# Identify the value that is most frequent (majority) in the WorkLoc column.
most_frequent_workloc = df['WorkLoc'].value_counts().idxmax()
print("The value that is most frequent in the 'WorkLoc' column:", most_frequent_workloc)


# Impute (replace) all the empty rows in the column WorkLoc with the value that you have identified as majority.
# Impute (replace) empty rows in the 'WorkLoc' column with 'Office'
df['WorkLoc'].fillna(most_frequent_workloc, inplace=True)


#### --------> Normalizing data

# List out the various categories in the column 'CompFreq'
compfreq_categories = df['CompFreq'].unique()
print("Various categories in the 'CompFreq' column:", compfreq_categories)

# Create a new column named 'NormalizedAnnualCompensation'.
# Custom function to calculate the NormalizedAnnualCompensation based on CompFreq
def calculate_normalized_compensation(row):
    if row['CompFreq'] == 'Yearly':
        return row['CompTotal']
    elif row['CompFreq'] == 'Monthly':
        return row['CompTotal'] * 12
    elif row['CompFreq'] == 'Weekly':
        return row['CompTotal'] * 52
    else:
        return None  # Handle cases with missing or invalid CompFreq values

# Apply the custom function to create the 'NormalizedAnnualCompensation' column
df['NormalizedAnnualCompensation'] = df.apply(calculate_normalized_compensation, axis=1)
print (df.head())