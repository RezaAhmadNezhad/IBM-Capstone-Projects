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

# Find the number of unique countries in the 'Country' column
unique_countries_count = df['Country'].nunique()
print("Number of unique countries in the 'Country' column:", unique_countries_count)