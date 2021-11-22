from colorama import Fore, Back, Style, init
import util
import configparser
import os.path
init()

spaces = " "*26

config = configparser.ConfigParser()
if os.path.isfile("save.ini"):
	config.read("save.ini")
else:
	open("save.ini", 'a').close()
	print(f"{Fore.RED}Please relaunch the game, save file was lost but recreated.")
	exit()

def mmenu():
	print(f"""
	{Fore.YELLOW}{spaces}CryptoGen v1.0.1

	{Fore.GREEN}{spaces}1. New Game
	{Fore.BLUE}{spaces}2. Continue
	{Fore.RED}{spaces}3. Exit
	""")
	choice = util.cinp()
	if choice == None or len(choice.replace(" ", "")) == 0:
		mmenu()
	elif choice == "1":
		gamestart()
	elif choice == "3":
		print("\n"*100 + " "*34 + Fore.RED + "CryptOS v6.9" + "\n" + " "*34 + Fore.BLUE + "Turning off...")
		exit()
	else:
		mmenu()

def gamestart():
	print(f"{Fore.RED}{Back.WHITE}TEMPLATE")

if __name__ == "__main__":
	mmenu()