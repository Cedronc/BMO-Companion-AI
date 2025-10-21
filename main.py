import speech_recognition as sr
import datetime
import json
import os
import random
import TTSEngine

class BMOAssistant:
    def __init__(self):
        # Create Diary
        create_bmo_diary()
        # BMO personality traits
        self.ttsEngine = TTSEngine.defaultBMOEngine()
        self.responses = {
            'greetings': [
                "Hello! I'm BMO! Are we going to play a game?",
                "Hi, friend! What shall we do today?",
                "BMO is here! Ready to help!",
                "Oh! Hello! I was just practicing my dance moves!"
            ],
            'farewells': [
                "Goodbye!",
                "Bye bye! I'll practice my football!",
                "See you later! I'm going to watch my stories!",
                "Okay! Remember, BMO loves you!"
            ],
            'confused': [
                "Hmm, I don't understand that.",
                "That's a strange rule. Can you explain it again?",
                "My circuits are tingling in a confused way!",
                "I think I need to update my playbook for that one."
            ]
        }
        print("BMO is starting up... Beep boop!")

    def greeting(self):
        tmp = random.choice(self.responses['greetings'])
        return tmp

    def run(self):
        """Main loop for BMO"""
        self.greeting()


# Additional utility functions
def create_bmo_diary():
    """Create a simple diary file for BMO to remember things"""
if not os.path.exists("bmo_diary.txt"):
    with open("bmo_diary.txt", "w") as f:
        f.write("BMO's Diary\n")
    f.write("===========\n")
    print("BMO diary created!")



if __name__ == "__main__":
    print("Initializing BMO...")
    create_bmo_diary()

    bmo = BMOAssistant()
    bmo.greeting()
    bmo.ttsEngine.speak(bmo.greeting())

    # For text-based testing (comment out for voice-only)
    print("\nTest commands: time, joke, game, weather, sleep")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'q':
            break
        if user_input:
            print('not implemented')

