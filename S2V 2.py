import pyttsx3

engine = pyttsx3.init()

rate =engine.getProperty("rate")
engine.setProperty("rate", 100)

volume =engine.getProperty("volume")
engine.setProperty("volume", 2)



a=input("Enter anything:  ")

engine.say(a)

engine.runAndWait()
