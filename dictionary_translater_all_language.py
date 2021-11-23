import googletrans
from pprint import pprint


# Initial
translator = googletrans.Translator()


# Basic Translate

def odia_to_en_trans(myword):
                    t=translator.translate(myword,src='en',dest='or').text
                    ts=list(t)
                    s=[]
                    dict={"ଅ":"A","ଆ ":"AAA","ା":"AA","ଇ ":"II","ଈ":"IIII","ଉ ":"UUU","ଊ  ":"RUU","ୠ  ":"RUU","ଊ  ":"RUU","ଊ  ":"RUU","ଏ" : "E","ଏ" : "E","ତ" : "TA","ତୁ" : "TU","ମ" : "MA","ମେ" : "ME","ନା" : "NA","ନ":"NA"}
                    for i in range (len(ts)):
                           if ts[i] in dict:
                             s.append(dict[ts[i]])
                    print(s)
                    a=''.join(s)
                    return a         
