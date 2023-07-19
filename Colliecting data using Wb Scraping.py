from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import csv

url = "http://www.ibm.com"
# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text 
soup = BeautifulSoup(data,"html5lib")  # create a soup object using the variable 'data'

for link in soup.find_all('a'):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))
    
for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link.get('src'))

#The below url contains a html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
soup = BeautifulSoup(data,"html5lib")

#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>
#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].getText() # store the value in column 3 as color_name
    color_code = cols[3].getText() # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))
    
    
#this url contains the data you need to scrape
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text 
soup = BeautifulSoup(data,"html5lib")  # create a soup object using the variable 'data'

language_data = []
#Scrape the `Language name` and `annual average salary`.
table = soup.find('table') # in html table is represented by the tag <table>
#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    Language_name = cols[1].getText() # store the value in column 3 as color_name
    Annual_average_salary = cols[3].getText() # store the value in column 4 as color_code
    language_data.append([Language_name, Annual_average_salary])

# Save the data to a CSV file
csv_filename = "programming_languages.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Language Name", "Annual Average Salary"])  # Write header
    writer.writerows(language_data)

print("Data saved to", csv_filename)
