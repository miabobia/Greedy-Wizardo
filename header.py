from enemy import Enemy

BUSH_IDLE   = (["bush.png","bounce2.png","bounce3.png"],[(30,0),(5,1),(10,2),(5,1)])
BUSH_OCCUPY = (["peek.png"],[(10,0)])

ENEMY_RUN = (["running1.png","running2.png","running3.png"],[(15,0),(3,1),(5,2),(3,1)])

BUSH_NUM = 6
B_SPACE  = 120
B_OFFSET = 40

# #seperated by levels
# bush_crds = [
# (82,B_SPACE-B_OFFSET), (442, B_SPACE-B_OFFSET),\ 
# (262, B_SPACE*2-B_OFFSET),\
# (82,B_SPACE*3-B_OFFSET), (442,B_SPACE*3-B_OFFSET),\
# (262,B_SPACE*4-B_OFFSET), \
# (82,B_SPACE*5-B_OFFSET),(442, B_SPACE*5-B_OFFSET)\
# ]

bush_crds = [(82,B_SPACE-B_OFFSET), (442, B_SPACE-B_OFFSET),(262, B_SPACE*2-B_OFFSET),(82,B_SPACE*3-B_OFFSET), (442,B_SPACE*3-B_OFFSET),(262,B_SPACE*4-B_OFFSET),(82,B_SPACE*5-B_OFFSET),(442, B_SPACE*5-B_OFFSET)]

BUSH_WIDTH  = 120
BUSH_HEIGHT = 80


E_INFO = [(3,Enemy)]

WIDTH = 720
HEIGHT = 960
