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

# how many duplicated values are there in the column Respondent?
duplicate_in_Respondent = df['Respondent'].duplicated().sum()
print ('Duplicated values in Respondent Column are:', duplicate_in_Respondent)

# Remove the duplicate rows from the dataframe.
df.drop_duplicates(inplace=True)

# Find the number of blank (missing or NaN) rows in the 'EdLevel' column
blank_edlevel_rows = df['EdLevel'].isnull().sum()
print("Number of blank rows in the 'EdLevel' column:", blank_edlevel_rows)

# Find the missing values for all columns.
missing_values = df.isnull().sum()
print("Missing values for each column:")
print(missing_values)

# Find out how many rows are missing in the column 'WorkLoc'
missing_values1 = df['WorkLoc'].isnull().sum()
print("Missing values for WorkLoc column:", missing_values1)

# Find out how many rows are missing in the column 'Country'
missing_values2 = df['Country'].isnull().sum()
print("Missing values for Country column:", missing_values2)

# Find the value counts for the column WorkLoc.
workloc_value_counts = df['WorkLoc'].value_counts()
print("Value counts for the 'WorkLoc' column:", workloc_value_counts)

# Identify the value that is most frequent (majority) in the WorkLoc column.
most_frequent_workloc = df['WorkLoc'].value_counts().idxmax()
print("The value that is most frequent in the 'WorkLoc' column:", most_frequent_workloc)

# Identify the value that is most frequent (majority) in the Employment column.
most_frequent_Employment = df['Employment'].value_counts().idxmax()
print("The value that is most frequent in the 'Employment' column:", most_frequent_Employment)

# Identify the value that is minimum in the UndergradMajor column.
minimum_UndergradMajor = df['UndergradMajor'].value_counts().idxmin()
print("The value that is minimum in the 'EUndergradMajor' column:", minimum_UndergradMajor)

# Impute (replace) all the empty rows in the column WorkLoc with the value that you have identified as majority.
# Impute (replace) empty rows in the 'WorkLoc' column with 'Office'
df['WorkLoc'].fillna(most_frequent_workloc, inplace=True)

# How many Respondent are being paid yearly?
# Filter the DataFrame to include only respondents who are paid yearly
yearly_paid_respondents = df[df['CompFreq'] == 'Yearly']
# Count the number of respondents who are paid yearly
num_yearly_paid_respondents = len(yearly_paid_respondents)
print("Number of respondents being paid yearly:", num_yearly_paid_respondents)



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


# Find the median of the 'NormalizedAnnualCompensation' column
median_normalized_compensation = df['NormalizedAnnualCompensation'].median()
print("Median of NormalizedAnnualCompensation:", median_normalized_compensation)
