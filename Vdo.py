import cv2
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame
from PIL import Image
from PIL import ImageTk
import time
from ctypes import windll

GWL_EXSTYLE=-20
WS_EX_APPWINDOW=0x00040000
WS_EX_TOOLWINDOW=0x00000080


def set_appwindow(root):
    hwnd = windll.user32.GetParent(root.winfo_id())
    style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    style = style & ~WS_EX_TOOLWINDOW
    style = style | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
    # re-assert the new window style
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: root.wm_deiconify())


def Play():
        white 		= "#ffffff"
        lightBlue2 	= "#adc5ed"
        font 		= "Constantia"
        fontButtons = (font, 12)
        maxWidth  	= 750
        maxHeight 	= 400

        #Graphics window
        mainWindow = tk.Tk()
        mainWindow.after(14000, lambda: mainWindow.destroy())
        #mainWindow.after(10, lambda: set_appwindow(mainWindow))
        mainWindow.wm_title("Little Finger")
        
        mainWindow.wm_attributes("-topmost", 1)
        mainWindow.overrideredirect(True)
        #mainWindow.configure(bg=lightBlue2)
        mainWindow.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,0,0))
        mainWindow.resizable(0,0)
        # mainWindow.overrideredirect(1)
        mainWindow.geometry("+300+200")

        mainFrame = Frame(mainWindow)
        mainFrame.place(x=0, y=0)                

        #Capture video frames
        lmain = tk.Label(mainFrame)
        lmain.grid(row=0, column=0)

        cap = cv2.VideoCapture('NCR Entrance Effect.mp4')

        def show_frame():
                ret, frame = cap.read()

                cv2image   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            

                img   = Image.fromarray(cv2image).resize((760, 450))
                imgtk = ImageTk.PhotoImage(image = img)
                lmain.imgtk = imgtk
                lmain.configure(image=imgtk)
                lmain.after(10, show_frame)
        def destroy():
                mainWindow.destroy()


                
##        closeButton = Button(mainWindow, text = "CLOSE", font = fontButtons, bg = white, width = 20, height= 1)
##        closeButton.configure(command= lambda: mainWindow.destroy())              
##        closeButton.place(x=270,y=430)
        show_frame()  #Display

        mainWindow.mainloop()  #Starts GUI


#Play()

