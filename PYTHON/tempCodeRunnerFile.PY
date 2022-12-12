 Ask.question()
      query = Ask.takeCommand().lower()
      # execution
      if 'wikipedia' in query:
         Voice.speak("searching in wikipedia...")
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         Voice.speak("According to wikipedia")
         print(results)
         Voice.speak(results)


      elif 'open google' in query:
         webbrowser.open("google.com")
    
      elif 'the time' in query:
         strTime = datetime.now().strftime("%H:%M:%S")
         Voice.speak(f"Sir, The time is {strTime}")

