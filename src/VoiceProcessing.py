import speech_recognition as sr
import whisper

# this shit is borked
model = whisper.load_model("medium")
def listen_until_speech():
    r = sr.Recognizer()
    
    while True:
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=100, phrase_time_limit=8)
                print(audio)

        except sr.WaitTimeoutError:
            print("⏰ No speech detected. Still listening...")
            continue
        except sr.UnknownValueError:
            print("🔁 Could not understand audio. Try speaking again...")
            continue
        except sr.RequestError as e:
            print(f"❌ API error: {e}")
            continue
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            continue

listen_until_speech()
