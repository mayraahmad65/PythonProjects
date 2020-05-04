import cv2
from numba import jit
import numpy as np
def AdaptiveThreshold(inputM,s,T = 0.15):  
    outputM=np.zeros(inputM.shape)
    nRow = inputM.shape[0]
    nCol = inputM.shape[1]
    S = int(max(nRow, nCol) / 8)

    s2 = int(S / 4)

    for i in range(nRow):
        y1 = i - s2
        y2 = i + s2

        if (y1 < 0) :
            y1 = 0
        if (y2 >= nRow):
            y2 = nRow - 1

        for j in range(nCol):
            x1 = j - s2
            x2 = j + s2

            if (x1 < 0) :
                x1 = 0
            if (x2 >= nCol):
                x2 = nCol - 1
            count = (x2 - x1)*(y2 - y1)

            sum=s[y2][x2]-s[y2][x1]-s[y1][x2]+s[y1][x1]

            if ((int)(inputM[i][j] * count) < (int)(sum*(1.0 - T))):
                outputM[i][j] = 255
    return outputM

@jit(nopython=True)
def adaptiveThreshold1(inputMat,s,T = 0.15):
    outputMat=np.zeros(inputMat.shape)
    nRow = inputMat.shape[0]
    nCol = inputMat.shape[1]
    S = int(max(nRow, nCol) / 8)

    s2 = int(S / 4)

    for i in range(nRow):
        y1 = i - s2
        y2 = i + s2

        if (y1 < 0) :
            y1 = 0
        if (y2 >= nRow):
            y2 = nRow - 1

        for j in range(nCol):
            x1 = j - s2
            x2 = j + s2

            if (x1 < 0) :
                x1 = 0
            if (x2 >= nCol):
                x2 = nCol - 1
            count = (x2 - x1)*(y2 - y1)

            sum=s[y2][x2]-s[y2][x1]-s[y1][x2]+s[y1][x1]

            if ((int)(inputMat[i][j] * count) < (int)(sum*(1.0 - T))):
                outputMat[i][j] = 255
                
    return outputMat

if __name__ == '__main__':
    ratio=1
    image = cv2.imdecode(np.fromfile('sudoku.jpeg', dtype=np.uint8), 0)
    img = cv2.resize(image, (int(image.shape[1] / ratio), int(image.shape[0] / ratio)), cv2.INTER_NEAREST)

    retval, adap = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
    cv2.imwrite('thresh_results.jpg',adap)

cv2.imwrite('results.jpg', np.uint8(thresh))

cv2.waitKey(0)
cv2.destroyAllWindows()