import sqlite3
import pandas as pd
import ssl
import matplotlib.pyplot as plt

# Set the certificate verification paths
ssl._create_default_https_context = ssl._create_unverified_context
# --------------------

conn = sqlite3.connect("m4_survey_data.sqlite") # open a database connection
# --------------------

# print how many rows are there in the table named 'master'
QUERY = """
SELECT COUNT(*)
FROM master
"""
# the read_sql_query runs the sql query and returns the data as a dataframe
df = pd.read_sql_query(QUERY,conn)
print (df.head())
# -------------------

# print all the tables names in the database
QUERY = """
SELECT name as Table_Name FROM
sqlite_master WHERE
type = 'table'
"""
# the read_sql_query runs the sql query and returns the data as a dataframe
print (pd.read_sql_query(QUERY,conn))
# ------------------------

# How to run a group by query
QUERY = """
SELECT Age,COUNT(*) as count
FROM master
group by age
order by age
"""
print (pd.read_sql_query(QUERY,conn))
# -------------------------

# How to describe a table
table_name = 'master'  # the table I wish to describe

QUERY = """
SELECT sql FROM sqlite_master
WHERE name= '{}'
""".format(table_name)

df = pd.read_sql_query(QUERY,conn)
print(df.iat[0,0])
# --------------------------

# --------------------------> ## Visualizing distribution of data

# Plot a histogram of `ConvertedComp.`
# Query to retrieve the 'ConvertedComp' column from the 'master' table
QUERY = """
SELECT ConvertedComp
FROM master
"""

# Read the data into a pandas DataFrame
df = pd.read_sql_query(QUERY, conn)


# Plot a histogram
plt.figure(figsize=(10, 6))
plt.hist(df['ConvertedComp'], bins=30, edgecolor='k')
plt.xlabel('Converted Compensation')
plt.ylabel('Frequency')
plt.title('Histogram of Converted Compensation')
plt.show()
# ---------------------

# Plot a box plot of `Age.`
# Query to retrieve the 'Age' column from the 'master' table
QUERY = """
SELECT Age
FROM master
"""

# Read the data into a pandas DataFrame
df = pd.read_sql_query(QUERY, conn)


# Plot a box plot of Age
Age_Data = df['Age']
Age_Data.plot(kind = 'box')
plt.title("Box Plot of Age")
plt.show()
# ------------------


# ------------------> ## Visualizing relationships in data

# Create a scatter plot of `Age` and `WorkWeekHrs.`
# Query to retrieve the 'Age' and 'WorkWeekHrs' columns from the 'master' table
QUERY = """
SELECT Age, WorkWeekHrs
FROM master
"""

# Read the data into a pandas DataFrame
df = pd.read_sql_query(QUERY, conn)

# Plot a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['WorkWeekHrs'], alpha=0.5)
plt.xlabel('Age')
plt.ylabel('Work Week Hours')
plt.title('Scatter Plot of Age vs. Work Week Hours')
plt.show()
# --------------------

# Create a bubble plot of `WorkWeekHrs` and `CodeRevHrs`, use `Age` column as bubble size.
# Query to retrieve the 'WorkWeekHrs', 'CodeRevHrs', and 'Age' columns from the 'master' table
QUERY = """
SELECT WorkWeekHrs, CodeRevHrs, Age
FROM master
"""

# Read the data into a pandas DataFrame
df = pd.read_sql_query(QUERY, conn)

# Plot a bubble plot
plt.figure(figsize=(10, 6))
plt.scatter(df['WorkWeekHrs'], df['CodeRevHrs'], s=df['Age'], alpha=0.5)
plt.xlabel('Work Week Hours')
plt.ylabel('Code Review Hours')
plt.title('Bubble Plot of Work Week Hours vs. Code Review Hours')
plt.colorbar(label='Age')  # Add a colorbar to represent the bubble size (Age)
plt.show()
# ----------------------

# ----------------------> ## Visualizing composition of data

# Create a pie chart of the top 5 databases that respondents wish to learn next year. Label the pie chart with database names. Display percentages of each database on the pie chart.
# Query to retrieve the 'DatabaseDesireNextYear' column from the 'DatabaseDesireNextYear' table
QUERY = """
SELECT DatabaseDesireNextYear
FROM DatabaseDesireNextYear
"""

# Read the data into a pandas DataFrame
df = pd.read_sql_query(QUERY, conn)

# Count the occurrences of each database and select the top 5
top_databases = df['DatabaseDesireNextYear'].value_counts().nlargest(5)

