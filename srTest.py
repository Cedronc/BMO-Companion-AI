import pyaudio
import json
from vosk import Model, KaldiRecognizer

def continuous_vosk_recognition():
    model = Model("/Users/cedric/Documents/git/BMO-Companion-AI/models/vosk-model-en-us-0.22-lgraph")  # Replace with your model path
    recognizer = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=8192)

    print("Continuous recognition started. Press Ctrl+C to stop.")
    
    try:
        while True:
            data = stream.read(4096, exception_on_overflow=False)
            
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get('text', '')
                if text:
                    print(f"\nFinal: {text}")
            else:
                partial = json.loads(recognizer.PartialResult())
                partial_text = partial.get('partial', '')
                if partial_text:
                    print(f"Listening: {partial_text}", end='\r', flush=True)
                    
    except KeyboardInterrupt:
        print("\nStopping recognition...")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

# Usage
continuous_vosk_recognition()
