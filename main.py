import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit

def transform():
    # r is a recognizer which recognize our voice
    r = sr.Recognizer()
    # When we collected our speaking words by Microphone, then turn them into a source
    with sr.Microphone() as source:
        #Wait time to listen= 0.8(s)
        r.pause_threshold = 0.8
        #store our words into a variable "said"
        said = r.listen(source)
        #Prevent the recognizer don't work :>
        try:
            print('I am listening...')
            # Using Google to recognize language
            catch_audio = r.recognize_google(said, language="en")
            #print(f'You said: {catch_audio}')
            return catch_audio
        except sr.UnknownValueError:
            print("Sorry, I did not understand...")
            return "I am waiting..."
        except sr.RequestError:
            print("Sorry the service is down")
            return "I am waiting..."
        except:
            return "I am waiting..."

        
#Assissant is speaking to us!!
def speaking(message):
    engine = pyttsx3.init()
    print(message)
    engine.say(message)
    engine.runAndWait()

speaking( 'hello' )


engine = pyttsx3.init()
for voice in engine.getProperty('voices'):
    print(voice)
    
#change assisstant's voice
id= 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', id )
engine.say('Hello World')
engine.runAndWait()


#return the weekday name

def query_day():
    day = datetime.date.today()
    weekday = day.weekday()
    mapping = {
        0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'
    }
    try:
        speaking(f'Today is {mapping[weekday]}')
    except:
        pass
    
    
#returns the time
def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speaking(f" { time[1] } o'clock and { time[3:5] }  minutes ")
    
    
#Intro greeting at startup
def whatsup():
    speaking('''
    Hi, I am ZIRA. I am your personal assistant.
    How can i help you?
    ''')
    
#the heart of our assistant. Takes queries and return answer
def querying():
    whatsup()
    start = True
    while(start):
        catch_audio = transform().lower()
        
        if 'open youtube' in catch_audio:
            speaking('opening youtube for you. Just a second. Lazy head!')
            webbrowser.open('https://www.youtube.com')
            continue
            
        elif 'open google' in catch_audio:
            speaking('opening google for you. Just a second. O M G Jesus!')
            webbrowser.open('https://www.google.com')
            continue
        
        elif 'what day is it' in catch_audio:
            query_day()
            continue
            
        elif 'what time is it' in catch_audio:
            query_time()
            continue
        
        elif 'shut down' in catch_audio:
            speaking('OK Goodbye')
            break
            
        elif 'your name' in catch_audio:
            speaking('I am Zira. Your Super Cute Voice Assistant.')
            continue
        
        elif 'search web' in catch_audio:
            pywhatkit.search(catch_audio)
            speaking("That is what i found")
            continue
        
        elif 'play' in catch_audio:
            speaking(f'playing {catch_audio}')
            pywhatkit.playonyt(catch_audio)
            continue
            
            
#Test it
querying()