# Plot a pie chart
plt.figure(figsize=(8, 8))
plt.pie(top_databases, labels=top_databases.index, autopct='%1.1f%%')
plt.title('Top 5 Databases Respondents Wish to Learn Next Year')
plt.show()
# ------------------------

# Create a stacked chart of median `WorkWeekHrs` and `CodeRevHrs` for the age group 30 to 35.
# Query to retrieve the 'WorkWeekHrs', 'CodeRevHrs', and 'Age' columns from the 'master' table
QUERY = """
SELECT WorkWeekHrs, CodeRevHrs, Age
FROM master
"""

# Read the data into a pandas DataFrame
df = pd.read_sql_query(QUERY, conn)

# Filter the data for respondents within the age group 30 to 35
age_group_df = df[(df['Age'] >= 30) & (df['Age'] <= 35)]

# Calculate the median 'WorkWeekHrs' and 'CodeRevHrs'
median_work_week_hrs = age_group_df['WorkWeekHrs'].median()
median_code_rev_hrs = age_group_df['CodeRevHrs'].median()

# Create a stacked bar chart
plt.figure(figsize=(8, 6))
plt.bar('Age Group 30-35', median_work_week_hrs, label='Median WorkWeekHrs')
plt.bar('Age Group 30-35', median_code_rev_hrs, bottom=median_work_week_hrs, label='Median CodeRevHrs')
plt.xlabel('Age Group')
plt.ylabel('Median Hours')
plt.title('Median WorkWeekHrs and CodeRevHrs for Age Group 30-35')
plt.legend()
plt.show()
# ----------------------

# ----------------------> ## Visualizing comparison of data

# Create Line chart Plot the median `ConvertedComp` for all ages from 45 to 60.
# Query to retrieve the 'Age' and 'ConvertedComp' columns from the 'master' table
QUERY = """
SELECT Age, ConvertedComp
FROM master
"""

# Read the data into a pandas DataFrame
df = pd.read_sql_query(QUERY, conn)

# Filter the data for respondents within the age range 45 to 60
age_range_df = df[(df['Age'] >= 45) & (df['Age'] <= 60)]

# Calculate the median 'ConvertedComp' for each age
median_converted_comp_by_age = age_range_df.groupby('Age')['ConvertedComp'].median()

# Create a line chart
plt.figure(figsize=(10, 6))
plt.plot(median_converted_comp_by_age.index, median_converted_comp_by_age.values, marker='o')
plt.xlabel('Age')
plt.ylabel('Median Converted Compensation')
plt.title('Median Converted Compensation for Ages 45 to 60')
plt.grid(True)
plt.show()
# -------------------------

# Create a horizontal bar chart using column `MainBranch.`
# Query to retrieve the 'MainBranch' column from the 'master' table
QUERY = """
SELECT MainBranch
FROM master
"""

# Read the data into a pandas DataFrame
df = pd.read_sql_query(QUERY, conn)

# Count the occurrences of each value in the 'MainBranch' column
main_branch_counts = df['MainBranch'].value_counts()

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(main_branch_counts.index, main_branch_counts.values)
plt.xlabel('Number of Respondents')
plt.ylabel('Main Branch')
plt.title('Number of Respondents by Main Branch')
plt.show()
# --------------------------

# Query to retrieve the 'LanguageDesireNextYear' column from the 'LanguageDesireNextYear' table
QUERY = """
SELECT LanguageDesireNextYear
FROM LanguageDesireNextYear
"""

# Read the data into a pandas DataFrame
df = pd.read_sql_query(QUERY, conn)

# Get the top 5 programming languages respondents wish to learn next year
language_counts = df['LanguageDesireNextYear'].value_counts()

print("Programming languages respondents wish to learn next year, sorted by count:")
for language, count in language_counts.items():
    print(f"{language}: {count}")
# ----------------------------

# Query to retrieve the 'DevType' column from the 'DevType' table
QUERY = """
SELECT DevType
FROM DevType
"""

# Read the data into a pandas DataFrame
df = pd.read_sql_query(QUERY, conn)

# Count the occurrences of each job role in the 'DevType' column
job_role_counts = df['DevType'].value_counts()

# Find the most common job role reported by the respondents
most_common_job_role = job_role_counts.idxmax()

# Find the count of the most common job role
most_common_job_role_count = job_role_counts.max()

print("The majority of respondents' current job roles:")
print(f"{most_common_job_role} (Count: {most_common_job_role_count})")
# -------------------------


conn.close()

