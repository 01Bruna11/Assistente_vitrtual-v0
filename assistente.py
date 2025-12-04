# Assistente virtual em Python

import speech_recognition as sr
import playsound
from gtts import gTTS
import random
import webbrowser
import os
import pyautogui
import time

class Virtual_assit():
    def __init__(self, assist_name, person):
        self.person = person
        self.assit_name = assist_name

        self.r = sr.Recognizer()
        self.voice_data = ""

    def engine_speak(self, audio_string):
        audio_string = str(audio_string)
        tts = gTTS(text=audio_string, lang='en')
        r = random.randint(1,20000)
        audio_file = f"audio{r}.mp3"
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(self.assit_name + ":", audio_string)
        os.remove(audio_file)

    def record_audio(self, ask=""):
        with sr.Microphone() as source:
            if ask:
                self.engine_speak(ask)
            audio = self.r.listen(source, phrase_time_limit=5)
            try:
                self.voice_data = self.r.recognize_google(audio)
            except sr.UnknownValueError:
                self.engine_speak("Sorry, I did not understand.")
                return ""
            except sr.RequestError:
                self.engine_speak("Server error.")
                return ""

        print(">>", self.voice_data.lower())
        return self.voice_data.lower()

    def there_exist(self, terms):
        return any(term in self.voice_data for term in terms)

    def respond(self, voice_data):

        if self.there_exist(['hey', 'hi', 'hello', 'oi', 'hola']):
            greetings = [
                f'Hi {self.person}, what are we doing today?',
                'Hi Boss, how can I help you?',
                'Hi Boss, what do you need?'
            ]
            self.engine_speak(random.choice(greetings))

        # Google search
        if self.there_exist(['looking for']) and 'youtube' not in voice_data:
            search_term = voice_data.split("for")[-1]
            url = "https://google.com/search?q=" + search_term
            webbrowser.open(url)
            self.engine_speak("Here is what I found for " + search_term)

        # YouTube search
        if self.there_exist(['looking youtube for']):
            search_term = voice_data.split("for")[-1]
            url = "https://www.youtube.com/results?search_query=" + search_term
            webbrowser.open(url)
            self.engine_speak("Here is what I found for " + search_term)

        # WhatsApp
        if self.there_exist(['open whatsapp', 'whatsapp']):
            webbrowser.open("https://web.whatsapp.com/")
            self.engine_speak("Whatsapp is open")

        # Shutdown
        if self.there_exist(['power off', 'desligar', 'turn off']):
            self.engine_speak("Turning off")
            os.system("shutdown /s /t 1")

        # Notepad
        if self.there_exist(['open notepad', 'notepad', 'notes']):
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.write('bloco de notas')
            pyautogui.press('enter')
            time.sleep(1)

            self.engine_speak("What do you want to write?")
            text = self.record_audio()
            pyautogui.write(text)

            self.engine_speak("Saving and closing")
            os.system("taskkill /im notepad.exe /f")

assistent = Virtual_assit('Smoak', 'Bru')

while True:
    voice_data = assistent.record_audio("Hey, what do you need today?")
    assistent.respond(voice_data)

    if assistent.there_exist(['bye', 'goodbye', 'see you', 'thanks']):
        assistent.engine_speak("Have a nice day! Goodbye!")
        break
