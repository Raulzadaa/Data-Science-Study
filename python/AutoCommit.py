import pyautogui as bot

bot.PAUSE = 2

bot.hotkey('ctrl','shift','`')

comandos = ["git add ." , "git commit -m 'AutoCommit' " , "git push"]

for c in comandos:
    bot.write(c)
    bot.press('Enter')