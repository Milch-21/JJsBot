from pynput.keyboard import Controller
from pynput import keyboard
from num2words import num2words
import time

list = {}

for i in range(1, 501):
    list[i] = num2words(i).upper()

max = input("How many JJs would you like to do? ")
max = int(max)

n = 1
keyboard_controller = Controller()

def Check():
    global n

    while n <= max:
        if n in list:
            time.sleep(0.25)

            keyboard_controller.press("/")
            time.sleep(0.5)

            for letter in list[n]:
                keyboard_controller.press(letter)
                time.sleep(0.1)

            time.sleep(0.1)
            keyboard_controller.press(keyboard.Key.enter)
            time.sleep(0.25)
            keyboard_controller.press(keyboard.Key.space)
            time.sleep(.1)
            keyboard_controller.release(keyboard.Key.space)

            n = n + 1
        else:
            print("no")
            break

    print("done")

time.sleep(1.5)

Check()