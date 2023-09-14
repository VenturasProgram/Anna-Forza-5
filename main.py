import speech_recognition as sr
import pyttsx3
import pocketsphinx as ps
import pyaudio
import random
import pyautogui
import json


engine = pyttsx3.init()
r = sr.Recognizer()
user = "Ventura"

with sr.Microphone() as source:
    while True:
        try:
            audio = r.listen(source, timeout=2)
            fala = r.recognize_amazon(audio, language='pt-br')
            voices = engine.getProperty('voices')
            print(fala)
        except sr.exceptions.UnknownValueError:
            nao_te_ouvi_list = ("Por favor, repita", "não consegui te entender")
            nao_te_ouvi = random.choice(nao_te_ouvi_list)
            engine.say(nao_te_ouvi)
            print(nao_te_ouvi)
            engine.runAndWait()
        except sr.exceptions.WaitTimeoutError:
            pass

            
        if fala == 'Ei Ana':
            Hey_list = ("Olá No Que Posso Te Ajudar?", "Oi No Que Posso Te Ajudar Hoje {}?".format(user))
            Hey = random.choice(Hey_list)
            pyautogui.press(2)
            print (Hey)
            engine.say(Hey)
            engine.runAndWait()

        