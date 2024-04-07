import pyautogui as bot
import time as tm

bot.PAUSE = 1

bot.hotkey('ctrl','shift','`')

comandos = ["git add ." , "git commit -m 'AutoCommit' " , "git push", "exit"]

for c in comandos:
    if c == "exit":
        tm.sleep(5)
    bot.write(c)
    bot.press('Enter')