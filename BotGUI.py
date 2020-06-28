from tkinter import *
from tkinter import ttk
import nltk
from PIL import Image, ImageTk
import tkinter.font as font  # library to set the font size in btn text

# For prompt box
from tkinter.messagebox import *

# Multi-threading Library
from threading import *

# Speech Recognition Library
import speech_recognition as sr
import webbrowser as wb
import os

# Inter-Communication Library
from subprocess import call
import subprocess, time, os

# ChatBot Library
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# python text-to-speech
import pyttsx3 as pp

# Error solved by pip install pyttsx3==2.7
# File "C:\ProgramData\Anaconda3\lib\site-packages\comtypes_init.py", line 329, in setattr
# self.make_methods(value)
# File "C:\ProgramData\Anaconda3\lib\site-packages\comtypes_init.py", line 698, in make_methods
# prototype = WINFUNCTYPE(restype, *argtypes)
# File "C:\ProgramData\Anaconda3\lib\ctypes_init.py", line 123, in WINFUNCTYPE
# class WinFunctionType(_CFuncPtr):
# TypeError: item 2 in argtypes passes a union by value, which is unsupported.

engine = pp.init()
voices = engine.getProperty('voices')

# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

rate = engine.getProperty('rate')
engine.setProperty('rate', 175)
print(rate)


def Speak(line):
    engine.say(line)
    engine.runAndWait()


#############End##############

root = Tk()
root.minsize(350, 650)
root.title("2S.2 Bot Assitant")
root.iconbitmap(r'img/favicon2.ico')  # icon

# Content and Logo
# botImg = PhotoImage(file=r"img/IconContent.png")
## The (250, 250) is (height, width)
botImg = Image.open(r"img/iconContent.png")
botImg = ImageTk.PhotoImage(botImg.resize((350, 254), Image.ANTIALIAS))
botImgLbl = Label(root, image=botImg)
botImgLbl.pack(side='top', anchor="e")  # Top-Right

# Speech Recognition

mic1 = sr.Recognizer()
mic2 = sr.Recognizer()


##Voice Search

# UC - Use Case

def google_UC(cmd):
    if "Google" in cmd:
        mic2 = sr.Recognizer()
        url = 'https://www.google.com/search?q='
        # wb.get().open(url)
        with sr.Microphone() as source:
            # print('What you want to Search?')
            Speak("What you want to Search?")
            audio = mic2.listen(source)

            try:
                get = mic2.recognize_google(audio)
                # if user say 'search', remove it when search in google
                if "search" in get.lower():
                    get = get.lower().replace('search', '').strip()
                print(get)
                wb.get().open(url + get)
            except sr.UnknownValueError:
                error = "Sorry, i can't hear you. Please try again"
                # showinfo("Error", error) # prompt message
                Speak(error)
            except sr.RequestError as e:
                error = 'Failed'.format(e)
                showinfo("Error", error)


def open_google():
    voiceCmd.config(state=DISABLED)
    try:
        with sr.Microphone() as source:
            Speak("What is your query?")
            audio = mic1.listen(source)

        cmd = mic2.recognize_google(audio)  # convert audio into string
        print(mic2.recognize_google(audio))
        google_UC(cmd)
    except sr.UnknownValueError:
        # showinfo("Error", "Sorry, i can't hear you. Please try again")
        Speak("Sorry, i can't hear you. Please try again")
    voiceCmd.config(state=NORMAL)


def opengoogle_Thread():
    threading = Thread(target=open_google)
    threading.start()


VSImg = ImageTk.PhotoImage(Image.open(r"img/VSCircle.png").resize((335, 61), Image.ANTIALIAS))
voiceCmd = Button(root, relief='ridge', image=VSImg, command=opengoogle_Thread)
voiceCmd.place(x=5, y=288)


## Create File
'''for p in nltk.data.path:
    datas.append((p, "nltk_data"))'''

hiddenimports = ["nltk.chunk.named_entity"]

def create_UC(cmd):
    # if "create" in cmd.lower():  # when it detect create word it create file
    #     fileName = cmd.lower().replace('create', '').replace(" ", '') + ".txt" #replacing create word
    fileName = cmd.lower().replace(" ", '') + ".txt"
    print(fileName)
    if fileName != '' and not os.path.exists(fileName):
        f = open(fileName, 'a+')
        f.close()
        Speak("Successfully created '" + fileName + "'")
        showinfo("Message", "Successfully created '" + fileName + "'")
    else:
        Speak("Sorry, File Already Exist")
        showinfo("Error", "Sorry, File Already Exist!")


