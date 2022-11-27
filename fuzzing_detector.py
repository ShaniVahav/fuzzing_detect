from time import sleep

from spellchecker import SpellChecker

count = 0
check_spell = SpellChecker()
line = ''
with open("/var/log/auth.log", "r") as f:
    f.seek(0, 2)
    print("monitor...")
    while True:
        line = f.readline()  # a line in the log
        while line == '':
            sleep(5)
            line = f.readline()

        if ("ssh" or "sshd") and "error:" and "invalid" and ("format" or "protocol") in line:
            count += 1
            if count >= 5:
             print("Fuzzing detected")
             exit()
        else:
          words_arr = line.split()  # the words in the line
          # if the all words is garbage so it's fuzzing
          for i in range(len(words_arr)):
            if not check_spell.unknown(words_arr[0]):  # check for garbage values
             break
            print("Fuzzing detected")
            exit()
