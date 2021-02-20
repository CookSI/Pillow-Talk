#pillow library exploratory project
import numpy as np
from PIL import Image


class Img_stat:
      # we will use subrectangle for spample std deveation
    # histogram, box plot and scater plot
    # range mean mode, std dist
    
    def __init__(self, pic):
        self.img = Image.open(pic)
        
        self.blueBand = np.asarray(list(self.img.getdata(band=2)))
        self.blueBand.sort()
        
        self.greenBand = np.asarray(list(self.img.getdata(band=1)))
        self.greenBand.sort()
        
        self.redBand = np.asarray(list(self.img.getdata(band=0)))
        self.redBand.sort()
        
        if self.img.mode == "RGBA":
            self.alphaBand = list(self.img.getdata(band=3))
            self.alphaBand.sort()
        
    
        
    #Mean for blue redd gree and alpha

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
    #Histogram of 5 bars incramenting by 51 
   


 


imstat1 = Img_stat("test.png")
imstat1.blue_mean()
imstat1.green_mean()
imstat1.red_mean()
imstat1.alpha_mean()
#print(pic.format, pic.size, pic.mode)

#Load the RGB values for every pixel in the form ((r1,b1,g1), (r2,g2,b2), ...)
#pixels = list(pic.getdata())

#pixels_blue = list(pic.getdata(band=2))

#pixels_green = list(pic.getdata(band=1))

#pixels_red = list(pic.getdata(band=0))
#print(pixels)

#print(pixels_red)