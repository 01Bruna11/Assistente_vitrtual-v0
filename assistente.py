#assistente virtual em pythno
import speech_recognition as sr
import playsound 
from gtts import gTTS, tts
import random
import webbrowser
import pyttsx3
import os
import pyautogui
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# root = tk.Tk()
# root.title('Bora?')
# root.geometry('608x600')
# root.configure(background='#ffc8dd')

class Virtual_assit():
    def __init__(self, assist_name, person):
        self.person = person
        self.assit_name = assist_name

        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        
        self.voice_data = ''

    def engine_speak(self, text):
        """
        fala da assitente virtual
        """
        text = str(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def record_audio(self, ask=""):


        with sr.Microphone() as source:
            if ask:
                print('recording...')
                self.engine_speak(ask)

            audio = self.r.listen(source,5 , 5)# pega dados de auido
            print('looking at the data base')
            try:
                self.voice_data = self.r.recognize_google(audio) #converte audio para texto

            except sr.UnknownValueError:
                self.engine_speak('Sorry Boss, I did not get what you said. Can you please repeat?')

            except sr.RequestError:
                self.engine_speak('Sorry Boss, my server is down') # recognizer is not connected

            print(">>",self.voice_data.lower()) #imprime o que vc disse
            self.voice_data = self.voice_data.lower()

            return self.voice_data.lower()

    def engine_speak(self, audio_strig):
        audio_strig = str(audio_strig)
        tts = gTTS(text=audio_strig, lang='en')
        r = random.randint(1,20000)
        audio_file = 'audio' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(self.assit_name + ':', audio_strig)
        os.remove(audio_file)


    def there_exist(self, terms):
        for term in terms:
            if term in self.voice_data:
                return True


    def respond(self, voice_data):
        if self.there_exist(['hey', 'hi', 'hello', 'oi', 'holla']):
            greetigns = [f'Hi {self.person}, what are we doing today?',
                        'Hi Boss, how can I help you?',
                        'Hi Boss, what do you need?']

            greet = greetigns[random.randint(0,len(greetigns)-1)]
            self.engine_speak(greet)

        #google
        if self.there_exist(['looking for']) and 'youtube' not in voice_data:
            search_term = voice_data.split("for")[-1]
            url =  "http://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("here is what I found for " + search_term + 'on google')

        #google 
        if self.there_exist(['looking youtube for']):
            search_term  = voice_data.split("for")[-1]
            url = "http://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("Here is what i found for" + search_term + 'on youtube')

        #whatsapp
        if self.there_exist(['Open whatsapp', 'whatsapp']):
            #self.engine_speak("Opening Whatsapp")
            url = "https://web.whatsapp.com/"
            webbrowser.get().open(url)
            self.engine_speak("Whatsapp is open")
            
        #abrir aréa de trabalho 
        if self.there_exist(['please open the work', 'workspace']):
            self.engine_speak("Opening work")
            url = "https://www.google.com/"
            webbrowser.get().open(url)
            self.engine_speak("Work is open")
            time.sleep(0.5)
            pyautogui.moveTo(381, 57)
            pyautogui.click(381, 57)
            time.sleep(2)
            pyautogui.moveTo(901, 805)   #gather
            pyautogui.click(901, 805)    #gather
            time.sleep(3)                #gather
            pyautogui.moveTo(1187, 639)  #não funciona aqui
            pyautogui.click(1187, 639)
            time.sleep(2)
            
        if self.there_exist(['gather', 'open gather', 'open cat']):
            self.engine_speak("Opening gather")
            url = "https://app.gather.town/app/FmUVFRbs3wnvJrx0/Pedagogico%20Time"
            webbrowser.get().open(url)
            self.engine_speak("Gather is open")
            #pyautogui.moveTo(381, 57)
            #pyautogui.click(381, 57)
            #time.sleep(2)
            time.sleep(8)                #gather
            pyautogui.moveTo(1187, 639)  #não funciona aqui
            pyautogui.click(1187, 639)
            #time.sleep(2)
            
        #nova funçao - desligar pc 
        if self.there_exist(['power off', 'desligar', 'off', 'turn off']):
            self.engine_speak("Turning off", "delsigando")
            time.sleep(1)
            os.system("shutdown /s /t 1")

        #nova funçao - open blender
        if self.there_exist(['open blender', 'blender', 'open editor blender']):
            self.engine_speak("Opening Blender")
            time.sleep(1)
            os.system("C:/Program Files/Blender Foundation/Blender 2.93/blender.exe")

        #abrir projeto super.blender no blender
        if self.there_exist(['open project super']):
            self.engine_speak("Opening project in Blender")
            time.sleep(1)
            os.system("C:/Program Files/Blender Foundation/Blender 2.93/blender.exe")
            time.sleep(1)
            pyautogui.moveTo(x=1062, y=716)
            time.sleep(1)
            self.engine_speak("Project is open")

        #arir pasta de projetos 
        if self.there_exist(['Open projects', 'show me the projects in past', 'open the project', 'open project']): 
            self.engine_speak("Opening projects")
            time.sleep(1)
            os.system("C:/Users/bru/Documents/Projects")
            self.engine_speak("Projects is open")

        #abrir bloco de notas e fazer anotaçoes
        if self.there_exist(['open notepad', 'notepad', 'open notes', 'notes']):
            self.engine_speak("Opening notepad")
            time.sleep(1)
            #abrir notepad
            # cmd = 'notepad'
            # os.system(cmd)
            pyautogui.press('winleft')
            time.sleep(1)
            pyautogui.write('bloco de notas')
            pyautogui.press('enter')
            time.sleep(1)
            self.engine_speak("What do you want writer?")
            time.sleep(1)
            #transcrever audio em escrita
            self.record_audio()
            pyautogui.write(self.record_audio())
            
            time.sleep(1)
            #perguntar se deve escrever algo mais caso a resposta seja nao, salvar bloco de notas e fecjar
            # self.engine_speak("Do you want to write something else?")
            # self.record_audio()
            # if self.there_exist(['yes', 'sim', 'yep', 'yap', 'yup', 'yeah']):
            #     self.engine_speak("What do you want writer?")
            #     self.record_audio()
            #     pyautogui.write(self.voice_data)
            #     time.sleep(1)
            self.engine_speak("Writed")
            time.sleep(1)
            #salvar com hora e data
            self.engine_speak("Saving")
            time.sleep(1)
            #fechar bloco de notas
            self.engine_speak("Closing notepad")
            time.sleep(1)
            os.system("taskkill /im notepad.exe /f")
            self.engine_speak("Notepad is closed")


#arir teclado para digitar palavras 
        if self.there_exist(['open keyboard', 'keyboard', 'open the keyboard', 'open the keyboard']):
            self.engine_speak("Opening keyboard")
            time.sleep(1)
            #abrir teclado
            cmd = 'osk'
            os.system(cmd)
            self.engine_speak("Keyboard is open")
            time.sleep(1)
            self.engine_speak("What do you want writer?")
            time.sleep(1)
            #transcrever audio em escrita
            self.record_audio()
            pyautogui.write(self.record_audio())
            time.sleep(1)
            #perguntar se deve escrever algo mais caso a resposta seja nao, salvar bloco de notas e fecjar
            self.engine_speak("Do you want to write something else?")
            self.record_audio()
            if self.there_exist(['yes', 'sim', 'yep', 'yap', 'yup', 'yeah']):
                self.engine_speak("What do you want writer?")
                self.record_audio()
                pyautogui.write(self.voice_data)
                time.sleep(1)
            self.engine_speak("Writed")
            time.sleep(1)
            #salvar com hora e data
            self.engine_speak("Saving")
            time.sleep(1)
            #fechar bloco de notas
            self.engine_speak("Closing keyboard")
            time.sleep(1)
            os.system("taskkill /im osk.exe /f")
            self.engine_speak("Keyboard is closed")


assistent = Virtual_assit('Smoak', 'Bru')

while True:

    voice_data = assistent.record_audio('Hey, what do you need today?...')
    assistent.respond(voice_data)

    if assistent.there_exist(['bye', 'goodbye', 'seeyou', 'see you later', 'see you', 'Thanks, bye', 'thank you']):
        assistent.engine_speak("Have a nice day! Good bye!")
        break


