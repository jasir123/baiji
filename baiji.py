# -*- coding: utf-8 -*-
for x in range(1,20):
    for y in range(1,32):
        for z in range(1,93):
            if x+y+z==100:
                if 5*x+ 3*y +z/3==100:
                    print(x,y,z)
                
