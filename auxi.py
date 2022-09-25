import cv2 as cv
import numpy as np
import time

def dda(x0,y0,x1,y1, grosor):
    blank = np.zeros((1080,1920,3), dtype="uint8")
    x, y = x0, y0
    dx = x1-x0
    dy = y1-y0
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    xs = dx / steps
    ys = dy / steps 
    for i in range(0, steps+grosor):    
        print('x = ',round(x), 'y = ', round(y))   
        blank[round(x-grosor/2):round(x+grosor/2), round(y-grosor/2):round(y+grosor/2)] = (0,255,10)
        if xs == 1:
            x += xs
            y += grosor+ys
        else:
            x += grosor+xs 
            y += ys 
    cv.imshow("Green", blank)
    cv.waitKey(0)
    
def main():
    dda(125,150,300,210,5)

if __name__ == '__main__':
    main()