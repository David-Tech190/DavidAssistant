import pyttsx3
import speech_recognition as sr
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import random

# Initialize the speech engine
engine = pyttsx3.init()

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use male voice

# Initialize recognizer
recognizer = sr.Recognizer()

def speak(text):
    """Speak the given text using pyttsx3."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for a command using the microphone."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            speak("Could not request results.")
            return None

class AssistantApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("David Assistant")
        self.setGeometry(300, 300, 400, 200)

        # Create a timer for repeated tasks
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_for_commands)
        self.timer.start(5000)  # Check for commands every 5 seconds

    def check_for_commands(self):
        """Check if the assistant needs to respond to a command."""
        command = listen()
        if command:
            if "hello" in command.lower():
                speak("Hello, how can I help you today?")
            elif "play music" in command.lower():
                speak("Playing music.")
                # Code to play music (or use a music player API)
            elif "tell me a joke" in command.lower():
                joke = random.choice([
                    "Why don't skeletons fight each other? They don't have the guts.",
                    "I told my wife she was drawing her eyebrows too high. She looked surprised!"
                ])
                speak(joke)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    assistant = AssistantApp()
    assistant.show()
    sys.exit(app.exec_())
