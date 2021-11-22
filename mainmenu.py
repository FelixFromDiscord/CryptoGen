from colorama import Fore, Back, Style, init
import util
import game
import configparser
init()

spaces = " "*26

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
		print("")
		game.gamestart()
	elif choice == "2":
		print("")
		game.gamemain()
	elif choice == "3":
		print("\n"*100 + " "*34 + Fore.RED + "CryptOS v6.9" + "\n" + " "*34 + Fore.BLUE + "Turning off...")
		exit()
	else:
		mmenu()

if __name__ == "__main__":
	mmenu()
