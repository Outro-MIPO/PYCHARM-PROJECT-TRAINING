import pyttsx3
f = open("readd.txt", "r")
a=f.read()
speaker = pyttsx3.init()
#speaker.say('je suis grand')
speaker.say(a)
speaker.runAndWait()
