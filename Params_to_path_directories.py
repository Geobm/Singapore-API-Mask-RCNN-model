# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 13:20:00 2020

@author: GeovaniBM
"""
import os
import ntpath
import shutil
import requests
import datetime

#Function to obtain images of every camera
def getImages(date_format):

    for i in range(len(date_format)):
        url_date = date_format[i].replace('/','-') #Adjust timestamps to correct url format
        endpoint = "https://api.data.gov.sg/v1/transport/traffic-images?date_time="+url_date
        data = requests.get(endpoint)

    #check http status of dates list
    if (data):
        print("Request OK")
        data = requests.get(endpoint).json()
        output_data_path = "C:/Users/Issstezac1/Desktop/output_data"

        if not os.path.exists(output_data_path): # check for is dictionary exists
            os.mkdir(output_data_path) # create the dictionary if not exists
        
        for record in data["items"][0]["cameras"]:
            camera_id = record["camera_id"]
            image_location = record["image"]
            image_name = ntpath.basename(image_location)
            if not os.path.exists(f"{output_data_path}/{camera_id}"):
                os.mkdir(f"{output_data_path}/{camera_id}")
        
            image_data = requests.get(image_location, stream=True) # get the source of image
            with open(f"{output_data_path}/{camera_id}/{image_name}", 'wb') as image_file:
                shutil.copyfileobj(image_data.raw, image_file) # write the source into a file
            #print("Downloaded an image for camera id:", camera_id) 
    else:
            print("Response Failed try a valid date")
            exit()

def getLimitDate(year, month, day):#function to get next day as limit date

    if (year % 400 == 0):
        leap_year = True
    elif (year % 100 == 0):
        leap_year = False
    elif (year % 4 == 0):
        leap_year = True
    else:
        leap_year = False
    
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30
    
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    return year, month, day
           
if __name__ == "__main__":
    #internal vars
    year =int(input("Type the timestamp\n\nYear: "))
    month = int(input("Month : "))
    day = int(input("Day : "))
    hour = int(input("Hour:"))
    mins =int(input("Minutes:"))
    string_date_list = []
    
    #get new limit date vars
    n_year, n_month, n_day = getLimitDate(year, month, day)
    #Generate timestamps every 5 minutes. The minutes parameter of the delta variable can be adjusted 
    initial_time = datetime.datetime(year, month, day, mins, 0)
    final_time = datetime.datetime(n_year, n_month, n_day, 0, 0)
    delta = datetime.timedelta(minutes=5)
    times = []
    
    while initial_time < final_time:
        times.append(initial_time)
        initial_time += delta
    
    #Convert datetime objects to string list     
    for i in range(len(times)):
        string_date_list.append((times[i].strftime('%Y/%m/%dT%H:%M:%S')))
        getImages(string_date_list)
        