
##
import keyboard
import pandas
import tkinter
import time
from tkinter import *
import os,sys
import Notifier


def comments():
        
        #To collect data and create a dictionary
        w= pandas.read_csv("ES_codes.csv",encoding = "ISO-8859-1") 
        Code={}
        s=0
        for i in w.Codes[:]:
            Code.update({i:[]})
            if str(w.com1[s])!='nan':
                Code[i].append(w.com1[s])
            if str(w.com2[s])!='nan':
                Code[i].append(w.com2[s])
            if str(w.com3[s])!='nan':
                Code[i].append(w.com3[s])
            if str(w.com4[s])!='nan':
                Code[i].append(w.com4[s])
            if str(w.com5[s])!='nan':
                Code[i].append(w.com5[s])
            s=s+1
        ###################################################################################################################


        ###############Recording and saving in object################
        import keyboard

        def generate_events():
            while True:
                yield keyboard.read_event()
                #print(keyboard.read_event())

        strings = keyboard.get_typed_strings(generate_events())
        
        #def excution():
        while True:
            global Line
            
            if keyboard.read_key(suppress=False)=='f11':
                                              Notifier.notify("Deactivated")
                                              break

            Line=(next(strings)).strip()

        ##############################################################
            DataSet=Line.split(';')           ###Input stings conevrsion to List
            
            if len(DataSet[0])!=0:    
                        LenD= len(DataSet)            ###Dataset List Length
                        Key=DataSet[0]                ###item number of List
                        print('key:',Key)
                        if Key in Code:
                            LenC=len(Code[Key])           ###Abbrivation List len 
                            k=LenC-LenD
                            CharTyped=""
                            for i in DataSet: CharTyped= CharTyped+str(i)##Length of Char typed by user
                            print('LEN OF TYPE',len(CharTyped)+len(DataSet))
                            for i in range(len(CharTyped)+len(DataSet)):
                                    keyboard.press('backspace')
                                    time.sleep(0.05)
                            print(k)
                            print(len(Code[Key]))
                            for i in range(k+1):DataSet.append('##')
                            Input= 1
                            
                            for i in Code[Key]:
                                if len(Code[Key])==1 and k>-1:
                                        keyboard.write(str(i))
                                else:
                                        keyboard.write(str(i)+" #"+str(DataSet[Input])+" ")
                                        Input=Input+1

        print("Exit Loop")

