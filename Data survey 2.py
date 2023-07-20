import pandas as pd
import matplotlib.pyplot as plt
import ssl
# for certified ssl
ssl._create_default_https_context = ssl._create_unverified_context


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv")

# Plot the Distribution Curve of ConvertedComp Column
# Assuming 'df' is the name of your DataFrame, and 'ConvertedComp' is the column name
data = df['ConvertedComp']
# Plot the Distribution Curve of ConvertedComp Column
plt.figure(figsize=(10, 6))
plt.hist(df["ConvertedComp"], bins=30, color='skyblue', edgecolor='black')
plt.xlabel("Converted Compensation")
plt.ylabel("Frequency")
plt.title("Distribution of Converted Compensation")
plt.grid(True)
plt.show()
# ----------------------------

# Plot the Histogram for ConvertedComp Column
plt.figure(figsize=(10, 6))
plt.hist(df["ConvertedComp"], bins=30, color='purple', edgecolor='black')
plt.xlabel("Converted Compensation")
plt.ylabel("Frequency")
plt.title("Histogram of Converted Compensation")
plt.grid(False)
plt.show()
# ---------------------

# What is the median of the column `ConvertedComp`?
median_converted_comp = df["ConvertedComp"].median()
print("Median of the 'ConvertedComp' column:", median_converted_comp)
# ----------------------

# How many responders identified themselves only as a **Man**?
# Filter the data to include only responders who identified as "Man"
man_responders = df[df["Gender"] == "Man"]
# Get the number of responders who identified as "Man"
num_man_responders = len(man_responders)
print("Number of responders who identified as 'Man':", num_man_responders)
# ----------------------

# Find out the  median ConvertedComp of responders identified themselves only as a **Woman**?
# Filter the data to include only responders who identified as "Woman"
woman_responders = df[df["Gender"] == "Woman"]
# Calculate the median of "ConvertedComp" for responders who identified as "Woman"
median_converted_comp_woman = woman_responders["ConvertedComp"].median()
print("Median ConvertedComp for responders who identified as 'Woman':", median_converted_comp_woman)
# -----------------------

# Calculate the five-number summary for the "Age" column
five_num_summary_age = df["Age"].describe().loc[['min', '25%', '50%', '75%', 'max']]
print("Five-number summary for the 'Age' column:")
print(five_num_summary_age)
# -----------------------

# Plot the histogram of the "Age" column
plt.figure(figsize=(10, 6))
plt.hist(df["Age"], bins=20, color='green', edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Histogram of Age")
plt.show()
# -----------------------

# Find out if outliers exist in the column `ConvertedComp` using a box plot?
Converted_Comp = df['ConvertedComp']
Converted_Comp.plot(kind = 'box')
plt.xlabel("Converted Compensation")
plt.title("Box Plot of Converted Compensation")
plt.show()
# -----------------------

# Find out the Inter Quartile Range for the column `ConvertedComp`.
# Calculate the Interquartile Range (IQR) for the "ConvertedComp" column
Q1 = df["ConvertedComp"].quantile(0.25)
Q3 = df["ConvertedComp"].quantile(0.75)
iqr = Q3 - Q1
print("Interquartile Range (IQR) for the 'ConvertedComp' column:", iqr)
# ------------------------

# Calculate the lower and upper bounds
lower_bound = Q1 - 1.5 * iqr
upper_bound = Q3 + 1.5 * iqr
print("Lower bound for potential outliers:", lower_bound)
print("Upper bound for potential outliers:", upper_bound)
# ------------------------

# Identify how many outliers are there in the `ConvertedComp` column.
# Find the outliers in the "ConvertedComp" column
outliers = df[(df["ConvertedComp"] < lower_bound) | (df["ConvertedComp"] > upper_bound)]
# Count the number of outliers
num_outliers = len(outliers)
print("Number of outliers in the 'ConvertedComp' column:", num_outliers)
# ------------------------

# Create a new dataframe by removing the outliers from the `ConvertedComp` column.
# Create a new DataFrame without outliers
df_no_outliers = df[(df["ConvertedComp"] >= lower_bound) & (df["ConvertedComp"] <= upper_bound)]
# Display the new DataFrame without outliers
print(df_no_outliers)
# ------------------------

# --------------- > ### Finding correlation

# Find the correlation between `Age` and all other numerical columns.

# Select only the numerical columns from the new DataFrame
numerical_columns = df_no_outliers.select_dtypes(include=['int64', 'float64'])
# Calculate the correlation between "Age" and all other numerical columns in the new DataFrame
correlation_no_outliers = numerical_columns.corrwith(df_no_outliers["Age"])
# Display the correlation
print("Correlation between 'Age' and all other numerical columns in the new DataFrame without outliers:")
print(correlation_no_outliers)
# ----------------

median_converted_comp = df_no_outliers["ConvertedComp"].mean()
print("Median of the 'ConvertedComp' column:", median_converted_comp)