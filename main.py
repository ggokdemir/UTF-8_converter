#manipulator.py Author:ggokdemir@splunk

import csv
import re
import json
from traceback import print_tb

# May take logs directory as command input
file_location = "MY_FILE_LOCATION"

def search_link(row):
    print('Inside of the row.')
    #Find the link.

    row_string = json.dumps(row)
    
    if(row_string.find("https://www.aljazeera.net/news/2")!= -1):
        print(row_string[row_string.find("https://www.aljazeera.net/news/2"):row_string.find("reqHost")-6])
    else:
        print("Link not found.")
        
    print(" ")

    
def encoder(data):
    return data.encode('cp1252').decode('cp1256')

    
def opener():   
    print('Inside of the opener.')
    with open('source.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            search_link(row)            
            #Instead of printing, rows are going to be saved as json objects.


#main 
opener()

print(encoder("Óæí Ïæã ÈíåÞí"))
    
