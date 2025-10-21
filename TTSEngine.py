import pyttsx3
 
class BMO_TTSEngine:
    def __init__(self, engine = None):
        if engine == None:
            self.engine = pyttsx3.init()
        else:
            self.engine = engine

    def speak(self, text: str) -> None:
        self.engine.say(text)


def defaultBMOEngine() -> BMO_TTSEngine:
    return BMO_TTSEngine()


if __name__ == "__main__":
    print("This is the BMOtts.py file. Don't run this.")
