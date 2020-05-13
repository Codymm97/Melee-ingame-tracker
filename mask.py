import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import keras

img = cv2.imread('frame82.jpg')
player1 = img[430:480, 90:152]
# player2 = img[430:480, 175:240]
# player3 = img[430:480, 260:320]
# player4 = img[430:480, 370:430]
# player1 = np.concatenate((player1,player2),axis=1)
# player1 = np.concatenate((player1,player3),axis=1)
# player1 = np.concatenate((player1,player4),axis=1)  
cv2.imshow('image',player1)
cv2.waitKey(0)
cv2.imwrite('temp.jpg',player1)
cv2.destroyAllWindows()