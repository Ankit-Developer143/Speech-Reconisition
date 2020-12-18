import speech_recognition as sr
from time import ctime
import webbrowser
import time
from gtts import gTTS
import playsound
import os
import random

r=sr.Recognizer()

                   #6th parameter 
def record_audio(ask = False):
     with sr.Microphone() as source:

         #6th ----
        if ask:
            alexis_speak(ask)

             #-----end
        r.adjust_for_ambient_noise(source,duration=1)
        audio= r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
           # print(voice_data)
        except sr.UnknownValueError:
            alexis_speak("sorry, could not recognise")
        except sr.RequestError:
            alexis_speak('Sorry, my Speech service is down')
        return voice_data

#text to speech
def alexis_speak(audio_string):
    tts = gTTS(text = audio_string,lang='en')
    r = random.randint(1,100000)
    audio_file = 'audio-'+str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

#Third steps
def respond(voice_data):
    #4th
    if 'what is your name' in voice_data:
        alexis_speak('my Name is Alexis')
        #5th
    if 'what time is it' in voice_data:
        alexis_speak(ctime())
     if 'Who is your Boss' in voice_data:
        alexis_speak("My boss Name is Ankit Singh")

        #6th
    if 'search' in voice_data:
        search = record_audio('What do you Want To Search For?')
        url = 'https://google.com/search?q=' +search
        webbrowser.get().open(url)
        alexis_speak('here what I found for' +search)

    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Here is the location of' + location)
    if 'exit' in voice_data:
        exit()

        
time.sleep(1)
 #Second steps  
alexis_speak('How can I help You')
while 1:
    voice_data = record_audio()
    respond(voice_data)

