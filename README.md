# Intelligent-Assistant

Simple speech recognition assistant which can perform some task to make your work easier and simple. Its a project of Operating System.
The main module covered in this assistant is **Multi-threading** and **Inter-Process Communication**.

## Features:
#### Module Handle by Speech Recogniton
* Search your query on __Google__.
* Search your query on __Youtude__.
* Create your file.
* Delete your file.

#### System Module Handle by Assistant to cover Inter-Process Communication
* Open Camera
* Open Internet Explorar
* Camera
* Notepad

**ChatBot to cover Multi-Threading**  
Chat can be also support by speech recognizer.

## Library:
#### Speech Recognition
import speech_recognition as sr  
import webbrowser as wb  
import os  

#### Inter-Process Communication
from subprocess import call  
import subprocess, time, os

#### ChatBot
from chatterbot import ChatBot  
from chatterbot.trainers import ListTrainer  

#### python text-to-speech
import pyttsx3 as pp version **2.7**.

---
**Created By S.M Burair Abbas**
