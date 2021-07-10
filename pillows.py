#%%
#pillow library exploratory project
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image

plt.style.use('ggplot')
matplotlib.rcParams['backend'] = 'Qt5Agg'

# mistgram used with mode
def Histo(arr) -> dict:
        histogram = {}
        for i in arr:
            histogram[i] = histogram.get(i,0) + 1
        return histogram

class Img_stat:
    # we will use subrectangle for spample std deveation
    # histogram, box plot and scater plot
    # range mean mode, std dist

    def __init__(self, pic):
        self.img = Image.open(pic)
        
        self.blueBand = np.asarray(list(self.img.getdata(band=2)))
        self.blueBand.sort()
        self.blueHist = Histo(self.blueBand)
        
        self.greenBand = np.asarray(list(self.img.getdata(band=1)))
        self.greenBand.sort()
        self.greenHist = Histo(self.greenBand)

        self.redBand = np.asarray(list(self.img.getdata(band=0)))
        self.redBand.sort()
        self.redHist = Histo(self.redBand)


        if self.img.mode == "RGBA":
            self.alphaBand = np.asarray(list(self.img.getdata(band=3)))
            self.alphaBand.sort()
            self.alphaHist = Histo(self.alphaBand)
        
    
        
#Mean for blue red green and alpha

    def alpha_mean(self):
        if self.img.mode != "RGBA":
            print(0)
        else:
         self.alphaMean  = self.alphaBand.mean()
         print(self.alphaMean)
         
    def blue_mean(self):
         self.blueMean  = self.blueBand.mean()
         print(self.blueMean)
    def green_mean(self):
         self.greenMean  = self.greenBand.mean()
         print(self.greenMean)
    def red_mean(self):
         self.redMean  = self.redBand.mean()
         print(self.redMean)
    
#Range for each color band
    
    def alpha_range(self):
        if(self.img.mode != 'RGBA'):
            print("(0, 0)")
        else:
            self.alphaRange = (np.amin(self.alphaBand), np.amax(self.alphaBand))
            print(self.alphaRange)
            
    def blue_range(self):
        self.blueRange = (np.amin(self.blueBand), np.amax(self.blueBand))
        print(self.blueRange)
        
    def green_range(self):
        self.greenRange = (np.amin(self.greenBand), np.amax(self.greenBand))
        print(self.greenRange)
        
    def red_range(self):
        self.redRange = (np.amin(self.redBand), np.amax(self.redBand))
        print(self.redRange)
    
#Mode for each color band
    
    def blue_mode(self):
        self.blueMode =  max(self.blueHist, key = self.blueHist.get)
        print(self.blueMode)
         
    def green_mode(self):
        self.greenMode =  max(self.greenHist, key = self.greenHist.get)
        print(self.greenMode)     
     
    def red_mode(self):
        self.redMode =  max(self.redHist, key = self.redHist.get)
        print(self.redMode)   
    
    def alpha_mode(self):
        if(self.img.mode != 'RGBA'):
            print("N/A")
        else:
            self.alphaMode = max(self.alphaHist, key = self.alphaHist.get)
            print(self.alphaMode)

# STD Deviation

#Histogram of 5 bars incramenting by 51 
   
    def blue_histogram(self):
        plt.hist(self.blueBand, bins=5, color="blue",edgecolor ="black")
        plt.title('Blue Pixel values')
        plt.xlabel('Pixel Values')
        plt.ylabel('Total Pixels')    
        plt.show()

    def green_histogram(self):
        plt.hist(self.greenBand, bins=5, color="green",edgecolor ="black")    
        plt.title('Green Pixel values')
        plt.xlabel('Pixel Values')
        plt.ylabel('Total Pixels')    
        plt.show()

    def red_histogram(self):
        plt.hist(self.redBand, bins=5, color="red",edgecolor ='black')
        plt.title('Red Pixel values')
        plt.xlabel('Pixel Values')
        plt.ylabel('Total Pixels')    
        plt.show()

    def alpha_histogram(self):
        if(self.img.mode != "RGBA"):
            print("N/A")
        else:
            plt.hist(self.alphaBand, bins=5, color="White",edgecolor ='black')
            plt.title('Alpha Pixel values')
            plt.xlabel('Pixel Values')
            plt.ylabel('Total Pixels')    
            plt.show()    
#3D Scatter Plot 
    def scatterplot(self):
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = self.redBand
        y = self.greenBand
        z = self.blueBand

        ax.scatter(x, y, z, c='b', marker='o')

        ax.set_xlabel('Red')
        ax.set_ylabel('Green')
        ax.set_zlabel('Blue')

        plt.show()
command = ""
color = ""

img = input('Enter image file name: ')
imstat1 = Img_stat(img)

while(command != "exit"):
    command = input("Enter a command: ")
    if(command == "mean"):
        color = input("For what color? ")
        if(color == "blue"):
            imstat1.blue_mean()
        elif(color == "red"):
            imstat1.red_mean()
        elif(color == "green"):
            imstat1.green_mean()
        elif(color == "alpha"):
            imstat1.alpha_mean()
    if(command == "range"):
        color = input("For what color? ")
        if(color == "blue"):
            imstat1.blue_range()
        elif(color == "red"):
            imstat1.red_range()
        elif(color == "green"):
            imstat1.green_range()
        elif(color == "alpha"):
            imstat1.alpha_range()
    if(command == "mode"):
        color = input("For what color? ")
        if(color == "blue"):
            imstat1.blue_mode()
        elif(color == "red"):
            imstat1.red_mode()
        elif(color == "green"):
            imstat1.green_mode()
        elif(color == "alpha"):
            imstat1.alpha_mode()
    if(command == "histogram"):
        color = input("For what color? ")
        if(color == "blue"):
            imstat1.blue_histogram()
        elif(color == "red"):
            imstat1.red_histogram()
        elif(color == "green"):
            imstat1.green_histogram()
        elif(color == "alpha"):
            imstat1.alpha_histogram()
    if(command == 'scatter'):
        imstat1.scatterplot()
        
# %%
