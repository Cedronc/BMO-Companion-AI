import keyboard
import time

##Media keys are used to hopefully cover both windows and linux (even macos?)

def media_keys() -> tuple:
    return {
        'play_pause': 'play/pause media',
        'next_track': 'next track', 
        'prev_track': 'previous track',
        'volume_up': 'volume up',
        'volume_down': 'volume down',
        'volume_mute': 'volume mute'
    }

def skip_song():
    """Skip to next track using media keys"""
    try:
        keyboard.send('next track')
        print("Skipped to next track")
    except Exception as e:
        print(f"Error: {e}")

def play_pause():
    """Play/pause media"""
    keyboard.send('play/pause media')
