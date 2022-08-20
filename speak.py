# simple text to speech in python
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, you're welcome. I am a robot. I am here to help you.")
engine.runAndWait()
engine.stop()
