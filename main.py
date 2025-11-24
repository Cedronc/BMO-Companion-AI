import os
import random
# Text to Speech
from src.TTSEngine import makeEngine, speak
# Generating tokens
from src.AIEngine import talk
# listening for audio
from src.GoogleVoiceProcessing import listen_until_speech
# playing audio files
from just_playback import Playback
import threading

def playAudio(filename): 
    playback = Playback()
    playback.load_file(filename)
    playback.set_volume(1)
    playback.loop_at_end(False)
    playback.play()
    print(playback.volume())

# def playAudio(filename):
#     """Play audio in a separate thread"""
#     def _play():
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         wave_obj.play()
    
#     # TODO: look at the api for this cuz i got no clue if the thread is reused or not.
#     thread = threading.Thread(target=_play)
#     thread.daemon = True  # Thread will close when main program closes
#     thread.start()
#     return thread

class BMOAssistant:
    def __init__(self):
        # BMO personality traits
        self.responses = {
            'greetings': {
                "bmo_chop": "./voices/bmo-chop.wav",
                "i_am_bmo": "./voices/i-am-bmo.wav",
                "mhm": "./voices/mmm-hmm.wav",
                "yay_bmo": "./voices/yaay-bmo.wav",
            },
            'farewells': {
                "battery_low_shut_down",  "./voices/battery-low-shut-down.wav"
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

    playAudio(bmo.responses['greetings']['bmo_chop'])

    # For text-based testing (comment out for voice-only)
    while True:
        listen_until_speech()
        talk(input("\nPrompt:\n"))

