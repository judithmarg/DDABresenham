import cv2
import numpy as np
import time
 
def bresenham (x0,y0,x1,y1,grosor):
    t1 = time.time()
    blank = np.zeros((1080,1920,3),dtype="uint8")
    dx = abs(x1-x0)
    dy = abs(y1-y0)
    p = 2*dy-dx if dx > dy else 2*dx-dy
    incE = 2*dy if dx > dy else 2*dx
    incNE = 2*(dy-dx) if dx > dy else 2*(dx-dy)
    
    if (x0 > x1 and dx > dy) or (y0 > y1 and dy > dx):
        x, y = x1, y1
        xend, yend = x0, y0
        start = x
        end = xend 
    else:
        x, y = x0, y0
        xend, yend = x1, y1
        start = y
        end = yend
         
    for i in range(start,end*grosor):
        blank[int(x-grosor/2) : int(x+grosor/2), int(y-grosor/2):int(y+grosor/2)] = (51, 222, 255)
        if dx > dy:
            x = x+grosor if x < x1 else x-grosor
        else:
            y = y+grosor if y < y1 else y-grosor
        if p < 0:
            p += incE
        else:
            if dx > dy:
                y = y+grosor if y < y1 else y-grosor
            else:
                x = x+grosor if x < x1 else x-grosor
            p += incNE
    
    cv2.imshow("Yellow",blank)
    t2 = time.time()
    print("El tiempo de ejecucion es: ", t2-t1)
    cv2.waitKey(0)

def main():
    bresenham(200,20,300,800,3)
    
if __name__ == '__main__':
    main()
 