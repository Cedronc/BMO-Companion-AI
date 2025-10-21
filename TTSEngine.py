import pyttsx3

class BMO_TTSEngine:
  def __init__(self):
    self.engine = pyttsx3.init()

  def speak(self, text):
    self.engine.say(text)

if __name__ == "__main__":
    print("This is the BMOtts.py file. Don't run this.")
