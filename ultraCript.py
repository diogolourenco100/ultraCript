import os
import time
import base64
from pyfiglet import figlet_format
import platform
from modules.colora import cyan, green, red, yellow

def clear():
    so = platform.system()
    if so == "Windows":
        os.system("cls")
    elif so == "Linux":
        os.system("clear")

def banner():
    banner_text = figlet_format('Ultra Cripter', font='big')

    print(cyan('-'*59))
    print(green(banner_text))
    print(red('by Diogo S. Lourenco'))
    print(cyan('-'*59))

def encode(text, times):
    encoded_text = text
    for _ in range(times):
        encoded_text = base64.b64encode(encoded_text.encode('utf-8')).decode('utf-8')
    return print(green(encoded_text))

def decode(hash, limit):
    decoded_text = hash
    try:
        while True:
            decoded_text = base64.b64decode(decoded_text).decode('utf-8')
            if len(decoded_text) > limit:
                break
        return print(decoded_text)
    except base64.binascii.Error:
        return print(green(decoded_text))

while True:
    clear()
    try:
        banner()

        print(cyan('\n[1] - Encode\n[2] - Decode\n[3] - Exit\n\n'))

        mode = int(input(yellow("Enter the mode: ")))

        if mode == 1:
            print(yellow("\nEnter the text for ultra Encode: "))
            text = input("$ ")
            
            print(yellow("\nEnter the number of times: "))
            times = int(input("$ "))

            print()
            encode(text, times)
            
            print(cyan("\nTry again?\n"))
            print(cyan("[1] - Yes"))
            print(cyan("[2] - No"))

            ta = int(input("$ "))
            if ta == 1:
                pass
            elif ta == 2:
                print("\nExiting...")
                time.sleep(0.5)
                break

        elif mode == 2:
            print(yellow("\nEnter the hash for ultra Decode: "))
            hash = input("$ ")

            print()
            decode(text, 9999999)

            print(cyan("\nTry again?\n"))
            print(cyan("[1] - Yes"))
            print(cyan("[2] - No"))

            ta = int(input("$ "))
            if ta == 1:
                pass
            elif ta == 2:
                print("\nExiting...")
                time.sleep(0.5)
                break
        
        elif mode == 3:
            print("\nExiting...")
            time.sleep(0.5)
            break

        else:
            print("Enter a validi responde...")
            time.sleep(1.75)

    except Exception as ex:
        print("Invalid argument...")
        time.sleep(1.5)
        clear()
