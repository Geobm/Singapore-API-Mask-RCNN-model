
### This repository uses Singapore's public [API](https://data.gov.sg/dataset/traffic-images) information from real-time traffic. 

#### About this dataset

Returns links to images of live traffic conditions along expressways and Woodlands & Tuas Checkpoints.
|  Managed By  | [Land Transport Authority](https://data.gov.sg/dataset?organization=land-transport-authority)       |
|------------|--------------------------------|
| Last Updated | February 13, 2018, 14:49 (SGT) |
|    Created   | April 8, 2016, 15:55 (SGT)     |
|   Coverage   | From March 1, 2016             |
|   Frequency  | Real-time                      |
|   Source(s)  | Land Transport Authority       |
|    Licence   | [Singapore Open Data Licence](https://data.gov.sg/open-data-licence)    |

#### API Example value

```
{
  "api_info": {
    "status": "healthy"
  },
  "items": [
    {
      "timestamp": "2020-06-15T17:30:38.245Z",
      "cameras": [
        {
          "timestamp": "2020-06-15T17:30:38.245Z",
          "camera_id": 0,
          "image_id": 0,
          "image": "string",
          "image_metadata": {
            "height": 0,
            "width": 0,
            "md5": "string"
          }
        }
      ]
    }
  ]
}
```

