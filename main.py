import os
import colorama
from colorama import Fore, Back, Style

colorama.init()
path = "."
files = (file for file in os.listdir(path) 
         if os.path.isfile(os.path.join(path, file)))
folders = (file for file in os.listdir(path) 
         if not os.path.isfile(os.path.join(path, file)))
print(Style.BRIGHT + Fore.BLUE + " ".join(folders) + " " + Style.RESET_ALL + " ".join(files))