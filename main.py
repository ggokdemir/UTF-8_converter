#manipulator.py Author:ggokdemir@splunk

import csv
import json

# May take logs directory as command input
file_location = "MY_FILE_LOCATION"

def row_to_json(row):
    print('Inside of the row')
    json_object = json.loads(row)
    #json_object[]

def opener():   
    print('Inside of the opener.')
    with open('source.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_to_json(row)            
            #Instead of printing, rows are going to be saved as json objects.
            #print(row)

#main 
opener()
    
