# Made by Lososik | https://github.com/Lososiik | https://discord.gg/46y8cqQUCt
# You need to have tokens.txt at same folder, at tokens.txt put your own tokens. For token bruteforcer you need to create .txt file named grab.txt
# You need to write to cmd: pip install discord, pip install pyautoui, pip install requests, pip install websocket, pip install emoji, pip install json, pip intall base64, pip install colorama. Without it, the code will not work.
# © PussyKiller discord multi tool

import threading
import colorama
import time
import json
import requests
import random
import string
from colorama import Fore
import os
from os import system
import discum



ur = 'https://discord.com/api/v9/channels/messages'
title = 'PenisKiller'
system(f'title {title}')
tokens = open('tokens.txt', 'r').read().splitlines()


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text


def spammer():
    tokens = open('tokens.txt', 'r').read().splitlines()
    clear = lambda: os.system('cls')
    cl = clear()


    colorama.init()


    tokens = open("tokens.txt", "r").read().splitlines()
    server = input(f'Server ID: ')
    channel = input(f'Chanel ID: ')
    mess = input(f'Message: ')
    delay = float(input(f'Delay: '))
    mas = input('MassPing y/n?: ').lower()

    tokens2 = open('tokens.txt').read().splitlines()[0:1]
    tokens3 = open('tokens.txt').read().splitlines()[1:2]
    tokens4 = open('tokens.txt').read().splitlines()[2:3]
    tokens5 = open('tokens.txt').read().splitlines()[4:5]
    tokens6 = open('tokens.txt').read().splitlines()[5:6]
    tokens7 = open('tokens.txt').read().splitlines()[6:7]
    tokens8 = open('tokens.txt').read().splitlines()[7:8]
    tokens9 = open('tokens.txt').read().splitlines()[9:10]
    tokens10 = open('tokens.txt').read().splitlines()[10:11]
    tokens11 = open('tokens.txt').read().splitlines()[11:]

    if mas == 'y':
        mess += '\n'
        mess1 = mess
        mess2 = mess
        mess3 = mess
        mess4 = mess
        mess5 = mess
        mess6 = mess
        mess7 = mess
        mess8 = mess
        mess9 = mess

        print(f'{Fore.LIGHTMAGENTA_EX}Use it with 500 members + on servers... {Fore.RESET}')
        time.sleep(1)
        print(f'{Fore.LIGHTMAGENTA_EX}Use 15 tokens +{Fore.RESET}')
        time.sleep(1)

        def Scrape():
            with open("tokens.txt") as f:
                firstline = f.readline().rstrip()
            bot = discum.Client(token=firstline)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('staff/users.txt', "w")
            for element in memberslist:
                f.write(f'<@{element}>' + '\n')

        Scrape()
        members1 = open('staff/users.txt').readlines()[0:50]
        for member1 in members1:
            mess += "".join(f'{member1}')
        members2 = open('staff/users.txt').readlines()[50:100]
        for member2 in members2:
            mess1 += "".join(f' {member2}')
        members3 = open('staff/users.txt').readlines()[100:150]
        for member3 in members3:
            mess2 += "".join(f'{member3}')
        members4 = open('staff/users.txt').readlines()[150:200]
        for member4 in members4:
            mess3 += "".join(f'{member4}')
        members5 = open('staff/users.txt').readlines()[200:250]
        for member5 in members5:
            mess4 += "".join(f'{member5}')
        members6 = open('staff/users.txt').readlines()[300:350]
        for member6 in members6:
            mess6 += "".join(f'{member6}')
        members7 = open('staff/users.txt').readlines()[350:400]
        for member7 in members7:
            mess7 += "".join(f'{member7}')
        members8 = open('staff/users.txt').readlines()[400:450]
        for member8 in members8:
            mess8 += "".join(f'{member8}')
        members9 = open('staff/users.txt').readlines()[450:500]
        for member9 in members9:
            mess9 += "".join(f'{member9}')

        def spam(token, mess):

            url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
            payloadd = {"content": mess1, "tts": False}
            payloaddd = {"content": mess2, "tts": False}
            payloadddd = {"content": mess3, "tts": False}
            payloaddddd = {"content": mess4, "tts": False}
            payload1 = {"content": mess5, "tts": False}
            payload2 = {"content": mess6, "tts": False}
            payload3 = {"content": mess7, "tts": False}
            payload4 = {"content": mess8, "tts": False}
            payload5 = {"content": mess9, "tts": False}

            header = {"authorization": token,
                       "accept": "*/*",
                       "accept-language": "en-GB",
                       "content-length": "90",
                       "content-type": "application/json",
                       "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                       "origin": "https://discord.com",
                       "sec-fetch-dest": "empty",
                       "sec-fetch-mode": "cors",
                       "sec-fetch-site": "same-origin",
                       "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                       "x-debug-options": "bugReporterEnabled",
                       "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"

                       }

            while True:
                time.sleep(delay)
                src2 = requests.post(url, headers=header, json=payloadd)
                src3 = requests.post(url, headers=header, json=payloaddd)
                src4 = requests.post(url, headers=header, json=payloadddd)
                src5 = requests.post(url, headers=header, json=payloaddddd)
                src7 = requests.post(url, headers=header, json=payload1)
                src8 = requests.post(url, headers=header, json=payload2)
                src9 = requests.post(url, headers=header, json=payload3)
                src10 = requests.post(url, headers=header, json=payload4)
                src11 = requests.post(url, headers=header, json=payload5)

                if src2.status_code or src3.status_code or src4.status_code or src5.status_code or src7.status_code or src9.status_code or src8.status_code or src10.status_code or src11.status_code == 429:
                    ratelimit = json.loads(src2.content or src3.content or src4.content or src5.content or src7.content or src8.content or src9.content or src10.content or src11.content)

                    try:
                        print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Ratelimit for",
                              str(float(ratelimit['retry_after'])) + " seconds")
                        time.sleep(float(ratelimit['retry_after']))
                    except:
                        pass

                elif src2.status_code or src3.status_code or src4.status_code or src5.status_code or src7.status_code or src9.status_code or src8.status_code or src10.status_code or src11.status_code  == 200:
                    print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{mess1 or mess2 or mess3 or mess4 or mess5 or mess6 or mess7 or mess8 or mess9} sent')

                elif src2.status_code or src3.status_code or src4.status_code or src5.status_code or src7.status_code or src9.status_code or src8.status_code or src10.status_code or src11.status_code  == 401:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Invalid token')
                elif src2.status_code or src3.status_code or src4.status_code or src5.status_code or src7.status_code or src9.status_code or src8.status_code or src10.status_code or src11.status_code  == 404:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Not found ¯\_(ツ)_/¯')
                elif src2.status_code or src3.status_code or src4.status_code or src5.status_code or src7.status_code or src9.status_code or src8.status_code or src10.status_code or src11.status_code  == 403:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Token havent got access to this channel')


        def thread1():
            text1 = mess1
            text2 = mess2
            text3 = mess3
            text4 = mess4
            text5 = mess5
            text6 = mess6
            text7 = mess7
            text8 = mess8
            text9 = mess9

            for token1 in tokens2:
                threading.Thread(target=spam, args=(token1, text1)).start()
            for token2 in tokens3:
                threading.Thread(target=spam, args=(token2, text2)).start()
            for token3 in tokens4:
                threading.Thread(target=spam, args=(token3, text3)).start()
            for token4 in tokens5:
                threading.Thread(target=spam, args=(token4, text4)).start()
            for token5 in tokens6:
                threading.Thread(target=spam, args=(token5, text5)).start()
            for token6 in tokens7:
                threading.Thread(target=spam, args=(token6, text6)).start()
            for token7 in tokens8:
                threading.Thread(target=spam, args=(token7, text7)).start()
            for token8 in tokens9:
                threading.Thread(target=spam, args=(token8, text8)).start()
            for token9 in tokens10:
                threading.Thread(target=spam, args=(token9, text9)).start()
            for token10 in tokens11:
                threading.Thread(target=spam, args=(token10, text5)).start()

    else:
        ch = input('Do you want append random string: y/n?: ').lower()

        def spam(token, mess):

            if ch == 'y':
                mess += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))

            elif ch == 'n':
                pass

            else:
                pass

            url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
            payload = {"content": mess, "tts": False}
            header = {"authorization": token,
                      "accept": "*/*",
                      "accept-language": "en-GB",
                      "content-length": "90",
                      "content-type": "application/json",
                      "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                      "origin": "https://discord.com",
                      "sec-fetch-dest": "empty",
                      "sec-fetch-mode": "cors",
                      "sec-fetch-site": "same-origin",
                      "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                      "x-debug-options": "bugReporterEnabled",
                      "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                      }

            while True:
                time.sleep(delay)
                src = requests.post(url, headers=header, json=payload)

                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Ratelimit for",
                          str(float(ratelimit['retry_after'])) + " seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif src.status_code == 200:
                    print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{mess} sent')

                elif src.status_code == 401:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Invalid token')
                elif src.status_code == 404:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Not found ¯\_(ツ)_/¯')
                elif src.status_code == 403:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Token havent got access to this channel')

        def thread():
            text = mess
            for token in tokens:
                threading.Thread(target=spam, args=(token, text)).start()

    if mas == 'y':
        start = input(f'Press eny key to start: ')
        start = thread1()
    else:
        start = input(f'Press eny key to start: ')
        start = thread()


spammer()