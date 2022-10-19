import pyautogui
import math
import sched, time


s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    R = 200 #Radius 
    (x,y) = pyautogui.size() # measure screen size
    (X,Y) = pyautogui.position(x/2,y/2)#locate center of the screen 
    pyautogui.moveTo(X+R,Y)# offset by radius 

    for i in range(360):
        if i%6==0:
            pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))

    sc.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()