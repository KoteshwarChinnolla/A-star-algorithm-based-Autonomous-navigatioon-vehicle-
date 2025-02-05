import matplotlib.pyplot as plt
import numpy as np
import heapq
import serial
import time
from PIL import Image

class send_arduino:
    def costamise(self,d):
        prev='down'
        curr=''
        cusarray=[]
        for i in range(1,len(d)):
            curr=d[i]
            if prev=='down':
                prev=curr
                if curr =='down':
                    cusarray.append('f')
                elif curr=='up':
                    cusarray.append('b')
                    cusarray.append('f')
                elif curr=='right':
                    cusarray.append('r')
                    cusarray.append('f')
                else:
                    cusarray.append('l')
                    cusarray.append('f')
            elif prev=='up':
                prev=curr
                if curr =='down':
                    cusarray.append('b')
                    cusarray.append('f')
                elif curr=='up':
                    cusarray.append('f')

                elif curr=='right':
                    cusarray.append('l')
                    cusarray.append('f')
                else:
                    cusarray.append('r')
                    cusarray.append('f')
            elif prev=='left':
                prev=curr
                if curr =='down':
                    cusarray.append('r')
                    cusarray.append('f')
                elif curr=='up':
                    cusarray.append('l')
                    cusarray.append('f')
                elif curr=='right':
                    cusarray.append('b')
                    cusarray.append('f')
                else:
                    cusarray.append('f')
            else:
                prev=curr
                if curr =='down':
                    cusarray.append('l')
                    cusarray.append('f')
                elif curr=='up':
                    cusarray.append('r')
                    cusarray.append('f')
                elif curr=='right':
                    cusarray.append('f')
                else:
                    cusarray.append('b')
                    cusarray.append('f')
        return cusarray

    def sendtoarduino(self,data):
        arduino.write((data + '\n').encode())
        if data=='f':
            time.sleep(0.07)
        else:
            time.sleep(0.07)