import tkinter
import cv2
import PIL.Image , PIL.ImageTk
import imutils 
from functools import partial   #we cant directly pass functions and its arguements in command, partial helps us to do so
import threading

SET_WIDTH = 650
SET_HEIGHT = 368


def play(speed):
    print(speed)

def out():
    print("OUT!")
    thread = threading.Thread(target=pending,args=('out',))
    thread.daemon = 1
    thread.start()

def not_out():
    print("NOT OUT")
    thread = threading.Thread(target=pending,args=('not out',))
    thread.daemon = 1
    thread.start()


def pending(d):
    # display decision pending and wait

    frame = cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB) # ---> converts image to RGB   (image to be inserted.... delete the paranthesis wen done @ KARAN)
    frame = imutils.resize(frame,width = SET_WIDTH, height = SET_HEIGHT) # incase the image is not resized
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))  # to make it tkinter usable
    canvas.image = frame
    canvas.create_image(0,0,image = 'frame', anchor = tkinter.NW)
    time.sleep(1)

    # display sponsors and wait
    
    frame = cv2.cvtColor(cv2.imread("sponsor.png"),cv2.COLOR_BGR2RGB) # ---> converts image to RGB   (image to be inserted.... delete the paranthesis wen done @ KARAN)
    frame = imutils.resize(frame,width = SET_WIDTH, height = SET_HEIGHT) # incase the image is not resized
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))  # to make it tkinter usable
    canvas.image = frame
    canvas.create_image(0,0,image = 'frame', anchor = tkinter.NW)
    time.sleep(1.5)

    # display the decision  

    if d == 'out':
        decisionIMG = "out.png"                 #(image to be inserted.... delete the paranthesis wen done @ KARAN)     
    else:
        decisionIMG = 'not_out.png'             #(image to be inserted.... delete the paranthesis wen done @ KARAN)
        
    frame = cv2.cvtColor(cv2.imread(decisionIMG),cv2.COLOR_BGR2RGB) # ---> converts image to RGB   (image to be inserted.... delete the paranthesis wen done @ KARAN)
    frame = imutils.resize(frame,width = SET_WIDTH, height = SET_HEIGHT) # incase the image is not resized
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))  # to make it tkinter usable
    canvas.image = frame
    canvas.create_image(0,0,image = 'frame', anchor = tkinter.NW)


window = tkinter.Tk()
window.title("Decision Review System")
cv_img = cv2.cvtColor(cv2.imread("welcome.png") , cv2.COLOR_BGR2RGB )
canvas = tkinter.Canvas(window, width = SET_WIDTH, height = SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0 ,0 , ancho=tkinter.NW, image=photo )
canvas.pack()


#Buttons
btn = tkinter.Button(window, text = "<< PREVIOUS(FAST)", width =50, command = partial(play,-25) )
btn.pack() 

btn = tkinter.Button(window, text = "<< PREVIOUS(SLOW)", width =50, command = partial(play,-2) )
btn.pack() 

btn = tkinter.Button(window, text = ">> NEXT(FAST)", width =50, command = partial(play,25) )
btn.pack() 

btn = tkinter.Button(window, text = ">> NEXT(SLOW)", width =50, command = partial(play,2) )
btn.pack() 

btn = tkinter.Button(window, text = "OUT", width =50, command  =  out )
btn.pack()

btn = tkinter.Button(window, text = "NOT OUT", width =50, command  =  not_out )
btn.pack()


window.mainloop()