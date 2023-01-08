def main():
	# Import base code
	from bin import Bot
	from bin import Responses as R

	# Import librarys
	try:
		from sys import exit
		from os import environ, close
		from dotenv import load_dotenv
	except ImportError:
		print("Import Error:")
		print("\tThe program cannot be run because it needs the dotenv library to load API.")
		print("\tyou can use this commands to install it:")
		print("\tpip3 install python-dotenv \n\t # or")
		print("\tpip3 install -r requirements.txt")
		exit()

	try:
		# from telegram.ext import *
		from telegram import KeyboardButton, ReplyKeyboardMarkup
		from telegram import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM, CallbackQuery
	except ImportError:
		print("Import Error:")
		print("\tThe program cannot be run because it needs the python-telegram-bot library.")
		print("\tyou can use this commands to install it:")
		print("\tpip3 install python-telegram-bot \n\t # or")
		print("\tpip3 install -r requirements.txt")
		exit()
	else:
		print("librarys imported successfully.")

	try:
		load_dotenv()
		API_Key = environ.get("API_Key", "hey")
	except:
		print("cant load API Key, check the .env file.")
		exit()
	else:
		print("API-Key Loaded successfully")


if __name__ == "__main__":
	main()