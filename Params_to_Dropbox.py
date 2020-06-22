#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 14:20:00 2020
@author: GeovaniBM
"""
import requests
import datetime
import itertools
import dropbox
import sys
#Function to upload a file to dropbox
def uploadToDropbox(): 
    dbx = dropbox.Dropbox('***TOKEN***') #Generate you access token with OAuth guide from dropbox developers documentation
    rootdir = 'C:/Users/Issstezac1/Desktop/DropboxTest/' #Local path
    print ("Attempting to upload...")
    # walk return first the current folder that it walk, then tuples of dirs and files not "subdir, dirs, files"
    for dir, dirs, files in os.walk(rootdir):
        for file in files:
            try:
                file_path = os.path.join(dir, file)
                dest_path = os.path.join('/', file) #root folder of dropbox app
                print('Uploading %s to %s' % (file_path, dest_path))
                with open(file_path, "br") as f:
                    dbx.files_upload(f.read(), dest_path, mute=True)
                print("Finished upload.")
            except Exception as err:
                print("Failed to upload %s\n%s" % (file, err))

#Function to obtain URLS of every camera
def getURLS(date_format):
    for i in range(len(date_format)):
        url_date = date_format[i].replace('/','-') #Adjust timestamps to correct url format
        endpoint = "https://api.data.gov.sg/v1/transport/traffic-images?date_time="+url_date
        data = requests.get(endpoint)
        if (data):
            data = requests.get(endpoint).json()
            cam_list = extract_values(data,'camera_id')#Extract values as lists
            images_list = extract_values(data, 'image')#Extract values as lists
            
            #write URL images into csv 
            with open("C:/Users/Issstezac1/Desktop/DropboxTest/test.txt","a") as f:
                #f.write(endpoint)
                for item in images_list:
                    f.write("%s,\n" % item)
                    
            for i in range(len(cam_list)): #Merge camera's id and correspondent image into a list
                if i % 2 == 0:
                    list1 = cam_list
                    list2 = images_list
                    for n in range(len(list1)):
                        combined_list.append([list1[n],list2[n]])
            #print(combined_list)
               
#Function to extract parameters from JSON
def extract_values(obj, key):
    #Pull all values of specified key from nested JSON.
    arr = []

    def extract(obj, arr, key):
        #Recursively search for values of key in JSON tree.
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results


if __name__ == "__main__":    
    string_date_list = []   
    combined_list=[]
    
    #Generate timestamps every N minutes. Parameters can be modified  
    initial_time = datetime.datetime(2020, 1, 1, 0, 0)
    final_time = datetime.datetime(2020, 1, 2, 0, 0)
    delta = datetime.timedelta(minutes=360) #6 hours delta
    times = []
    
    while initial_time < final_time:
        times.append(initial_time)
        initial_time += delta
    
    #Convert datetime objects to string list     
    for i in range(len(times)):
        string_date_list.append((times[i].strftime('%Y/%m/%dT%H:%M:%S')))
    #print(string_date_list)
    getURLS(string_date_list)
    uploadToDropbox()