def createfile():
    cfCmd.config(state=DISABLED)
    try:
        with sr.Microphone() as source:
            Speak("What is your query?")
            audio = mic1.listen(source)

        cmd = mic2.recognize_google(audio)  # convert audio into string
        # print(mic2.recognize_google(audio))
        create_UC(cmd)
    except sr.UnknownValueError:
        # showinfo("Error", "Sorry can't hear you. Please try again!")
        Speak("Sorry can't hear you. Please try again!")
    cfCmd.config(state=NORMAL)


def createfile_Thread():
    thread = Thread(target=createfile)
    thread.start()


cfImg = ImageTk.PhotoImage(Image.open(r"img/cfCircle.png").resize((335, 60), Image.ANTIALIAS))
cfCmd = Button(root, relief='ridge', image=cfImg, command=createfile_Thread)
cfCmd.place(x=5, y=363)


## DeleteFile

def delete_UC(cmd):
    if "delete" in cmd.lower():
        fileName = cmd.lower().replace('delete', '').replace(" ", '')
        fileName = fileName + ".txt"
        if os.path.exists(fileName):
            os.remove(fileName)
            Speak("Successfully delete '" + fileName + "'")
            showinfo("Message", "Successfully delete '" + fileName + "'")
        else:
            Speak("Sorry, File doesn't exist")
            showinfo("Error", "Sorry, File doesn't exist")
    else:
        Speak("Please Speak again, with keyword 'Delete' ")


def deletefile():
    dltbtn.config(state=DISABLED)
    try:
        with sr.Microphone() as source:
            Speak("What is your query?")
            audio = mic1.listen(source)

        cmd = mic2.recognize_google(audio)  # convert audio into string
        print(mic2.recognize_google(audio))

        delete_UC(cmd)
    except sr.UnknownValueError:
        Speak("Sorry can't hear you. Please try again!")
        # showinfo("Error", "Sorry can't hear you. Please try again!")
    dltbtn.config(state=NORMAL)


def deletefile_Thread():
    thread = Thread(target=deletefile)
    thread.start()


dfImg = ImageTk.PhotoImage(Image.open(r"img/dfCircle.png").resize((335, 60), Image.ANTIALIAS))
dltbtn = Button(root, relief='ridge', image=dfImg, command=deletefile_Thread)
dltbtn.place(x=5, y=438)


# Inter-Communication

def open_Calc():
    call(["calc.exe"])


def open_IE():
    iexplore = os.path.join(os.environ.get("PROGRAMFILES", "C:\\Program Files"),
                            "Internet Explorer\\IEXPLORE.EXE")
    ie = wb.BackgroundBrowser(iexplore)
    ie.open("google.com")


def open_Camera():
    subprocess.run('start microsoft.windows.camera:', shell=True)
    time.sleep(10)
    subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)


def open_Notepad():
    call(["notepad.exe"])


def open_ITC():
    itcWindow = Tk()
    itcWindow.minsize(280, 220)
    itcWindow.title("2S.2 InterProcessCommunication")
    itcWindow.iconbitmap(r'img/favicon2.ico')  # icon

    MyFont = font.Font(size=6)  # set the size of the font in the btn text

    # calImage = ImageTk.PhotoImage(Image.open(r"img/calCircle.png").resize((240, 45), Image.ANTIALIAS))
    calbtn = Button(itcWindow, text="Calculator", font=MyFont, relief='ridge', bd=4,
                    fg="white", width=15, bg="gray", command=open_Calc)
    calbtn.place(x=45, y=10)

    # calderImage = ImageTk.PhotoImage(Image.open(r"img/calderCircle.png").resize((240, 45), Image.ANTIALIAS))
    calenderbtn = Button(itcWindow, text="Internet Explorar", font=MyFont, relief='ridge', bd=4,
                         fg="white", width=15, bg="gray", command=open_IE)
    calenderbtn.place(x=45, y=60)

    # cameraImage = ImageTk.PhotoImage(Image.open(r"img/cameraCircle.png").resize((240, 45), Image.ANTIALIAS))
    camerabtn = Button(itcWindow, text="Camera", font=MyFont, relief='ridge', bd=4,
                       fg="white", width=15, bg="gray", command=open_Camera)

    camerabtn.place(x=45, y=110)

    # ntpadImage = ImageTk.PhotoImage(Image.open(r"img/ntpadCircle.png").resize((), Image.ANTIALIAS))
    ntpadbtn = Button(itcWindow, text="NotePad", font=MyFont, relief='ridge', bd=4,
                      fg="white", width=15, bg="gray", command=open_Notepad)

    ntpadbtn.place(x=45, y=160)

    mainloop()


