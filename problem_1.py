#!/usr/bin/env python3

print(f"\nProblem #1:")
### Problem 1

water_level_obs = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv') # Load in the csv file

water_level_list = []   # Making an empty variable for the water level list
for line in water_level_obs:      
    line = line.strip() # Removing spaces
    cols = line.split(',')  # Setting the delimiter from the csv
    water_level_observation = cols[1]    # Extracting water level measurements
    water_level_list.append(water_level_observation)    # Appending new observations to the water level list

highest_water_level = max(water_level_list)
water_level_obs = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv') # Load in the csv file once more

for line in water_level_obs:
    line = line.strip() # Removing spaces
    cols = line.split(',')  # Setting the delimiter from the csv
    water_level_observation = cols[1]    # Extracting water level measurements
    if highest_water_level in water_level_observation:  # Checking for the highest value in the list of observations
        date_of_observation = cols[0]   # Extracting the corresponding date

print("The highest water level was " + highest_water_level + ", observed on " + date_of_observation[0:9] + ".\n")
