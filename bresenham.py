import cv2 as cv
import numpy as np
import time

def bresenham(x0,y0,x1,y1):
    start = time.time()
    blank = np.zeros((1080,1920,3), dtype="uint8")
    dx = abs(x1-x0)
    dy = abs(y1-y0)
    p = 2*dy - dx
    incE = 2*dy
    incNE = 2*(dy-dx)
    if x0 > x1:
        x = x1
        y = y1
        xend = x0
    else:
        x = x0
        y = y0
        xend = x1
    for i in range(x, xend):
        blank[x,y] = (51, 222, 255)
        print('x = ', x, 'y = ', y)
        x = x + 1 if x < x1 else x - 1
        if p < 0:
            p += incE
        else:
            y = y + 1 if y < y1 else y - 1
            p += incNE
    cv.imshow("Yellow", blank)
    end = time.time()
    print("Tiempo de ejecucion", end-start)
    cv.waitKey(0)

def main():
    bresenham(200,20,300,800)
    
if __name__ == '__main__':
    main()
    