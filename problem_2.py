#!/usr/bin/env python3

### Problem 2

print("\nProblem #2:")
water_level_obs = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv') # Load in the csv file

water_level_list_raw = []   # Making an empty variable for the water level list
for line in water_level_obs:
    line = line.strip() # Removing spaces
    cols = line.split(',')  # Setting the delimiter from the csv
    water_level_observation = cols[1]    # Extracting water level measurements
    water_level_list_raw.append(water_level_observation)    # Appending new observations to the water level list

water_level_list_header_removed=water_level_list_raw[1:]    # Removing the header
water_level_list_non_blank_strings = [] # Setting a blnak variable
for i in range(0,len(water_level_list_header_removed)): # Making a for loop to remove blank strings
   if water_level_list_header_removed[i] != '':
        water_level_list_non_blank_strings.append(water_level_list_header_removed[i])
water_level_list_num = []   # Setting a blank variable
for i in range(0,len(water_level_list_non_blank_strings)):  # Making a for loop to convert strings to floating points
   water_level_list_num.append(float(water_level_list_non_blank_strings[i]))
lowest_water_level = min(water_level_list_non_blank_strings)
highest_water_level = max(water_level_list_non_blank_strings)
average_water_level = str(round(sum(water_level_list_num)/len(water_level_list_num),3))

water_level_obs = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv') # Load in the csv file once more

for line in water_level_obs:
    line = line.strip() # Removing spaces
    cols = line.split(',')  # Setting the delimiter from the csv
    water_level_observation = cols[1]    # Extracting water level measurements
    if highest_water_level in water_level_observation:  # Checking for the highest value in the list of observations
        date_of_highest_observation = cols[0]   # Extracting the corresponding date

water_level_obs = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv') # Load in the csv file once more

for line in water_level_obs:
    line = line.strip() # Removing spaces
    cols = line.split(',')  # Setting the delimiter from the csv
    water_level_observation = cols[1]    # Extracting water level measurements
    if lowest_water_level in water_level_observation:  # Checking for the highest value in the list of observations
        date_of_lowest_observation = cols[0]   # Extracting the corresponding date

print("The highest water level was " + highest_water_level + ", observed on " + date_of_highest_observation[0:9] + ".")
print("The lowest water level was " + lowest_water_level + ", observed on " + date_of_lowest_observation[0:9] + ".")
print("The average water level is " + average_water_level + ".\n")

