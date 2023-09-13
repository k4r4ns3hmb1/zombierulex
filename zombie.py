from urllib import response
import mechanize
import uuid
import os
import datetime
import time
import sys
from time import sleep
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)


	
url = 'https://m.facebook.com/login'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('xdg-open https://www.facebook.com/vinodkumar.vinodkjmar?mibextid=haYZDX')
        
def sp(stri):
    for letter in stri:
        print(letter, end = "")
        sys.stdout.flush()
        sleep(0.03)

logo ="""\033[1;36mWELCOME T0 ZOMBI3 RUL3X TOOL

\033[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[1;30m ____  ____  _      ____    ____  _     _     ________  _
\033[1;30m/  __\/  _ \/ \__/|/  _ \  /  __\/ \ /\/ \   /  __/\  \//
\033[1;30m|  \/|| / \|| |\/||| / \|  |  \/|| | ||| |   |  \   \  / 
\033[1;30m|    /| \_/|| |  ||| |-||  |    /| \_/|| |_/\|  /_  /  \ 
\033[1;30m\_/\_\\____/\_/  \|\_/ \|  \_/\_\\____/\____/\____\/__/\\
                                         
\033[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[1;36m━▷ \033[1;36m𝙊𝙒𝙉𝙀𝙍    \033[1;36m◈✙◈\033[1;33mMR KARAN SEHMBI
\033[1;36m━▷ \033[1;36m𝙏𝙀𝘼𝙈     \033[1;36m◈✙◈\033[1;33mTEAM OF ZOMBIE RULEX
\033[1;36m━▷ \033[1;36m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 \033[1;36m◈✙◈ \033[1;33mfb.com/https://www.facebook.com/vinodkumar.vinodkjmar
\033[1;36m━▷ \033[1;36m𝙎𝙏𝘼𝙏𝙐𝙎  \033[1;36m◈✙◈ \033[1;33mCONVO LOADER TOOL
\033[1;36m━▷ \033[1;36m𝙑𝙀𝙍𝙎𝙄𝙊𝙉  \033[1;36m◈✙◈ \033[1;33m9.0
\033[1;36m━▷ \033[1;36m𝙁𝙀𝙀𝙇 𝙏𝙃𝙀 𝙋𝙊𝙒𝙀𝙍 𝙈𝙍 𝙆𝘼𝙍𝘼𝙉 𝙎𝙀𝙃𝙈𝘽𝙄 𝙊𝙒𝙉𝙀𝙍 𝙊𝙁 𝙕𝙊𝙈𝘽𝙄𝙀 𝙍𝙐𝙇𝙀𝙓 
\033[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●"""



def login():
    browser.open(url)
    browser.select_form(nr = 0)
    browser.form['email'] = USERNAME
    browser.form['pass'] = PASSWORD
    r = browser.submit()
    f = open("login.html", "wb")
    f.write(r.read())
    f.close()
    browser.select_form(nr = 0)
    print("\033[1m\033[36m", end = "")
    print('\033[1;32m[+]================================[+]')
    sp("\033[1;32m[?] Enter the 2 factor code by google authenticator\n")
    print('\033[1;32m[+]================================[+]')
    apr = str(input('\033[1;32m[?] Enter Code : '))
    try:
        browser.form['approvals_code'] = apr
    except mechanize._form_controls.ControlNotFoundError:
        print("Wrong password or some shit, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    browser.select_form(nr = 0)
    try:
        browser.form['name_action_selected'] = ['save_device']
    except mechanize._form_controls.ControlNotFoundError:
        print("Some shit gone down, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    f = open("full_login_" + str(USERNAME) + ".html", "wb")
    f.write(r.read())
    f.close()

def findtextchat(curl):
    r = browser.open(curl)
    x = browser.title()
    if x == "Review recent login":
        print("\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.")
        exit(1)
    if x == "Login approval needed":
        print("\nYour account is stuck on verification\nPlease do it and then re run the program.")
        exit(1)
    if x == "Epsilon":
        print("\nYour account got locked, recover it kindly and re run the script.")
        exit(1)

def sendtextconvo(comment):
    try:
        browser.select_form(nr = 1)
    except mechanize._mechanize.FormNotFoundError:
        print("Some error occured while finding text area, please check your account")
        exit(1)
    try:
        browser.form['body'] = comment
    except mechanize._form_controls.ControlNotFoundError:
        print("Some error occured while filling text, please check your account")
        exit(1)
    r = browser.submit()
    e = datetime.datetime.now()
    print("\033[1;32m",end = "")
    print (e.strftime("MESSEGE SEND SUCCESSFUL :: Date - %d/%m/%Y  Time - %I:%M:%S %p"))
    print(">>  WELCOME TO ZOMBI3 RULEX :: ", hater, line, "\n")
os.system('clear')
print("\033[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●")
print("\033[1;33;40m", end = "")
print(logo)
print('  ☾⋆                                           ⋆☽ ')
sp("\033[1;32m[+] \033[1;32m𝗟𝗢𝗚𝗜𝗡 𝗙𝗕 𝗜𝗗 𝗧𝗬𝗣𝗘 𝗡𝗨𝗠𝗕𝗘𝗥 & 𝗘𝗠𝗔𝗜𝗟 𝗔𝗡𝗗 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 \n")
print('  ☾⋆                                           ⋆☽ ')
print('\033[1;32m[+]================================[+]')
USERNAME = str(input('\033[1;32m[+] 𝗧𝗬𝗣𝗘 𝗡𝗨𝗠𝗕𝗘𝗥 & 𝗘𝗠𝗔𝗜𝗟  : '))
print("\033[1;33;40m", end = "")
print('\033[1;32m[+]================================[+]')
sp("\033[1;32m[+] \033[1;32m𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟 \n")
print('\033[1;32m[+]================================[+]')
PASSWORD = str(input('\033[1;32m[?] 𝗧𝗬𝗣𝗘 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 : '))
login()
print("\033[1;34;40m", end = "")
print('\033[1;32m[+]================================[+]')
sp("\033[1;32m[?] \033[1;32mEnter Chat/inbox Link\n")
print('\033[1;32m[+]================================[+]')
cid = str(input('\033[1;32m[?] \033[1;32mEnter Link : '))
curl = 'https://m.facebook.com/messages/t/' + str(cid)

print("\033[1;34;40m", end = "")
print('\033[1;32m[+]================================[+]')
sp("\033[1;32m[?] \033[1;32mEnter File Name\n")
print('\033[1;32m[+]================================[+]')
np = str(input('\033[1;32m[?] \033[1;32mEnter File Name : '))
f = open(np, 'r')
lines = f.readlines()
f.close()
print("\033[1;33;40m", end = "")
print('\033[1;32m[+]================================[+]')
hater = input(' [+] Haters Name : ')
print("\033[1;33;40m", end = "")
print('\033[1;32m[+]================================[+]')
sp("\033[1;32m[?] \033[1;32mEnter The Time Delay In Seconds\n")
print('\033[1;32m[+]================================[+]')
t = int(input('\033[1;32m[?] \033[1;32mEnter Time : '))

os.system('clear')
print(logo)

count = 0
while True:
    try:
        for line in lines:
            if len(line) > 3:
                if count != 0:
                    sleep(t)
                findtextchat(curl)
                sendtextconvo(hater + line)
                count += 1
                if count % 10 == 0:
                    sleep(1)
                    clear()
                    print("\033[1;32m")
    except Exception as e:
        print(e)
        sleep(3)