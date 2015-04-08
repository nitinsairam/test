'''
Created on Mar 16, 2015

Simple Voice recognition application
which listens to user command and opens the desired folder in the local system
Currently it will work for windows only

@author: Nitin
'''
import webbrowser as wb
import time
import speech_recognition as sr

r=sr.Recognizer() # Recognizer class object is instantiated

print "Tell me ...."
time.sleep(1)

with sr.Microphone() as source: 
    audio=r.listen(source)  # Microphone class object is instantiated to come into listen mode
while True:
    try:       
        word = r.recognize(audio) # Recognizing the user command
        print"Folder required.... ",word # Printing on console the said input
        folder=''
        time.sleep(1)
        if word=="my folder":
            folder="D:\jarvis" 
            print"Opening ::",folder      
            wb.open(folder) # Opening the folder but this will work on windows only
        print"Thanks for using my Application..."
        break
    except LookupError,err:
        print"Could not understand audio",err # Handling the exception if not able to listen audio
        break
    

