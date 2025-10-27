import os
import random
import TTSEngine
from AIEngine import talk
import simpleaudio as sa

def playAudio(filePath: str):
    wave_obj = sa.WaveObject.from_wave_file(filePath)
    play_obj = wave_obj.play()
    # play_obj.wait_done()

class BMOAssistant:
    def __init__(self):
        # BMO personality traits
        self.ttsEngine = TTSEngine.defaultBMOEngine()
        self.responses = {
            'greetings': {
                "BMO CHOP!": "./voices/bmo-chop.wav",
                "I am BMO.": "./voices/i-am-bmo.wav",
                "mmmmhhmmm.": "./voices/mmm-hmm.wav",
                "YAAAY BMO!": "./voices/yaay-bmo.wav",
            },
            'farewells': {
                "Battery low, shut down...",  "./voices/battery-low-shut-down.wav"
            },
        }
        print("BMO is starting up... Beep boop!")

    def greeting(self):
        tmp = random.choice(self.responses['greetings'])
        return tmp

    def run(self):
        """Main loop for BMO"""
        self.greeting()


# TODO add diary
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

    bmo = BMOAssistant()

    # playAudio(bmo.responses['greetings']['BMO CHOP!'])

    # For text-based testing (comment out for voice-only)
    while True:
        talk(input("\nPrompt:\n"))

