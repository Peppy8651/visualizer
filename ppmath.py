import numpy as np




class numHandler:
    def __init__(self):
        self.RealMin = -2
        self.RealMax = 2
        self.ImagMin = -1
        self.ImagMax = 1


        self.ImgGrid = np.arange(self.ImagMin, self.ImagMax, 0.05)
        self.RealGrid = np.arange(self.RealMin, self.RealMax, 0.05)

        self.CompGrid = np.zeros((len(self.RealGrid), len(self.ImgGrid)), dtype=np.complex64)
        for j in range(len(self.ImgGrid)) :
            for i in range(len(self.RealGrid)) :
                self.CompGrid[i][j] = complex(self.RealGrid[i], self.ImgGrid[j])

    def runMandelbrot(self, c):
        z = 0
        for i in range(100) :
            z = z**2 + c
            if (np.abs(z) > 4) :
                return False
                break;
        return True
