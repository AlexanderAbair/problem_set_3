#!/usr/bin/env python3

print(f"\nProblem #3:")
### Problem 3

water_level_obs = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv') # Load in the csv file once more

water_level_list_raw = []   # Making an empty variable for the water level list
for line in water_level_obs:
    line = line.strip() # Removing spaces
    cols = line.split(',')  # Setting the delimiter from the csv
    water_level_observation = cols[1]    # Extracting water level measurements
    water_level_list_raw.append(water_level_observation)    # Appending new observations to the water level list

water_level_list_header_removed = water_level_list_raw[1:]  # Removing header

water_level_list_non_blank_strings = [] # Setting a blank variable
for i in range(0,len(water_level_list_header_removed)): # Making a for loop to fix blank strings
    if water_level_list_header_removed[i] != '':    
        water_level_list_non_blank_strings.append(water_level_list_header_removed[i])
    if water_level_list_header_removed[i] == '':    # Interpolating a value for the blank string
        interpolated_level = '6.406'
        water_level_list_non_blank_strings.append(interpolated_level)   # Rplacing the blank string with the interpolated string

water_level_list_num = []   # Setting a blank variable for a list of numbers
for i in range(0,len(water_level_list_non_blank_strings)):  # Making a for loop to convert strings to floating points
   water_level_list_num.append(float(water_level_list_non_blank_strings[i]))

water_level_difference_list = []    # Setting a blank value for water level differences
for i in range(0,len(water_level_list_num)-1):  # Making a for loop to calculate differences between successive water levels
    water_level_difference = (water_level_list_num[i+1]-water_level_list_num[i])
    water_level_difference_list.append(water_level_difference)

fastest_level_rise = max(water_level_difference_list)

water_level_obs = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv') # Load in the csv file once more

dates_of_observation_with_header = []   # Setting a blank variable
for line in water_level_obs:
    line = line.strip() # Removing spaces
    cols = line.split(',')  # Setting the delimiter from the csv
    observation_date = cols[0]    # Extracting water level measurements
    dates_of_observation_with_header.append(observation_date)  

dates_of_observation = dates_of_observation_with_header[1:] # Removing the header

for i in range(0,len(water_level_difference_list)): # Making a for loop to determine the fastest rise and the date thereof
    if fastest_level_rise == water_level_difference_list[i]:
        print("The fastest water level rise was " + str(fastest_level_rise) + " on " + dates_of_observation[i+1] +".\n")
