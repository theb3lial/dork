import os
import time

def clear():
    os.system(["clear", "cls"][os.name == "nt"])

def art():
    print(f"""{fCiano}
           ,   ,
          /////|
         ///// |
        |~~~|  |
        |===|  |
        |   |  |  {fReset}theb3lial{fCiano}
        |   |  |
        |   | /
        |===|/
        '---'\n{fReset}""")

fPreto = '\033[2;30m'
fBranco = '\033[1;97m'
fVermelho = '\033[1;91m'
fAzul = '\033[1;34m'
fAmarelo = '\033[1;33m'
fVerde = '\033[1;92m'
fCiano = '\033[1;36m'
fReset = '\033[m'

file = open("path.txt", "r")
path = file.readlines()
path = list(map(lambda a: a.strip(), path))

linhas = 0
for x in path:
    linhas = linhas + 1

clear()
time.sleep(1)
art()

inurl = input(f"Nome do diretório {fCiano}‒ {fReset}")

with open("dork.txt", "w") as f:
    for x in range(0, linhas):
        f.write(f"{inurl}{path[x]}\n")
print("Salvo em dork.txt")
