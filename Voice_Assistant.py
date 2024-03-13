#Jaya Kushal
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

#for speech recognition
recognizer = sr.Recognizer()
#convert text to speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening..")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing..")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
    except Exception as e:
        print("Sorry,can you please repeat?")
        query = None
    return query

def assistant():
    speak("Hello, I'm Alex. How can I help you today?")
    while True:
        query = listen()
        if query:
            if "hello" in query:
                speak("Hi. How can I assist you?")
            elif "how are you" in query:
                speak("I'm good.Thank you for asking!")
            elif "time" in query:
                current_time = datetime.datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}")
            elif "date" in query:
                current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
                speak(f"The date is {current_date}")
            elif "search" in query:
                speak("What would you like me to search for?")
                search_query = listen()
                if search_query:
                    url = f"https://www.google.com/search?q={search_query}"
                    webbrowser.open(url)
                    speak(f"Here are the search results for {search_query}")
            elif "exit" in query:
                speak("Goodbye")
                break

assistant()
