import os
import time
import base64
import platform

def clear():
    so = platform.system()
    if so == "Windows":
        os.system("cls")
    elif so == "Linux":
        os.system("clear")

def encode(text, times):
    encoded_text = text
    for _ in range(times):
        encoded_text = base64.b64encode(encoded_text.encode('utf-8')).decode('utf-8')
    return print(encoded_text)

def decode(hash, limit):
    decoded_text = hash
    try:
        while True:
            decoded_text = base64.b64decode(decoded_text).decode('utf-8')
            if len(decoded_text) > limit:
                break
        return print(decoded_text)
    except base64.binascii.Error:
        return print(decoded_text)

while True:
    clear()
    try:
        print("\n[1] - Encode")
        print("[2] - Decode")
        print("[3] - Exit\n\n")

        mode = int(input("Enter the mode: "))

        if mode == 1:
            print("\nEnter the text for ultra Encode: ")
            text = input("$ ")
            
            print("\nEnter the number of times: ")
            times = int(input("$ "))

            print()
            encode(text, times)
            
            print("\nTry again?\n")
            print("[1] - Yes")
            print("[2] - No")

            ta = int(input("$ "))
            if ta == 1:
                pass
            elif ta == 2:
                print("\nExiting...")
                time.sleep(0.5)
                break

        elif mode == 2:
            print("\nEnter the hash for ultra Decode: ")
            hash = input("$ ")

            print()
            decode(text, 9999999)

            print("\nTry again?")
            print("[1] - Yes")
            print("[2] - No")

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
