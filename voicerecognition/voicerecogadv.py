'''
Created on Mar 16, 2015

Simple Voice recognition application
which listens to user command and opens the desired url in the web-browser

@author: Nitin
'''
import webbrowser
import time
import speech_recognition as sr

def main():
    url=''
    list={"google":"www.google.com","facebook":"www.facebook.com", "youtube" :"www.youtube.com","twitter":"www.twitter.com"
          ,"linkedin":"www.linkedin.com","c-dac":"www.cdac.in"}
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
            if word in list.keys(): 
                print "found ",word # navigating in the list of urls 
                url=list.get(word)
                print "opening  ",url
            
            else:
                print"not found ",word # coming out of the loop if the url is not found
                break 
                    
        except LookupError,err:
            print"not able to listen properly",err # Handling the exception if not able to listen audio
            break
        
        webbrowser.open(url) # Opening the URL in systems default browser
        choice = raw_input("Do you want to continue??Y/N :: ") # continuing the application unless the user type n/N
        if choice.lower()=="n":
            print"Thanks for using my Application..."
            print ""
            print "**********************************************"
            print "Ended Speech Recognizer App..................."
            print "**********************************************"
            break
        else:
            continue
    

if __name__=="__main__":
    print "***********************************"
    print "Welcome to my Speech Recognizer App"
    print "***********************************"
    main()