iTcImg = ImageTk.PhotoImage(Image.open(r"img/iTcCircle.png").resize((335, 59), Image.ANTIALIAS))

# width=15, height=2
iTcbtn = Button(root, relief='ridge', image=iTcImg, command=open_ITC)
iTcbtn.place(x=5, y=510)

##Inter-process Comunication End

## chatterBot

from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot("Bot")


# convo = [
#         "hello",
#         "hi there!",
#         "how are you doing?",
#         "what is your name?"
#         "my name is 2S.2",
#         "i am your Assitant"
#         "i am doing great.",
#         "that is good to hear",
#         "Thank you.",
#         "You're welcome."
#     ]
# trainer = ListTrainer(bot)


def trainer_Thread():
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train('chatterbot.corpus.english')


thread = Thread(target=trainer_Thread)
thread.start()


# without Threading
# trainer.train("chatterbot.corpus.english")


def talk_bot(usermsg, msgs):
    usrmsg = usermsg.get()
    bot_answer = bot.get_response(usrmsg)
    msgs.insert(END, "You: " + usrmsg)
    strbotAnswer = str(bot_answer)
    if (len(strbotAnswer) > 55):  # break the answer of bot so it remain of ListBox frame
        split_strings = []
        n = 55
        for index in range(0, len(strbotAnswer), n):
            split_strings.append(strbotAnswer[index: index + n])

        for index in range(0, len(split_strings)):
            if (index == 0):
                msgs.insert(END, "Bot: " + split_strings[index])
            else:
                msgs.insert(END, split_strings[index])
    else:
        msgs.insert(END, "Bot: " + strbotAnswer)

    Speak(bot_answer)
    usermsg.delete(0, END)  # Clear EntryTextBox
    msgs.yview(END)  # scrollBar set to the end


def talk_bot_Thread(usermsg, msgs):
    thread = Thread(target=talk_bot(usermsg, msgs))
    thread.start()


def get_voice_msg():
    try:
        with sr.Microphone() as source:
            audio = mic1.listen(source)

        text = mic2.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        Speak("Sorry, i can't hear you. Please try again")


def verbal_text(msgs):
    text = get_voice_msg()
    if  not (text == None):
        bot_answer = bot.get_response(text)
        msgs.insert(END, "You: " + text)
        strbotAnswer = str(bot_answer)
        if (len(strbotAnswer) > 55):  # break the answer of bot so it remain of ListBox frame
            split_strings = []
            n = 55
            for index in range(0, len(strbotAnswer), n):
                split_strings.append(strbotAnswer[index: index + n])

            for index in range(0, len(split_strings)):
                if (index == 0):
                    msgs.insert(END, "Bot: " + split_strings[index])
                else:
                    msgs.insert(END, split_strings[index])
        else:
            msgs.insert(END, "Bot: " + strbotAnswer)

        Speak(bot_answer)
        msgs.yview(END)  # scrollBar set to the end


def verbal_text_Thread(msgBox):
    threading = Thread(target=verbal_text(msgBox))
    threading.start()


def openChatBox():
    root2 = Tk()
    root2.minsize(350, 350)
    root2.iconbitmap(r'img/favicon2.ico')  # icon
    root2.title("2S.2 ChatBot")

    frame = Frame(root2, pady=5)
    sc = Scrollbar(frame)
    msgBox = Listbox(frame, width=50, height=10, yscrollcommand=sc.set)
    sc.pack(side=RIGHT, fill=Y)
    msgBox.pack(side=LEFT, pady=5)
    frame.place(x=5, y=10)
    usermsg = Entry(root2, font=("Verdena", 15), width=27)
    usermsg.place(x=5, y=200)

    MyFont = font.Font(size=6)  # set the size of the font in the btn text

    submitbtn = Button(root2, text="Speak", relief='ridge', bd=4,
                       fg="black", width=10, bg="gainsboro", font=MyFont,
                       command=lambda: verbal_text_Thread(msgBox))
    # command=lambda: talk_bot_Thread(usermsg, msgBox)
    submitbtn.place(x=5, y=250)

    def enter_function(event):
        # submitbtn.invoke()  # call the submit btn
        talk_bot_Thread(usermsg, msgBox)

    # when press enter it call the above func and it invoke the submit button
    root2.bind('<Return>', enter_function)  # '<Return>' used to call 'entry-key'

    mainloop()


cbImg = ImageTk.PhotoImage(Image.open(r"img/chatCircle.png").resize((335, 54), Image.ANTIALIAS))

chatbtn = Button(root, text="ChatBot", image=cbImg, relief='ridge', command=openChatBox)
chatbtn.place(x=5, y=583)

###############ChatterBot End##############


mainloop()

