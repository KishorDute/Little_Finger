import tkinter as tk
import keyboard
from tkinter import *
#Python 2.x program for Speech Recognition 

import speech_recognition as sr

def S2T():
        Name=sr.Microphone.list_microphone_names()
        #enter the name of usb microphone that you found 
        #using lsusb 
        #the following name is only used as an example 
        mic_name = Name[0]
        #Sample rate is how often values are recorded 
        sample_rate = 48000
        #Chunk is like a buffer. It stores 2048 samples (bytes of data) 
        #here. 
        #it is advisable to use powers of 2 such as 1024 or 2048 
        chunk_size = 2048
        #Initialize the recognizer 
        r = sr.Recognizer()
        m = sr.Microphone()

        #generate a list of all audio cards/microphones 
        mic_list = sr.Microphone.list_microphone_names() 

        #the following loop aims to set the device ID of the mic that 
        #we specifically want to use to avoid ambiguity. 
        for i, microphone_name in enumerate(mic_list): 
                if microphone_name == mic_name: 
                        device_id = i 

        #use the microphone as source for input. Here, we also specify 
        #which device ID to specifically look for incase the microphone 
        #is not working, an error will pop up saying "device_id undefined"
        def rec():
            global audio 
            with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
                                                            chunk_size = chunk_size) as source: 
                    #wait for a second to let the recognizer adjust the 
                    #energy threshold based on the surrounding noise level 
                    r.adjust_for_ambient_noise(source)
                    print("Say Something")
                    update("Say Something")
                    #listens for the user's input 
                    audio = r.listen(source,timeout=1,phrase_time_limit=10) 
                    print("Wait for a moment")
                    update("Converting")
        def stop():
        ##        stop_listening = r.listen_in_background(m, callback)
        ##        r.stop_listening(wait_for_stop=False)

                try:
                    text = r.recognize_google(audio,language="Eng-IN")
                    keyboard.write(text)
                    update("Try Again")
                #error occurs when google could not understand what was said
                except sr.UnknownValueError: update("Could not understand")
                except sr.RequestError as e:
                    update("Could not request results from Google Speech Recognition service; {0}".format(e))
                

        class MyBtn(tk.Button):
            # set function to call when pressed
            def set_down(self,fn):
                self.bind('<Button-1>',fn)
             
            # set function to be called when released
            def set_up(self,fn):
                self.bind('<ButtonRelease-1>',fn)

               
        class Mainframe(tk.Frame):
            def __init__(self,master,*args,**kwargs):
                tk.Frame.__init__(self,master,*args,**kwargs)
                
                # create the button and set callback functions
                btn = MyBtn(self,text = 'Press&Hold')
                btn.set_up(self.on_up)
                btn.set_down(self.on_down)
                btn.pack()
           
            # function called when pressed
            def on_down(self,x):
                print("Button down")
                rec()
                
            # function called when released
            def on_up(self,x):
                print("Button up")
                stop()
                        
        # create and run an App object
        if __name__ == '__main__':
                global variable 
                root = tk.Tk()
                text=StringVar()
                text.set("Welcome")
                def update(notification):
                        print('note',notification)
                        text.set(notification)
                        root.update()
                label = tk.Label(root, textvariable=text, font = ('Raleway',10),fg = 'blue')
                label.pack(side=TOP)
                root.title('Recording')
                root.geometry('150x50')                      
                Mainframe(root).pack()
                root.mainloop()

