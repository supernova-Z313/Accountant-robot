from telegram.ext import *

def javabha(update, context):
	date = context.user_data
	text = str(update.message.text).lower()
	if date["last_command"] == "creat":
		date["temp"] = [text]
		update.message.reply_text("Event seccessfully Addded.", quote=True)

	
	elif date["last_command"] == "add member":
		date["temp"] = [text]
		update.message.reply_text("Now send name of member in one line seperate with space", quote=True)
		date["last_command"] = "add_member 1"
	elif date["last_command"] == "add_member 1":
		text = text.split()
		for i in text:
			date[date["temp"]][i] = 0
		update.message.reply_text("Members added seccessfully.", quote=True)


	elif date["last_command"] == "add t":
		date["temp"] = [text]
		update.message.reply_text("Enter the name of the transaction:", quote=True)
		date["last_command"] = "add t 1"
	elif date["last_command"] == "add t 1":
		date["temp"].append(text)
		update.message.reply_text("Please add the names of people participating in this transaction:", quote=True)
		date["last_command"] = "add t 2"
	elif date["last_command"] == "add t 2":
		date["temp"].append(text.split())
		update.message.reply_text("Add the transaction amount:", quote=True)
		date["last_command"] = "add t 3"
	elif date["last_command"] == "add t 3":
		date["temp"].append(float(text))
		update.message.reply_text("Who made this purchase?", quote=True)
		date["last_command"] = "add t 4"
	elif date["last_command"] == "add t 4":
		for i in rnage(2, len(date["temp"])-2):
			date[date["temp"][0]][date["temp"][i]] -= date["temp"][-2]/(len(date["temp"])-4)
		date[date["temp"][0]][date["temp"][-1]] += date["temp"][-2]
		update.message.reply_text("Transaction added seccessfully.", quote=True)
	

	elif date["last_command"] == "Checkout":
		text = text.split()
		date[text[0]][text[1]] += float(text[3])
		date[text[0]][text[2]] -= float(text[3])
		update.message.reply_text("Checkout Was seccessfully.", quote=True)


	elif date["last_command"] == "state":
		text1 = "balance account state of members:\n"
		for i in date[text]:
			text1 += f"{i} = {date[text][i]}\n"
		update.message.reply_text(text1, quote=True)


	elif date["last_command"] == "state 2":
		text1 = "balance state of members:\n"
		for i in date[text]:
			text1 += f"{i} = {date[text][i]}\n"
		file = open("Balanceofaccounts.txt", "a+")
		file.write(text1)
		update.message.reply_document(file, quote=True)


	elif date["last_command"] == "del":
		text = text.split()
		date[text[0]].pop(text[1])
		update.message.reply_text("member delete seccessfully.", quote=True)


	else:
		update.message,reply_text("Sorry I cant undrestand what you say.", quote=True)


def start(update, context):
	update.message.reply_text("Hello my frind.\nWelcome To My Bot.\n", quote=True)
def error(update, context):
    print(f"Update {update} ==> {context.error}")


def creat(update, context):
	update.message.reply_text("Please enter the name of Event:", quote=True)
	date = context.user_data
	date["last_command"] = "creat"

def add_member(update, context):
	update.message.reply_text("Please enter name of Event you want to add member:")
	date = context.user_data
	date["last_command"] = "add member"

def add_t(update, context):
	update.message.reply_text("Enter Name of Event:")
	date = context.user_data
	date["last_command"] = "add t"

def Checkout(update, context):
	update.message.reply_text("Please enter name of Event Payer Receiver Amount in onr line seperate with space:", quote=True)
	date = context.user_data
	date["last_command"] = "Checkout"

def balances_state(update, context):
	update.message.reply_text("Please enter name of Event:", quote=True)
	date = context.user_data
	date["last_command"] = "state"

def send_balances(update, context):
	update.message.reply_text("Please enter name of Event:", quote=True)
	date = context.user_data
	date["last_command"] = "state 2"


def delete_member(update, context):
	update.member.reply_text("Please enter name of Event and member want to delete in one line seperate with space:", quote=True)
	date = context.user_data
	date["last_command"] = "del"


# addres of bot /////////////////////////////////////////////////////////////////////////////////
# @Myproject_sample7_bot
API_KEY = "5978945354:AAGFb-K_MtnGWofIDoQp8WnGC0UVd_NvNBE"
updater = Updater(API_KEY, use_context=True)
dis = updater.dispatcher
dis.add_handler(CommandHandler("start", start))
dis.add_handler(CommandHandler("creat_new_event", creat))
dis.add_handler(CommandHandler("add_member", add_member))
dis.add_handler(CommandHandler("add_t", add_t))
dis.add_handler(CommandHandler("checkout", Checkout))
dis.add_handler(CommandHandler("balances_state", balances_state))
dis.add_handler(CommandHandler("send_balances", send_balances))
dis.add_handler(CommandHandler("delete_member", delete_member))

dis.add_handler(MessageHandler(Filters.text, javabha))
dis.add_error_handler(error)
updater.start_polling(1)
print("bot started")
updater.idle()


