import keyboard
##Media keys are used to hopefully cover both windows and linux (even macos?)
def media_control(media_key: str, steps: int = 1):
    """
    Create media control functions at runtime,
    Params:
    a media key to be played could be any of these:
        'play/pause media',
        'next track', 
        'previous track
        'volume up',
        'volume down',
        'volume mute'
        And must be a string (str)
    steps optional param for how many volume up's or down's to execute default is 1 (int)
    returns nothing
    """
    print(steps//2)
    match media_key:
        case 'volume up' | 'volume down':
            for i in range((steps//2) - 1):
                print(i)
                keyboard.send(media_key)
        case 'unmute volume' | 'volume unmute':
            keyboard.send('volume mute')
        case _:
            keyboard.send(media_key)


