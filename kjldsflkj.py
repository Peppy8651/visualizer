import numpy as np

RealMin = -2
RealMax = 2
ImagMin = -1
ImagMax = 1

ImgGrid = np.arange(ImagMin, ImagMax, 0.05)
RealGrid = np.arange(RealMin, RealMax, 0.05)

CompGrid = np.zeros((len(RealGrid), len(ImgGrid)), dtype=np.complex64)

for j in range(len(ImgGrid)) :
    for i in range(len(RealGrid)) :
        CompGrid[i][j] = complex(RealGrid[i], ImgGrid[j])

def TestMandelbrot(c) :
    z = 0
    for i in range(100) :
        z = z**2 + c
        if (np.abs(z) > 4) :
            return False
            break;
    return True


for j in range(len(ImgGrid)):
    for i in range(len(RealGrid)):
        if TestMandelbrot(CompGrid[i][j]) == True:
            if i == len(RealGrid) - 1:
                print('*', end = '\n')
            else:
                print('*', end = '')
        else:
            if i == len(RealGrid) - 1:
                print('-', end = '\n')
            else:
                print('-', end = '')