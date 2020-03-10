import os
from matplotlib.image import imread
import numpy as np

def read_dataset(data_src):
    X = []
    y = []
    for directory in os.listdir(data_src):
        try:
            for pic in os.listdir(os.path.join(data_src, directory)):
                img = imread(os.path.join(data_src, directory, pic))
                X.append(np.squeeze(np.asarray(img)))
                print(np.asarray(img))
                y.append(directory)
        except Exception as e:
            print('Failed to read images from Directory: ', directory)
            print('Exception Message: ', e)
    print('Dataset loaded successfully.')
    return X,y

data_src = "./data_src"
read_dataset(data_src)