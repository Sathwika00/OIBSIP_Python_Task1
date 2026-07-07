import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except:
        speak("Sorry, I didn't understand.")
        return ""

# Greeting
speak("Hello! I am your voice assistant.")

while True:
    command = listen()

    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "google" in command:
        speak("What should I search?")
        search = listen()
        webbrowser.open(f"https://www.google.com/search?q={search}")

    elif "hello" in command:
        speak("Hello! How can I help you?")

    elif "bye" in command:
        speak("Goodbye!")
        break
    