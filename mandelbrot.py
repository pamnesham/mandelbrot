

import turtle
from complex import *

#This class deals with the computational aspects of the Mandelbrot sequence
class Mandelbrot:
    def __init__(self, start = 0, limit = 50):
        self.__limit = int(limit)
        self.__colormap = ["papayaWhip","LightCyan", "SkyBlue", "LightSkyBlue", "DeepSkyBlue",\
         "Turquoise", "DarkTurquoise", "Aquamarine", "MediumAquamarine", "MediumSeaGreen", "PaleGreen",\
        "Linen", "Pink", "IndianRed", "Lavender", "Salmon", "Crimson", \
         "PaleVioletRed","MediumVioletRed", "HotPink", "OrangeRed", "DarkOrange", "Coral", "Orange",\
          "Gold","LemonChiffon", "PapayaWhip", "PeachPuff", "LightYellow", "black"]
        self.__cardinality = int(0)
        self.__start = Complex(start.getReal(),start.getImag())
        self.z = Complex(start.getReal(),start.getImag())
        #the following loop determines how fast a sequence escapes to infinity
        #   the lower the cardinality, the faster it escapes
        #   if all numbers within the limit (default =50) don't escape, it is in the set
        while self.__cardinality < self.__limit:
            if abs(self.z) >= 2:
                break
            else:
                self.z = (self.z*self.z) + self.__start
                self.__cardinality += 1

    # This function chooses color based on cardinality
    #   if cardinality == 1, no numbers escape to inifity and color == black
    def get_color(self):
        ratio = self.__cardinality/self.__limit
        colorRatio = 1/len(self.__colormap)
        select = 0
        for i in range(len(self.__colormap)):
            if ratio <= colorRatio:
                return self.__colormap[select]
            elif ratio == 1:
                return self.__colormap[len(self.__colormap)-1]
            else:
                select += 1
                colorRatio += 1/len(self.__colormap)
