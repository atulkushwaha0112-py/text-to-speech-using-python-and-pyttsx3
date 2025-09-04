import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female

engine.setProperty('rate', 140)
engine.setProperty('volume', 1.0)

text = "Hello! This is a text-to-speech demo using pyttsx3 on Windows."
engine.say(text)
engine.runAndWait()
