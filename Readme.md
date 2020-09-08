
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

### Mask R-CNN Theory

Mask R-CNN is an instance segmentation technique which locates each pixel of every object in the image instead of the bounding
boxes. It has two stages: region proposals and then classifying the proposals and generating bounding boxes and masks. It does
so by using an additional fully convolutional network on top of a CNN based feature map with input as feature map and gives 
matrix with 1 on all locations where the pixel belongs to the object and 0 elsewhere as the output.


Backbone is a [FPN](https://arxiv.org/abs/1612.03144) style deep neural network. It consists of a bottom-up pathway , a top-bottom
pathway and lateral connections. Bottom-up pathway can be any ConvNet, which extracts features from raw images. Top-bottom pathway 
generates feature pyramid map which is similar in size to bottom-up pathway. Lateral connections are convolution and adding operations 
between two corresponding levels of the two pathways. FPN outperforms other single ConvNets mainly for the reason that it maintains 
strong semantically features at various resolution scales.

### Image segmentation 
Partitioning a digital image into multiple segments (sets of pixels, also known as image objects). The goal of segmentation is to 
simplify and/or change the representation of an image into something that is more meaningful and easier to analyze. In particular, 
Mask R-CNN performs **instance segmentation** which means that different instances of the same type of object in the input
image, for example, car, should be assigned distinct labels. **This project is mainly focused on car and trucks image segmentation.
Hence, to have a cuantitative measure of the traffic in Singapore expressways, Woodlands & Tuas Checkpoints before and during the 
global pandemic.**

### Mask R-CNN model 

![Architecture](https://miro.medium.com/proxy/1*IWWOPIYLqqF9i_gXPmBk3g.png)

### Data Flow
![Data FLow](https://miro.medium.com/max/698/1*aMRoAN7CtD1gdzTaZIT5gA.png)

FPN composes of a bottom-up and a top-down pathway. The bottom-up pathway is the usual convolutional network for feature extraction.
As we go up, the spatial resolution decreases. With more high-level structures detected, the semantic value for each layer increases.
