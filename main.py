import tkinter
import cv2
import PIL.Image , PIL.ImageTk
from functools import partial   #we cant directly pass functions and its arguements in command, partial helps us to do so
import threading
import imutils
import time


SET_WIDTH = 650
SET_HEIGHT = 368


def play(speed):
     print(f"Speed is {speed}")

def pending(decision):
     #pending
     frame = cv2.cvtColor(cv2.imread("pending.png") , cv2.COLOR_BGR2RGB ) # ---> converts image to RGB  
     frame = imutils.resize(frame,width = SET_WIDTH, height = SET_HEIGHT) # incase the image is not resized
     frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))  # to make it tkinter usable
     canvas.image = frame
     canvas.create_image(0 ,0, image= frame , anchor= tkinter.NW)

     time.sleep(2)

     #decision
     if decision == 'out':
         decisionImg = "out.png"
     else :
         decisionImg ="not_out.png"

     frame = cv2.cvtColor(cv2.imread(decisionImg) , cv2.COLOR_BGR2RGB )# ---> converts image to RGB   
     frame = imutils.resize(frame,width = SET_WIDTH, height = SET_HEIGHT) # incase the image is not resized
     frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))  # to make it tkinter usable
     canvas.image = frame
     canvas.create_image(0 ,0, image= frame , anchor= tkinter.NW)

def out():
     thread = threading.Thread(target= pending , args=("out",))
     thread.daemon = 1
     thread.start()

def notOut():
     thread = threading.Thread(target= pending , args=("Not out",))
     thread.daemon = 1
     thread.start()


window = tkinter.Tk()
window.title("Decision Review System")
cv_img = cv2.cvtColor(cv2.imread("welcome.png") , cv2.COLOR_BGR2RGB )
canvas = tkinter.Canvas(window, width = SET_WIDTH, height = SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0 ,0 , anchor=tkinter.NW, image=photo )
canvas.pack()

 #Buttons
btn = tkinter.Button(window, text = "PREVIOUS(FAST)", width =50 , command = partial(play, -25))
btn.pack() 

btn = tkinter.Button(window, text = "PREVIOUS(SLOW)", width =50 , command = partial(play, -5))
btn.pack() 

btn = tkinter.Button(window, text = "NEXT(FAST)", width =50 , command = partial(play, 25))
btn.pack() 

btn = tkinter.Button(window, text = "NEXT(SLOW)", width =50 , command = partial(play, 5))
btn.pack() 

btn = tkinter.Button(window, text = "GIVE OUT", width =50, command = out )
btn.pack()

btn = tkinter.Button(window, text = "GIVE NOT-OUT", width =50 , command = notOut)
btn.pack()


window.mainloop()
