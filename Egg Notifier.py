import time

import easyocr
import pyautogui
import numpy
import requests
import os
from requests.exceptions import MissingSchema

dcwebhook = "Empty"
tgbottoken = "Empty"
tgchatid = "Empty"
notiftype = "Empty"
eggtypes = "12"
delay = 5
countold = 0

try:
    with open("config.txt", "r") as x:
        lines = x.readlines()
        if "Telegram" in lines[0]:
            notiftype = "Telegram"
        elif "discord" in lines[0]:
            notiftype = "discord"
        tgbottoken = lines[1][20:-1]
        tgchatid = lines[2][18:-1]
        dcwebhook = lines[3][17:-1]
        eggtypes = lines[4][10:-1]
        delay = int(lines[5][7:-1])
        print("Program Succsessfuly Started!")
except (FileNotFoundError, IndexError):
    with open("config.txt", "w") as x:
        notifchoice = input("Choose Notification Method (just enter number)\n1:Telegram\n2:Discord\n> ")
        if notifchoice != "1" and notifchoice != "2" or notifchoice == "":
            print("Choice is wrong Please Restart The Program and Just type 1 or 2")
            if os.path.exists("config.txt"):
                x.close()
                os.remove("config.txt")
            input("Press Enter To Close The Program...")
            exit()
        if notifchoice == "1":
            notiftype = "Telegram"
            tgbottoken = input("Enter Telegram Bot Token: ")
            tgchatid = input("Enter Telegram Chat ID: ")

        elif notifchoice == "2":
            notiftype = "discord"
            dcwebhook = input("Enter Discord WebHook: ")

        eggtypes = input("Select Egg Types (with number only Example: 1 2 3 or 1 2 or 1)\n1: Divine Eggs\n2: Eternal Eggs\n3: Secret Eggs\n> ")
        if eggtypes == "":
            eggtypes = "12"
        if "1" not in eggtypes and "2" not in eggtypes and "3" not in eggtypes or eggtypes == "":
            print("Choice is wrong Please Restart The Program and Make it Correct i guess...")
            if os.path.exists("config.txt"):
                x.close()
                os.remove("config.txt")
            input("Press Enter To Close The Program...")
            exit()
        delay = input("Enter Delay Seconds Between Checks (default is 5 but if u want get notification quicker u can reduce it min 0 max 10): ")
        if delay == "":
            delay = 5
        try:
            delay = int(delay)
            if not (0 <= delay <= 10):
                raise ValueError
        except ValueError:
            print("Wrong Please Restart program and Enter just number")
            if os.path.exists("config.txt"):
                x.close()
                os.remove("config.txt")
            input("Press Enter To Close The Program...")
            exit()
        x.write(f"Notification Type: {notiftype}\nTelegram Bot Token: {tgbottoken}\nTelegram Chat ID: {tgchatid}\nDiscord WebHook: {dcwebhook}\nEggTypes: {eggtypes}\nDelay: {delay}\n")


reader = easyocr.Reader(["en"])
os.system("cls" if os.name == "nt" else "clear")
print("Program Succsessfuly Started!")


while True:
    img = numpy.array(pyautogui.screenshot(region=(0,0,800,600)))
    result = reader.readtext(img)
    count = sum("eternal" in x[1].lower() or "divine" in x[1].lower() or "secret" in x[1].lower() for x in result)
    if count > countold:
        if "1" in eggtypes and any("divine" in x[1].lower() for x in result):
            print("Divine Egg founded")
            if notiftype == "discord":
                try:
                    requests.post(dcwebhook, data={"content": "DIVINE EGG SPAWNED!\n@everyone"})
                except MissingSchema:
                    print("Discord WebHook link is Wrong Please Restart the Program and change it")
                    if os.path.exists("config.txt"):
                        os.remove("config.txt")
                    input("Press Enter To Close The Program...")
                    exit()
            elif notiftype == "Telegram":
                req = requests.post(f"https://api.telegram.org/bot{tgbottoken}/sendMessage",data={"chat_id": tgchatid, "text": "DIVINE EGG SPAWNED!"})
                if req.status_code == 404:
                    print("Telegram Bot Token is Wrong please restart the program and change it")
                    if os.path.exists("config.txt"):
                        os.remove("config.txt")
                    input("Press Enter To Close The Program...")
                    exit()
                if req.status_code == 400:
                    print("Telegram Chat ID is Wrong please restart the program and change it")
                    if os.path.exists("config.txt"):
                        os.remove("config.txt")
                    input("Press Enter To Close The Program...")
                    exit()
        if "2" in eggtypes and any("eternal" in x[1].lower() for x in result):
            print("Eternal Egg founded")
            if notiftype == "discord":
                try:
                    requests.post(dcwebhook, data={"content": "ETERNAL EGG SPAWNED!\n@everyone"})
                except MissingSchema:
                    print("Discord WebHook link is Wrong Please Restart the Program and change it")
                    if os.path.exists("config.txt"):
                        os.remove("config.txt")
                    input("Press Enter To CLose THe Program...")
                    exit()
            elif notiftype == "Telegram":
                requests.post(f"https://api.telegram.org/bot{tgbottoken}/sendMessage",data={"chat_id": tgchatid, "text": "ETERNAL EGG SPAWNED!"})
        if "3" in eggtypes and any("secret" in x[1].lower() for x in result):
            print("Secret Egg founded")
            if notiftype == "discord":
                try:
                    requests.post(dcwebhook, data={"content": "SECRET EGG SPAWNED!\n@everyone"})
                except MissingSchema:
                    print("Discord WebHook link is Wrong Please Restart the Program and change it")
                    if os.path.exists("config.txt"):
                        os.remove("config.txt")
                    input("Press Enter To CLose THe Program...")
                    exit()
            elif notiftype == "Telegram":
                requests.post(f"https://api.telegram.org/bot{tgbottoken}/sendMessage",data={"chat_id": tgchatid, "text": "SECRET EGG SPAWNED!"})
        countold = count
    elif count < countold:
        countold = count
    time.sleep(delay)