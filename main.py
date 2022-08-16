#manipulator.py Author:ggokdemir@splunk

import csv
import re
import json
from traceback import print_tb
from urllib.parse import unquote


# May take logs directory as command input
file_location = "MY_FILE_LOCATION"


def search_link(row):
    print('Inside of the row. \n Line:')

    
    #Find the link.

    row_string = json.dumps(row)

    if(finder(row_string)):
        #print(row_string[row_string.find("\"referer\":\"https://www.aljazeera.net/"):row_string.find("reqHost")-6])
        print(row_string[row_string.find("https://www.aljazeera.net/news/"):row_string.find("reqHost")-6])

        print(decoder(row_string[row_string.find("https://www.aljazeera.net/news/"):row_string.find("reqHost")-6]))
    else:
        print("Link not found.")
        #print("\"referer\":\"https://www.aljazeera.net/")
    print(" ")
    
def dont_search_link(row):
    row_string = json.dumps(row)
    print(decoder(row_string))

def finder(row_string):

    #return_regex = re.search("(?P<url>https?://[^\s]+)", row_string).group("url")
    #print(re.search("(?P<url>https?://[^\s]+)", row_string).group("url"))

    #return_find = (row_string.find("\"referer\":\"https://www.aljazeera.net/")!= -1)
    return_find = (row_string.find("https://www.aljazeera.net/news/")!= -1)
    

    return return_find
    #return return_regex

    
def decoder(url):
    
    return unquote(url)

    
def opener():   
    print('Inside of the opener.')
    with open('source.csv', newline='') as srcfile:
        reader = csv.DictReader(srcfile)
        

        #Send lines to the function
        for row in reader:
            #search_link(row)
            dont_search_link(row)
            writer(row)          
            #Instead of printing, rows are going to be saved as json objects.

def writer(new_row):
    print("Started to write.")
    with open('destination.csv', 'w', newline='') as dstfile:
        
        writer = csv.DictWriter(new_row)
        

#main 
opener()

#test the decoder function
#print(decoder("https://www.aljazeera.net/news/politics/2022/7/19/%D8%AD%D8%B1%D8%A8-%D8%A3%D9%88%D9%83%D8%B1%D8%A7%D9%86%D9%8A%D8%A7-%D8%A7%D9%84%D9%82%D8%B5%D9%81-%D8%A7%D9%84%D8%B1%D9%88%D8%B3%D9%8A-%D9%8A%D9%88%D9%82%D8%B9-%D8%B6%D8%AD%D8%A7%D9%8A%D8%A7"))
    
