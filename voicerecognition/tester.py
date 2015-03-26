'''
Created on Mar 16, 2015

Simple Voice recognition application
which listens to user command and opens the desired url in the web-browser

@author: Nitin
'''
import webbrowser
import time


def main():
    url=''
    list={"google":"www.google.com","facebook":"www.facebook.com", "youtube" :"www.youtube.com","twitter":"www.twitter.com"
          ,"linkedin":"www.linkedin.com","c-dac":"www.cdac.in","flipkart": "www.flipkart.com","coursera": "www.coursera.com",
          "snapdeal": "www.snapdeal.com","wikipedia": "www.wikipedia.org","gmail": "www.gmail.com"}
    while True:
        try:       
            word=raw_input("Enter the word:: ")
            print"you typed ",word # Printing on console the said input
            time.sleep(1)
            if word in list.keys():
                print "found ",word
                url=list.get(word)
                print url
            
            else:
                print"not found ",word
                print "project folder is opened"
                 
            print "out of try"
            
        except LookupError,err:
            print"not able to find the word",err # Handling the exception if not able to get the word
            break
        print "out of the loop"
        webbrowser.open(url) # Opening the URL in systems default browser
        choice = raw_input("Do you want to continue??Y/N :: ")
        if choice.lower()=="n":
            print"Thanks for using my Application..."
            print ""
            print "**********************************************"
            print "Ended tester to my Speech Recognizer App......"
            print "**********************************************"
            break
        else:
            continue
        
        
    

if __name__=="__main__":
    print "**********************************************"
    print "Welcome to tester to my Speech Recognizer App"
    print "**********************************************"
    main()
