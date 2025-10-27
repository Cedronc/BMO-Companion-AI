import keyboard
##Media keys are used to hopefully cover both windows and linux (even macos?)

def media_control(media_key: str):
    """
    Create media control functions at runtime,
    Params: a media key to be played could be any of these:
        'play/pause media',
        'next track', 
        'previous track
        'volume up',
        'volume down',
        'volume mute'
        And must be a string (str)
    returns nothing
    """
    print(type(media_key))
    keyboard.send(media_key)