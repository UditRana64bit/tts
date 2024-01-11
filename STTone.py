import speech_recognition as sr



def command():
 
  # Initialize speech recognizer
  r = sr.Recognizer()

  # Try to listen for a command
  try:
    with sr.Microphone() as source:
      r.adjust_for_ambient_noise(source)
      print('...')
      audio = r.listen(source,0,8)

      # Recognize the speech
      command = r.recognize_google(audio)
      print(f'User said: {command}')
      return command

  # If no command is recognized, ask the user for text input
  except sr.UnknownValueError:
    print("Sorry, I could not understand your command.")
    print("Please enter your command as text: ")
    command = input()
    print(f'User: {command}')
    return command