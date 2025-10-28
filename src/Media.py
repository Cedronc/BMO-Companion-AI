import keyboard
##Media keys are used to hopefully cover both windows and linux (even macos?)
def media_control(media_key: str, steps: int = 2):
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
    steps optional param for how many volume up's or down's to execute the lowest value is 2(int)
    returns nothing
    """
    steps = steps if steps > 1 else 2
    print(steps)
    match media_key:
        case 'volume up' | 'volume down':
            for i in range(steps // 2):
                try:
                    keyboard.send(media_key)
                except Exception as e:
                    print(f"Error: {e}")
        case 'unmute volume' | 'volume unmute':
            keyboard.send('volume mute')
        case _:
            keyboard.send(media_key)


