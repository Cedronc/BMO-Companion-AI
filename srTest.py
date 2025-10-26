import speech_recognition as sr


def listen_until_speech():
    r = sr.Recognizer()
    
    while True:
        try:
            with sr.Microphone() as source:
                print("🎤 Listening... Speak now!")
                # Adjust for ambient noise each time
                r.adjust_for_ambient_noise(source, duration=0.5)
                
                # Listen with longer timeout
                audio = r.listen(source, timeout=10, phrase_time_limit=8)
                
            print("🔄 Processing...")
            text = r.recognize_google(audio)
            
            if text.strip():  # If we got non-empty text
                print(f"✅ Recognized: {text}")
                return text
            else:
                print("🔁 Heard something but couldn't understand. Trying again...")
                
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

# Usage
result = listen_until_speech()
print(f"Final result: {result}")