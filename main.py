import os, threading, random
from playsound import playsound
from pynput import keyboard


def play_audio():
    random_index = random.randint(0, len(soundList) - 1)
    playsound("./assets/" + soundList[random_index])


def on_release(key):
    print('{0} released'.format(key))
    threading.Thread(target=play_audio).start()


if __name__ == '__main__':
    soundList = os.listdir("./assets/")
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()
