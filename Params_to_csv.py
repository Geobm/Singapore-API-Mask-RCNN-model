# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:48:00 2020

@author: GeovaniBM
"""

import json 
import csv
import requests

path = "C:/Users/Issstezac1/Desktop"
endpoint = "https://api.data.gov.sg/v1/transport/traffic-images"

"""response from API URL"""
get_req = requests.get(endpoint)

"""Transform json input to python objects""" 
data = json.loads(get_req.text)

##Prints all the json data
##print(data.get('items'))

def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
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

"""list of parameters"""
cam_list = extract_values(data,'camera_id')
images_list = extract_values(data, 'image')

"""writing data list into csv file """
with open('C:/Users/Issstezac1/Desktop/test.csv', 'w+', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(cam_list)
    wr.writerow(images_list)
    