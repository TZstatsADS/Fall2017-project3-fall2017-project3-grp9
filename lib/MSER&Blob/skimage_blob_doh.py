#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 21:35:28 2017

@author: KathrynL
"""


'''
reference:
    
http://scikit-image.org/docs/dev/auto_examples/features_detection/plot_blob.html
'''
from skimage.feature import blob_doh

from skimage.color import rgb2gray
from os import listdir
import cv2
import pandas as pd
import numpy as np

img_path="/Users/luoxin/Desktop/training_set/images/"

img_names=listdir(img_path)[1:]
blob_df=[]
for i in range(len(img_names)):
    print(i)
    image=cv2.imread(img_path+img_names[i])
    image=cv2.resize(image,(256,256),interpolation = cv2.INTER_LINEAR)
    image_gray = rgb2gray(image)
    blobs_doh = blob_doh(image_gray, max_sigma=50, threshold=.01)
    blobs_doh=blobs_doh.tolist()
    for x in blobs_doh:
        x.append(i+1)
    blob_df.extend(blobs_doh)
    
blob_DF=pd.DataFrame(np.array(blob_df))
blob_DF.columns=("X","Y","radius","image")
blob_DF.to_csv("/Users/luoxin/Desktop/[ADS]Advanced Data Science/Fall2017-project3-fall2017-project3-grp9/data/blob_df.csv",index=False)
'''
make k-means classification
'''
from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=200).fit(blob_df[["X","Y",'radius']])
blob_df['label']=kmeans.labels_


blob_df.to_csv("/Users/luoxin/Desktop/[ADS]Advanced Data Science/Fall2017-project3-fall2017-project3-grp9/data/blob_df.csv",index=False)



#plot part 
#import matplotlib.pyplot as plt   
#fig, ax = plt.subplots()  
#ax.imshow(image, interpolation='nearest')
#color="red"
#for blob in blobs_doh:
#        y, x, r = blob
#        c = plt.Circle((x, y), r, color=color, linewidth=2, fill=False)
#        ax.add_patch(c)
#plt.show()


