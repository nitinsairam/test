'''
Created on Mar 16, 2015

Simple Voice recognition application
which listens to user command and opens the desired url in the web-browser

@author: Nitin
'''
import webbrowser
import time
import speech_recognition as sr

r=sr.Recognizer() # Recognizer class object is instantiated

print "Now speak..."
time.sleep(1)

with sr.Microphone() as source: 
    audio=r.listen(source)  # Microphone class object is instantiated to come into listen mode
while True:
    try:       
        word = r.recognize(audio) # Recognizing the user command
        print"you said ",word # Printing on console the said input
        time.sleep(1)
        if word=="google":
            url="www.google.com"
        elif word=="facebook":
            url="www.facebook.com"
        elif word=="youtube":
            url="www.youtube.com"
        
        print"Opened ::",url
        webbrowser.open(url) # Opening the URL in systems default browser
        print"Thanks for using my Application..."
        break
    except LookupError:
        print"Could not understand audio" # Handling the exception if not able to listen audio
        break
    

