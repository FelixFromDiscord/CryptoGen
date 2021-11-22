from colorama import Fore, Back, Style, init
import util
import configparser
import os.path
import requests
init()

cfg = configparser.ConfigParser()
if os.path.isfile("save.ini"):
	cfg.read("save.ini")
else:
	req = requests.get("https://raw.githubusercontent.com/FelixFromDiscord/CryptoGen/main/util/templ.ini").text
	f = open("save.ini", "w")
	f.write(req)
	f.close()
	print(f"{Fore.RED}Please relaunch the game, save file was lost but recreated.")
	exit()

#####
username = cfg["Character"]["Name"]
#####

def gamestart():
	name = util.cinp("Enter your name # ")
	if name.__contains__(" "):
		print(f"{Fore.RED}Names can not contain spaces!\n")
		gamestart()
	elif len(name) > 10:
		print(f"{Fore.RED}Name is too long, try again! (max 10 characters)\n")
		gamestart()
	elif len(name) < 3:
		print(f"{Fore.RED}Are you serious? (min 3 characters)\n")
	elif len(name) == 0:
		gamestart()
	else: 
		print("")
		username = name
		cfg["Character"]["Name"] = name
		gamemain()

def gamemain():
	util.cprt(username, user)