import Constant as keys
import Resp as R
from os import system
from telegram.ext import *
# from telegram import KeyboardButton, ReplyKeyboardMarkup
# from telegram import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM, CallbackQuery

# ======================================================================
def start_command(update, context):
	data = context.user_data
	data["last_command"] = 0
	data["events"] = []
	update.message.reply_text("Hello\n Welcome to Accountant robot.\nTo start, you can use the following commands:"
							  "\n/new_event - Create a new event.\n/go_to_event - Go to an event.")
# ----------------------------------------------------------------------


def help_command(update, context):
	data = context.user_data
	data["last_command"] = 1
	update.message.reply_text("Commands:\n"
							  "\n/new_event - Create a new event.\n/go_to_event - Go to an event."
							  "\n/add_member - Add a new member to the event.\n/add_transaction - Add a transaction."
							  "\n/checkout - Checkout.\n/show_state - Display the status of accounts."
							  "\n/send_state - Sending account status as a text file.\n"
							  "\nIf you have more questions about the operation of the robot, you can read the description file.")
# ----------------------------------------------------------------------


def new_event(update, context):
	update.message.reply_text("To create a new event, first choose a name:")
	data = context.user_data
	data["last_command"] = 2
# ----------------------------------------------------------------------


def go_to_event(update, context):
	data = context.user_data
	data["last_command"] = 3
	update.message.reply_text("Please enter the destination event name.")
# ----------------------------------------------------------------------


def add_member(update, context):
	data = context.user_data
	if data.get("Head"):
		data["last_command"] = 4
		update.message.reply_text("Please enter the name of the event member:")
	else:
		update.message.reply_text("Please enter an event first.")
# ----------------------------------------------------------------------


def Add_transaction(update, context):
	data = context.user_data
	# should chan this
	if data.get("Head"):
		if len(data[data["Head"]]) != 0:
			data["last_command"] = 5
			update.message.reply_text("Please enter the name of the transaction:")
		else:
			update.message.reply_text("Please enter some member first.")
	else:
		update.message.reply_text("Please enter an event first.")
# ----------------------------------------------------------------------


def show_state(update, context):
	data = context.user_data
	# should chan this
	if data.get("Head"):
		if len(data[data["Head"]]) != 0:
			data["last_command"] = 6
			users = list(data[data["Head"]].keys())
			states = list(data[data["Head"]].values())
			head = data["Head"]
			text = f"In event {head}\nstatus of accounts:\n"
			for ind, i in enumerate(users):
				text += f"{i} = {states[ind]}\n"
			update.message.reply_text(text)
		else:
			update.message.reply_text("Please enter some member first.")
	else:
		update.message.reply_text("Please enter an event first.")
# ----------------------------------------------------------------------


def send_state(update, context):
	data = context.user_data
	# should chan this
	if data.get("Head"):
		if len(data[data["Head"]]) != 0:
			data["last_command"] = 7
			users = list(data[data["Head"]].keys())
			states = list(data[data["Head"]].values())
			head = data["Head"]
			text = f"In event {head}\nstatus of accounts:\n"
			for ind, i in enumerate(users):
				text += f"{i} = {states[ind]}\n"
			with open("status_accounts.txt", "a+") as f:
				f.write(text)
			update.message.reply_document(open("status_accounts.txt", "r+"), caption="status of accounts")
			system("rm status_accounts.txt")
		else:
			update.message.reply_text("Please enter some member first.")			
	else:
		update.message.reply_text("Please enter an event first.")
# ----------------------------------------------------------------------


def Checkout(update, context):
	data = context.user_data
	# should chan this
	if data.get("Head"):
		if len(data[data["Head"]]) != 0:
			data["last_command"] = 8
			update.message.reply_text("Please enter the name of the payer:")
		else:
			update.message.reply_text("Please enter some member first.")			
	else:
		update.message.reply_text("Please enter an event first.")
# ----------------------------------------------------------------------


def message_handler(update, context):
    data = context.user_data
    text = str(update.message.text)
    state = data["last_command"]
    result = R.responses(text, state, data)
    update.message.reply_text(result)


def error(update, context):
    print(f"Update {update} ==> {context.error}")

# ======================================================================
def main():
	# creat base bot
	updater = Updater(keys.API_K, use_context=True)
	dp = updater.dispatcher

	# add handlers
	dp.add_handler(CommandHandler("start", start_command))
	dp.add_handler(CommandHandler("help", help_command))
	dp.add_handler(CommandHandler("new_event", new_event))
	dp.add_handler(CommandHandler("go_to_event", go_to_event))
	dp.add_handler(CommandHandler("add_member", add_member))
	dp.add_handler(CommandHandler("add_transaction", Add_transaction))
	dp.add_handler(CommandHandler("show_state", show_state))
	dp.add_handler(CommandHandler("send_state", send_state))
	dp.add_handler(CommandHandler("checkout", Checkout))
	# ------------
	dp.add_handler(MessageHandler(Filters.text, message_handler))
	dp.add_error_handler(error)


	# start bot
	updater.start_polling(0.5)
	updater.idle()


# ======================================================================
if __name__ == "__main__":
	main()
