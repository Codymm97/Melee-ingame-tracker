import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras

"""
I think that it might be possible to run the Go mask adn the players Mask. 
This will cut down on the possible error of damage being done within seconds of
GO appearing. Once GO is found, the mask will stop showing the center of the
screen and just make the found areas of the percentages visible to help
the number detection from going crazy.
"""

def scanAndMaskGo():
    #TODO: takes in a frame of the match. It will mask everything but the middle of the
    #screen.
    pass

def scanAndMaskplayers():
    #TODO: takes in a frame and tries to find the places where the ingame percentages are
    #once found, 1 of 6 masks will be applied to every frame frame until the match is over.
    pass

def findGo():
    #TODO: will constantly scan frames until "GO!" is found. This will then return
    #a bool to let the program know when to find percentages
    pass

def getGamePercentages():
    #TODO: Uses object detection in order to find and identify numbers
    #Once the numbers are found, the classifier will then push those numbers
    #onto 2 different lists that will hold the data from the match.
    #These numbers will be updated every .25, .5, or 1 second. 
    pass

def plotGameData():
    #TODO: Once the match is over, this functions runs off of the two lists.
    #This function will then plot that data with the left most player in Red
    #and Right most player in Blue.
    #This will also save the plot as a picture
    pass

def main():
    #mask()
    #while(!Go)
    #   go = findgo()
    #   if(go == true)
    #       updateMask()
    #while(game == true)
    #   getGamePercentages()
    #plotGameData()
    pass