import cv2 as cv
import numpy as np
import time

def dda(x0,y0,x1,y1):
    start = time.time()
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
    for i in range(0, steps+1):    
        print('x = ',round(x), 'y = ', round(y))   
        blank[round(x),round(y)] = (0,255,10)
        x = x + xs
        y = y + ys
    cv.imshow("Green", blank)
    end = time.time()
    print("Tiempo de ejecucion", end-start)
    cv.waitKey(0)
    
def main():
    dda(200,20,300,800)

if __name__ == '__main__':
    main()
    

