import speech_recognition as sr

#initialize the recognizer
r = sr.Recognizer()

def record_text():
    #loop in case of errors
    while True:
        try:
            #use mic as source of input
            with sr.Microphone() as source2:
                #prepare recognizer to receive ip
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's ip
                audio2 = r.listen(source2)
                
                #using google to recognize audio
                MyText = r.recognize_google(audio2)
                
                return MyText
            
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        
        except sr.UnknownValueError:
            print("unknown error occurred")
        
        except Exception as e:
             print("An unexpected error occurred: {0}".format(e))
               
    return

def output_text(text):
    f = open("output.txt","a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while True:
    text =  record_text()
    output_text(text)
    
    print("Wrote text")