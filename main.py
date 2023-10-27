import speech_recognition as sr
import pyttsx3
import wikipedia
import pyaudio

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
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print(f"Error connecting to Google Speech Recognition service: {e}")
        return ""

def assistant():
    speak("Hello! How can I assist you today?")

    while True:
        query = listen()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=20)
            speak("According to Wikipedia, " + result)

        elif "exit" in query or "bye" in query:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("I'm sorry, I don't understand that command. Can you please repeat or ask something else?")

if __name__ == "__main__":
    assistant()
