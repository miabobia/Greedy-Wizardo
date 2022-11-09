from math import sqrt

def mouse_hit(x, y, w, h, mx, my):
    #returns if mouse(mx,my) is inside rect(x,y,w,h)
    if mx >= x and mx <= x + w:
        if my >= y and my <= y + h:
            return True
    return False

def rect_collide(x1, y1, w1, h1, x2, y2, w2, h2):
    #returns rectangle collision between two rects
    return \
    x1 + w1 >= x2 and \
    x1 <= x2 + w2 and \
    y1 + h1 >= y2 and \
    y1 <= y2 + h2

def dist(x1, y1, x2=0, y2=0):
    #gets distance between (x1,y1) -> (x2,y2)
    x = (x2 - x1)**2
    y = (y2 - y1)**2
    return sqrt(x+y)

def get_vector(x1, y1, x2, y2):
    #gets a vector from (x1,y1) -> (x2,y2)
    return (x2-x1,y2-y1)

def get_normal_vector(v):
    #takes in vector v and normalizes it and returns it
    d = dist(v[0], v[1])
    return (v[0]/d, v[1]/d)

def get_center_rect(x,y,w,h,f):
    #f is factor you want rectangle div by
    cx,cy = x+w/2,y+h/2

    new_w,new_h = w*f, h*f

    new_x, new_y = cx - new_w/2, cy - new_h/2

    return [new_x,new_y, new_w, new_h]
