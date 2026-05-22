# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pyttsx3
engine = pyttsx3.init()
engine.say("Ma go est jolie , elle ressemble Dj congelateur , et moi je resemble a Conger flaiwoooo")
engine.runAndWait()





import pyttsx3
def onWord(name, location, length):
   print ('word', name, location, length)
   if location > 10:
      engine.stop()
engine = pyttsx3.init()
engine.connect('started-word', onWord)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()



engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()



engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+100)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()


engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.25)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

