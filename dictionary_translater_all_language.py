import googletrans
from pprint import pprint
import json
import pyttsx3
import time

# Initial
translator = googletrans.Translator()
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[2].id)
engine. setProperty("rate", 100)
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Opening JSON file
f = open('odia.json',encoding="utf-8")

# returns JSON object as`
# a dictionary
data = json.load(f)
r=data['language']
o=r['odia']
# Basic Translate

def odia_to_en_trans(myword):
                    t=translator.translate(myword,src='en',dest='or').text
                    ts=list(t)
                    s=[]
                    f=[]
                    for i in range (len(ts)):
                           if ts[i] in o:
                             s.append(o[ts[i]])
                           else:
                            s.append(' ')
                    print(s)
                    a=''.join(s)
                    speak(a)
odia_to_en_trans("I love u because you love me soo much")