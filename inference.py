from datetime import datetime
from logging import exception
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

class Voice:
   def speak(audio):
      engine.say(audio)
      engine.runAndWait()


   def wishMe():
      Voice.speak("What is your Name?")
      name = Ask.takeCommand();
      hour = int(datetime.now().hour)
      if hour >= 0 and hour < 12:
         Voice.speak(f"Good Morning {name}!")
      elif hour >=12  and hour <= 18:
         Voice.speak(f"Good Afternoon {name}!")
      else:
         Voice.speak(f"Good Evening {name}!")

      Voice.speak(f"I here to help you  {name} about Agriculture related doubt  . Please tell me how I can Help You ")
      print(f"I here to help you  {name} about Agriculture related doubt  . Please tell me how I can Help You ")

class Ask():
   def takeCommand():
      r = sr.Recognizer()
      with sr.Microphone() as source:
         print("Listening....")
         r.pause_threshold = 1
         audio = r.listen(source)

      try:
         print("Recognizing...")
         query = r.recognize_google(audio, language= 'en-in')
         print(f"User said: {query}\n")

      except Exception as E:
         # print(e)
         print("Say that again please...")
         Voice.speak("Say that again please...")
         return "None"
      return query

   def question():
      print("Before Moving Forward Here Are some series of questions to be answered\n")
      Voice.speak("Before Moving Forward Here Are some series of questions to be answered")
      print("About Which Scheme you want to Known  Enter the Scheme Number...\n")
      Voice.speak("Which Scheme you want to Known... Enter the Scheme Number")
      print("1 Pradhan Mantri Kisan Samman Nidhi ")
      print("2 Pradhan Mantri Fasal BimaYojana")
      print("3 Agriculture Infrastructure Fund")
      print("4 Pradhan Mantri Krishi Sinchai Yojana")
      Voice.speak("1 Pradhan Mantri Kisan Samman Nidhi ")
      Voice.speak("2 Pradhan Mantri Fasal BimaYojana")
      Voice.speak("3 Agriculture Infrastructure Fund")
      Voice.speak("4 Pradhan Mantri Krishi Sinchai Yojana")

   def process():
         while True:

   # if 1:

            query = int(input("Above following Schemes, What You Want to Know About Enter"))
            if 1 == query:
               with open("scheme1.txt",'r') as file:
                  data = file.read()
                  print(data)
                  Voice.speak(data)
            elif 2 == query:
               with open("scheme2.txt",'r') as file:
                  data = file.read()
                  print(data)
                  Voice.speak(data)
            elif 3 == query:
               with open("scheme3.txt",'r') as file:
                  data = file.read()
                  print(data)
                  Voice.speak(data)
            elif 4 == query:
               with open("scheme4.txt",'r') as file:
                  data = file.read()
                  print(data)
                  Voice.speak(data)
            


if __name__ == "__main__":
   Voice.wishMe()
   Ask.question()

   Ask.process()
  
      