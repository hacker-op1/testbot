from time import sleep
import speech_recognition as sr
r = sr.Recognizer()
l =[]


def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')


def start():
    i =0
    while i ==0:
        print("I am listening...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio1 = r.listen(source)
                text1 = r.recognize_google(audio1, language='en')
                print(text1)
                l.append(text1)
                sleep(2)
                screen_clear()
            i = 1
        except:
            print('Sorry, I could not understand what you said.')



def edit(n):
    i = 0
    while i == 0:
        print('Which line do you want to edit?(number)')
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio1 = r.listen(source)
                text1 = r.recognize_google(audio1, language='en')
                print(text1)
                l[n - 1] = text1
                sleep(2)
                screen_clear()
                i=1
        except:
            print('Sorry, I could not understand what you said.')



def delete(n):
    i = 0
    while i ==0:
        print('Which line do you want to delete?(number)')
        sleep(3)
        screen_clear()
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio1 = r.listen(source)
                text1 = r.recognize_google(audio1, language='en')
                print(text1)
                l.pop(n - 1)
                sleep(2)
                screen_clear()
                i = 1
        except:
            print('Sorry, I could not understand what you said.')


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    while True:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio, language='en')
            if "start" in text.lower():
                start()
            elif "edit" in text.lower():
                audio2 = r.listen(source)
                text2 = r.recognize_google(audio2, language='en')
                if text2.lower() == 'to' or text2.lower() == 'too' or text2.lower() == 'tu':
                    text2 = 'two'
                from word2number import w2n
                edit(w2n.word_to_num(text2))
            elif 'delete' in text.lower():
                audio2 = r.listen(source)
                text2 = r.recognize_google(audio2, language='en')
                delete(w2n.word_to_num(text2))
            elif 'final stop' in text.lower():
                s = ""
                with open('file.txt', 'w+') as f:
                    for items in l:
                        s += items + ". "
                        f.write('%s\n' % items)
                f.close()
                from gtts import gTTS
                t = gTTS(text=s, lang='en')
                t.save("summary.mp3")
                print('Summary saved')
                import time

                timeout = 20
                time_start = time.time()
                while time.time() <= timeout + time_start:
                    r.adjust_for_ambient_noise(source)
                    audio3 = r.listen(source)
                    text3 = r.recognize_google(audio3, language='en')
                    if 'play summary' in text3.lower():
                        print('Playing summary...')
                        import os
                        os.system('summary.mp3')
                        break
                break
        except:
            pass












