import cv2 as cv
import numpy as np

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
    print(steps)
    for i in range(0, steps):
        print('x = ',round(x), 'y = ', round(y))         
        blank[roundDif(x-grosor/2, grosor):roundDif(x+grosor/2,grosor), roundDif(y-grosor/2,grosor):roundDif(y+grosor/2,grosor)] = (0,255,10)
        if ys == 1: 
            y += grosor
            x += grosor*xs
        else:
            x += grosor 
            y += grosor*ys
        
    cv.imshow("Green", blank)
    cv.waitKey(0)
    
def roundDif(n, c):
    if(n %c < c/2):
        result = n
    else:
        result = n-(n%c)+c
    return int(result)
    
def main():
    dda(56,100,90,160,14)

if __name__ == '__main__':
    main()

