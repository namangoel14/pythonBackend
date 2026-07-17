import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer =  sr.Recognizer()

newsapi = ""
# Initialize the pyttsx3 with .init()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"{newsapi}")
        if r.status_code == 200:
            data = r.json()

            articles = data.get("articles", [])

            for article in articles:
                speak(article["title"])
if __name__ == "__main__":
    speak("Initializing Jarvis....")

    # List for the wake word "Jarvis"
    while True:
    # obtain audio from the microphone
        r = sr.Recognizer()
        print("recognising..")
        try:
            with sr.Microphone() as source:
                print("Listing..")
                word = r.listen(source, timeout=2, phrase_time_limit=1)
            command = r.recognize_google(word)
            if (command.lower() == "jarvis"):
                speak("Yes sir")
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    process_command(command)
                    if (command.lower() == "shutdown"):
                        speak("Ok sir")
                        break
        except Exception as e:
           print("error; {0}".format(e))

