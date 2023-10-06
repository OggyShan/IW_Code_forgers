import speech_recognition as sr
import screen_brightness_control as sbc
import re
import pywhatkit
import ctypes
import time
import keyboard
import os
import win32api
import pyautogui
import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def play_song(command):
    song = command.replace('play','')
    speak("Playing"+song)
    pywhatkit.playonyt(song)

def sleep_mode(command):
    speak("Putting the computer to sleep in 10 seconds. Press 'Esc' to cancel.")
    print("Press 'Esc' key to cancel the sleep operation")

    start_time = time.time()
    while time.time() - start_time < 10:  # Keep checking for 10 seconds
        if keyboard.is_pressed('Esc'):  # If 'Esc' key is pressed
            speak("Operation cancelled")
            print("Operation cancelled")
            return  # Exit the function and cancel the sleep
        time.sleep(0.1)  # Wait for a short duration (0.1 seconds) before checking again

    print("Putting the computer to sleep")
    speak("Putting the computer to sleep")
    ctypes.windll.PowrProf.SetSuspendState(0, 1, 1)
    """
    first equals power saving mode
    second is necessary
    3rd referes to that if computer will exit the sleep mode of not if tracks and hardwar changes
    """
def shutdown_mode(command):
    speak("Shutting down the computer in 10 seconds. Press 'Esc' to cancel.")
    print("Press 'Esc' key to cancel the operation")
    
    start_time = time.time() #time when operation started
    while time.time() - start_time < 10:
        if keyboard.is_pressed('Esc'):
            speak("Operation cancelled")
            print("Operation cancelled")
            return
        time.sleep(0.1)  # sleep for a short duration to avoid high CPU usage
    
    print("Shutting down")
    os.system("shutdown /s /t 1")

def restart_mode(command):
    speak("Restarting the computer in 10 seconds")
    print("Restarting the computer in 10 seconds")
    start_time = time.time()
    while time.time()-start_time<10:
        if keyboard.is_pressed('Esc'):
            speak("Operation cancelled")
            print("Operation cancelled")
            return
        time.sleep(0.1)
    print("Restarting the machine")
    os.system("shutdown/r/t 1")


def control_brightness(command):
    if re.search(r"\b(increase|increasing|raise|full|max|maximum)\b",command):
        if re.search(r"\b(increase|increasing|raise)\b", command):
            curr_brightness = sbc.get_brightness()
            # print(curr_brightness) 
            latest_brightness = curr_brightness[0]+25
            speak(" increasing brightness")
            sbc.set_brightness(latest_brightness)
        elif re.search(r"\b(full|maximum|max)\b.*\b.(brightness)\b",command):
            sbc.set_brightness(100)
            speak("Maximum brightness reached")
        else:
            speak("Could not undertand")
    elif re.search(r"\b(decrease|decreasing||lower|minimum|least)\b",command):
        if re.search(r"\b(decrease|decreasilesserng|lesser|lower)\b", command):
            curr_brightness = sbc.get_brightness()
                    # print(curr_brightness) 
            latest_brightness = curr_brightness[0]-25
            speak("decreasing brightness")
            sbc.set_brightness(latest_brightness)
        elif re.search(r"\b(minimum|least)\b",command):
            sbc.set_brightness(0)
            speak("Minimum brightness reached")
        else:
            speak("Could not understand")
def handle_media_command(command):
    if re.search(r'\b(play|start)\b', command):
        win32api.keybd_event(0xB3, 0)  # VK_MEDIA_PLAY_PAUSE
        speak("Playing media")
        print("Playing media")
    elif re.search(r'\b(pause|stop)\b', command):
        win32api.keybd_event(0xB3, 0)  # VK_MEDIA_PLAY_PAUSE
        speak("Pausing media")
        print("Pausing media")
    else:
        speak("Command not recognized")
        print("Command not recognized")
    
command_list = {
     r"\b(play)\b.*\b(song|songs)\b":play_song,
     r"\b(brightness)\b" : control_brightness,
     r"\b(shutdown|turn off)\b.*\b(computer)\b":shutdown_mode,
     r"\b(restart)\b.*\b(computer)\b":restart_mode,
     r"\b(activate|turn on)\b.*\b(sleep mode)\b":sleep_mode,
     r"\b(play|start|pause|stop)\b": handle_media_command
    #  r"\b(shutdown|turn off)\b" : shutdown
}
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for commands...")
        audio = recognizer.listen(source,timeout=6)
    try:
        # Recognize speech using Google Web Speech API
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print("You said: " + command)
        # if 'oasis' in command:
        # command = command.replace('oasis','')
            
        return command
        # Perform actions based on the recognized command
        # (Add your logic here)
    except sr.WaitTimeoutError:
        print("Listening timed out. No audio detected.")
        
    except sr.UnknownValueError:
        print("Could not understand the audio")
        speak("Could not understand the audio Please speak again")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        speak("Could not request results; {0}".format(e))

def execute_command(recognized_command):
    for key_phrase,function in command_list.items():
        if re.search(key_phrase,recognized_command):
            function(recognized_command)
            return True
    print("Command not recognized")
    return False
# songs
# play puse increase decrese 

while True:
    recognized_command = recognize_speech()
    if recognized_command:
        if recognized_command=="exit":
            speak("Bye")
            break
        else:
            execute_command(recognized_command)

        

# recognize_speech()