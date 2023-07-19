import requests # you need this module to make an API call

#Import required libraries
import pandas as pd
import json

api_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
response = requests.get(api_url)
if response.ok:             
    data = response.json()
    
#Function for count python jobs
def get_number_of_jobs_T(technology):
    count = 0 
    for entry in data:
        key_skills = entry.get('Key Skills', '').lower()
        if technology.lower() in key_skills:
            count +=1
    return technology,count
print (get_number_of_jobs_T("Python"))

#Function for count jobs in each location
def get_number_of_jobs_L(location):
    count1 = 0
    for entry in data:
        location_counter = entry.get('Location','').lower()
        if location.lower() in location_counter:
            count1 +=1
    return location, count1

Locations = []
for entry in data:
    locationsi = entry.get('Location', '').upper()
    if locationsi not in Locations:
        Locations.append(locationsi)

for letter in Locations:
    print (get_number_of_jobs_L(letter))
