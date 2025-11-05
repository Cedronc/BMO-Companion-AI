import speech_recognition as sr
# TODO: Make return class with status and text

def listen_until_speech() -> str:
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Listening... Speak now!")
            # Adjust for ambient noise each time
            r.adjust_for_ambient_noise(source, duration=0.2)
            # Listen with no sentence limit
            audio = r.listen(source, timeout=200)
            
        print("[P]rocessing...")
        text = r.recognize_google(audio)
        
        if text.strip():  # If we got non-empty text
            print(f"User: {text}")
            return text
        else:
            print("Could not understand")
            return "Could not understand"
            
    except sr.UnknownValueError:
        print("🔁 Could not understand audio. Try speaking again...")
    except sr.RequestError as e:
        print(f"❌ API error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

listen_until_speech()