import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error connecting to Google Speech Recognition service: {e}")
        return ""

def get_date():
    date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {date}")

def get_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")

def get_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"There are multiple results for {query}. Please be more specific.")
    except wikipedia.exceptions.PageError as e:
        speak(f"Sorry, I couldn't find any information about {query}.")

def main():
    speak("Hello! How can I assist you today?")

    while True:
        query = listen()

        if "hello" in query:
            speak("Hello! How can I help you?")
        elif "how are you" in query:
            speak("I'm doing well, thank you!")
        elif "date" in query:
            get_date()
        elif "time" in query:
            get_time()
        elif "search" in query:
            query = query.replace("search", "")
            get_wikipedia(query)
        elif "exit" in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
