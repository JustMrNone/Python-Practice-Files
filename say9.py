import pyttsx3 

engine = pyttsx3.init()

sentence = input("this: ")

engine.say(sentence)

engine.runAndWait()