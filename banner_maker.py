from pyfiglet import Figlet
import os , colorama


def bannermaker():
    os.system("cls")
    colorama.init()
    print(f"{color}{part1}{reset}")

#font = Figlet(font="slant")
#part1 = font.renderText(str(input("[*]Enter Your Charachters > ")))
#color = colorama.Fore.LIGHTMAGENTA_EX
#reset = colorama.Fore.RESET

while(True):
    os.system("cls")
    font = Figlet(font="graffiti")
    part1 = font.renderText(str(input("[*]Enter Your Charachters > ")))
    color = colorama.Fore.LIGHTMAGENTA_EX
    reset = colorama.Fore.RESET
    bannermaker()
    input(" \"this made by Alireza-Mani!! ;)\" press 'Enter' to make another!")
