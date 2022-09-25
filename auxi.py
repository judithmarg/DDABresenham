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
        
        y += grosor+ys
        x += grosor+xs 
    cv.imshow("Green", blank)
    cv.waitKey(0)
    
def main():
    dda(150,125,170,180,5)

if __name__ == '__main__':
    main()