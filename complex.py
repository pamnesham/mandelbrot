
#This class creates complex numbers and methods for working with them
class Complex:
    #constructor
    def __init__(self, real = 0.0, imag = 0.0):
        self.__real = float(real)
        self.__imag = float(imag)

    #return complex number as a string
    def __repr__(self):
        if self.__imag == 0 or self.__imag == None:
            cplexStr = str(self.__real)
        elif self.__imag < 0:
            cplexStr = str(self.__real) + str(" - ") + str(self.__imag*-1) + str("i")
        else:
            cplexStr = str(self.__real) + str(" + ") + str(self.__imag) + str("i")
        return cplexStr

    #returns the real part of the complex number
    def getReal(self):
        return self.__real

    #returns the imaginary part of the complex number
    def getImag(self):
        return self.__imag

    #changes the real part of the complex number
    def setReal(self, newReal):
        self.__real = newReal

    #changes the imaginary part of the complex number
    def setImag(self, newImag):
        self.__imag = newImag

    #adds complex numbers together
    def __add__(self, rhand):
        self.__real += rhand.__real
        self.__imag += rhand.__imag
        return Complex(self.__real, self.__imag)

    #multiplies complex numbers together using foil
    def __mul__(self, rhand):
        front = self.__real * rhand.__real
        outer = self.__real * rhand.__imag
        inner = self.__imag * rhand.__real
        last = self.__imag * rhand.__imag
        inner = inner + outer
        last = last * (-1)
        front = front + last
        self.__real = front
        self.__imag = inner
        return Complex(self.__real, self.__imag)

    #finds the absolute value of a complex number
    def __abs__(self):
        a = self.__real**2
        b = self.__imag**2
        c = a+b
        absol = c**.5
        return absol
