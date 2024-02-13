import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

exit_flag = False  # Flag to indicate whether to exit the program

def cmd():
    global exit_flag  # Use the global flag

    with sr.Microphone() as source:
        print("Clearing background noises...please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything..')
        recorded_audio = recognizer.listen(source)

    while True:  # Infinite loop for continuous listening
        try:
            text = recognizer.recognize_google(recorded_audio, language='en_US')
            text = text.lower()
            print('Your message:', format(text))

            if 'chrome' in text:
                a = 'Opening chrome..'
                engine.say(a)
                engine.runAndWait()
                programName = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                subprocess.Popen([programName])
                break
            if 'time' in text:
                current_time = datetime.datetime.now().strftime('%I:%M %p')
                print(current_time)
                engine.say(current_time)
                engine.runAndWait()
                break
            if 'play' in text:
                a = 'opening youtube..'
                engine.say(a)
                engine.runAndWait()
                pywhatkit.playonyt(text)
                break
            if 'youtube' in text:
                b = 'opening youtube'
                engine.say(b)
                engine.runAndWait()
                webbrowser.open('www.youtube.com')
                break
            if 'goodbye' in text:
                c = 'goodbye'
                engine.say(c)
                exit_flag = True  # Set the exit flag to True
                break  # Exit the loop

        except Exception as ex:
            print(ex)

# Main loop for continuous execution
# Check the exit flag
while not exit_flag:  
    cmd()

# Cleanup after exiting the loop
# Stop the engine
engine.stop()  
