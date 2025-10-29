import speech_recognition as sr
recogniser=sr.Recognizer()
with sr.Microphone() as source:
    audio=recogniser.listen(source)
try:
    text=recogniser.recognize_google(audio)
    print("you said:",text)
except sr.UnknownValueError:
    print("Could not understand audio")