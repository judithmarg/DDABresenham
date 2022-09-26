import cv2 as cv
import numpy as np

def bresenham(x0,y0,x1,y1,grosor):
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
        yend = y0
    else:
        x = x0
        y = y0
        xend = x1
        yend = y1
    for i in range(x, xend*grosor):
        blank[int(x-grosor/2) : int(x+grosor/2), int(y-grosor/2):int(y+grosor/2)] = (51, 222, 255)
        print('x = ', x, 'y = ', y)
        x = x + grosor if x < xend*grosor else x - grosor
        if p < 0:
            p += incE
        else:
            y = y + grosor if y < yend*grosor else y - grosor
            p += incNE
    cv.imshow("Yellow", blank)
    cv.waitKey(0)

def main():
    bresenham(200,20,205,800,3)
    
if __name__ == '__main__':
    main()