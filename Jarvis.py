from time import sleep # Inbuilt
from playsound import playsound
import multiprocessing
print ("Wait")
def pl():
    playsound ("C://Users//soni//Desktop//Jarvis//pl.mp3")

sleep(2)

from bardapi import BardCookies # pip install bardapi
import datetime # pip install datetime
import speech_recognition as sr
from win10toast import ToastNotifier
import time
from cookie import save_cookies
import warnings
from elevenlabs import set_api_key
from elevenlabs import generate, play

set_api_key('0aa68134bd60c5b48690b07536907e6f')

def speak(text):
    text=str(text)
    audio=generate(
        text=text,
        voice="Daniel",
        model="eleven_multilingual_v2"
        )
    play(audio)





warnings.simplefilter('ignore')


from datetime import datetime
def greeting():
    # Get the current hour
    current_hour = datetime.now().hour

    # Define greeting messages for different time ranges
    greetings = {
        0: "Good Morning Sir!",
        12: "Good Afternoon Sir!",
        18: "Good Evening Sir!",
        24: "Good Evening Sir!",
    }

    # Choose the greeting based on the hour
    for threshold, greeting in greetings.items():
        if current_hour < threshold:
            print(greeting)
            return greeting

    # Handle edge cases for 24-hour format
    if current_hour == 24:
        return greetings[0]

    # If no greeting matches, return a default
    return "Hello Sir!"


def times():
    # Get the current time as a tuple of seconds since midnight
    current_time = time.time()

    # Convert seconds to hours, minutes, and seconds
    hours, minutes, seconds = time.gmtime(current_time).tm_hour, time.gmtime(current_time).tm_min, time.gmtime(current_time).tm_sec

    # Determine AM or PM
    am_pm = "AM" if hours < 12 else "PM"

    # Adjust hour for 12-hour format
    if hours > 12:
        hours -= 12

    # Format the time string
    time_string = f"{hours}:{minutes:02}:{seconds:02} {am_pm}"

    # Print the time
    return time_string

message = f"It`s currently {times()} at your current location. Tell me how I can be of your service sir."


def noti():
    # Create a notifier object
    toast = ToastNotifier()

    # Get and ensure valid greeting
    title = greeting()
    if title is None:
        title = "Good Day Sir!"

    # Define the notification content
    message1 = f"I am Jarvis, it is currently {times()} at your current location. Tell me how I can be of your service sir."

    # Customize the notification (optional)
    duration = 10  # Display for 10 seconds
    threaded = True  # Run in a separate thread

    # Show the toast notification
    toast.show_toast(title, message1, duration=duration, threaded=threaded)

    # Run your program logic here...


def command():
    try:
        r=sr.Recognizer()
        print("Listening for command...")
        with sr.Microphone() as source:
            audio = r.listen(source,0,8)  # Listen for 5 seconds
        command = r.recognize_google(audio)
        return (command)
        # Process the command here
    except sr.UnknownValueError:
        print("Sorry, I could not understand your command.")
        print("Please enter your command as text: ")
        command = input()
        print(f'User: {command}')
        return command
    except sr.RequestError as e:
        print("Could not request results from speech recognition service; {0}".format(e))



cookie_dict=save_cookies()
   

pl()
noti()
speak(message)



bard=BardCookies(cookie_dict=cookie_dict)

jarvis= "talk me like jarvis and always say i am jarvis whenever i ask about your identity"

reh=bard.get_answer(jarvis)['content']

while True:
    while True:
        try:
            Question = command()
            results = bard.get_answer(Question)['content']
            speak(results)
            print(results)
           
        except Exception as e:
            print(e)
