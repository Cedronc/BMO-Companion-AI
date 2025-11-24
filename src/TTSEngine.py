import pyttsx3
#import piper
#from piper import PiperVoice
# TODO: port to piper-tts
 
def makeEngine():
    engine = pyttsx3.init()

    # Configure for more BMO-like qualities
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 180)  # Faster speed = more energetic
    engine.setProperty('volume', 0.8) 
    engine.setProperty('pitch', 110)  # Higher pitch = more childlike

def speak(engine, text: str) -> None:
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    print("This is the BMOtts.py file. Don't run this.")
