import Constant as keys
import responses as R
from telegram.ext import *
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM, CallbackQuery
from os import system

# ---------------------------------------------------------------------------------------------

def start(update, context):
	user_name = update.effective_user['first_name']
	user_dict = context.user_data
	user_dict["Where"] = "__Home__"
	user_dict["State"] = 0
	user_dict["temp"] = []
	kb = [[KeyboardButton("/add_member"), KeyboardButton("/share")], [KeyboardButton("/transaction")], 
		  [KeyboardButton("/checkout"), KeyboardButton("/data_file")], [KeyboardButton("/back_to_home")]]
	kb_m = ReplyKeyboardMarkup(kb, one_time_keyboard=True)
	user_dict["KeyboardButton"] = kb_m
	update.message.reply_text(f"🆔 Hello {user_name}.\n🤖 Welcome to Money Management Robot.💯\n"
							   "📦 You can use the following command to start.\n🔰 /add_event\n🔰 /go_to_event\n"
							   "❗️ Run the /help command to get help.", quote=True)

"""/////////////////////////////////////////////////////////////////////////////////////////////"""

def help_u(update, context):
	user_dict = context.user_data
	user_dict["State"] = 1
	user_dict["temp"] = []
	update.message.reply_text("hello", quote=True)

"""/////////////////////////////////////////////////////////////////////////////////////////////"""

def messages(update, context):
	user_dict = context.user_data
	text = str(update.message.text)
	result = R.process(text, user_dict, user_dict["State"])
	if user_dict["State"] == -1:
		kb_m = user_dict["KeyboardButton"]
		update.message.reply_text(result, quote=True, reply_markup=kb_m)
	else:
		update.message.reply_text(result, quote=True)

"""/////////////////////////////////////////////////////////////////////////////////////////////"""
# remove this
def error(update, context):
	print(f"{update} \n {context.error}")

"""/////////////////////////////////////////////////////////////////////////////////////////////"""

def add_event(update, context):
	user_dict = context.user_data
	user_dict["State"] = 2
	user_dict["temp"] = []
	update.message.reply_text("Please enter the name of the event:", quote=True)

"""/////////////////////////////////////////////////////////////////////////////////////////////"""

def go_to_event(update, context):
	user_dict = context.user_data
	if len(user_dict) > 3:
		user_dict["State"] = 3
		user_dict["temp"] = []
		update.message.reply_text("Please enter the name of the event you want to enter:", quote=True)
	else:
		update.message.reply_text("❌ Please add an event first.\n⭕ Use this command to add:\n🔰 /add_event")

"""/////////////////////////////////////////////////////////////////////////////////////////////"""

def all_event(update, context):
	user_dict = context.user_data
	user_dict["State"] = 4
	user_dict["temp"] = []
	events = list(user_dict.keys())
	events.remove("temp")
	events.remove("Where")
	events.remove("State")
	if len(events) > 0:
		result = "📃 Events List:\n"
		for i in events:
			result += f"📦 {i}\n"
		update.message.reply_text(result, quote=True)
	else:
		update.message.reply_text("❌ No events have been added yet.", quote=True)

"""/////////////////////////////////////////////////////////////////////////////////////////////"""

def back_to_home(update, context):
	if context.user_data["Where"] != "__Home__":
		context.user_data["Where"] = "__Home__"
		context.user_data["State"] = 0
		context.user_data["temp"] = []
		update.message.reply_text("🏠 You have returned to the Home page.\n🛟 Suggested commands:\n"
								  "🔰 /add_event\n🔰 /all_event\n🔰 /go_to_event")
	else:
		update.message.reply_text("🏠 You are in home already.\n🛟 Suggested commands:\n"
								  "🔰 /add_event\n🔰 /all_event\n🔰 /go_to_event")

"""/////////////////////////////////////////////////////////////////////////////////////////////"""

def add_member(update, context):
	user_dict = context.user_data
	user_dict["State"] = 5
	user_dict["temp"] = []
	update.message.reply_text("Please enter a name or enter the 'exit' to exit:", quote=True)

"""/////////////////////////////////////////////////////////////////////////////////////////////"""

def share(update, context):
	user_dict = context.user_data
	user_dict["State"] = -1
	event_name = user_dict["Where"]
	kb_m = user_dict["KeyboardButton"]
	if len(user_dict[event_name]) > 0:
		names = list(user_dict[event_name].keys())
		moneys = list(user_dict[event_name].values())
		result = f"📋 Status of accounts in event {event_name}:\n"
		for ind, i in enumerate(names):
			result += f"🆔 {i} = {moneys[ind]}\n"
		update.message.reply_text(result, quote=True, reply_markup=kb_m)
	else:
		update.message.reply_text("⛔️ Please enter the names of the participants first.\n"
								  "⭕ Use this command to add member:\n🔰 /add_member", quote=True, reply_markup=kb_m)

"""/////////////////////////////////////////////////////////////////////////////////////////////"""

def transaction(update, context):
	user_dict = context.user_data
	event_name = user_dict["Where"]
	user_dict["temp"] = []
	kb_m = user_dict["KeyboardButton"]
	if len(user_dict[event_name]) > 0:
		user_dict["State"] = 6
		update.message.reply_text("Please enter the name of the transaction:", quote=True)
	else:
		update.message.reply_text("⛔️ Please enter the names of the participants first.\n"
								  "⭕ Use this command to add member:\n🔰 /add_member", quote=True, reply_markup=kb_m)		


"""/////////////////////////////////////////////////////////////////////////////////////////////"""

def checkout(update, context):
	user_dict = context.user_data
	event_name = user_dict["Where"]
	user_dict["temp"] = []
	kb_m = user_dict["KeyboardButton"]
	if len(user_dict[event_name]) > 0:
		user_dict["State"] = 7
		update.message.reply_text("Who wants to pay?", quote=True)
	else:
		update.message.reply_text("⛔️ Please enter the names of the participants first.\n"
								  "⭕ Use this command to add member:\n🔰 /add_member", quote=True, reply_markup=kb_m)		

"""/////////////////////////////////////////////////////////////////////////////////////////////"""

def data_file(update, context):
	user_dict = context.user_data
	user_dict["State"] = -1
	event_name = user_dict["Where"]
	kb_m = user_dict["KeyboardButton"]
	if len(user_dict[event_name]) > 0:
		names = list(user_dict[event_name].keys())
		moneys = list(user_dict[event_name].values())
		result = f"Status of accounts in event {event_name}:\n"
		for ind, i in enumerate(names):
			result += f"{i} = {moneys[ind]}\n"
		with open("state.txt", "a+") as txt:
			txt.write(result)
		update.message.reply_document(open("state.txt", "r+"), caption=f"📋 Status of accounts in event {event_name}:\n", quote=True, reply_markup=kb_m)
		system("rm state.txt")
	else:
		update.message.reply_text("⛔️ Please enter the names of the participants first.\n"
								  "⭕ Use this command to add member:\n🔰 /add_member", quote=True, reply_markup=kb_m)

# ---------------------------------------------------------------------------------------------

def main():
	updater = Updater(keys.api, use_context=True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help_u))
	dp.add_handler(CommandHandler("add_event", add_event))
	dp.add_handler(CommandHandler("go_to_event", go_to_event))
	dp.add_handler(CommandHandler("all_event", all_event))
	dp.add_handler(CommandHandler("back_to_home", back_to_home))
	dp.add_handler(CommandHandler("add_member", add_member))
	dp.add_handler(CommandHandler("transaction", transaction))
	dp.add_handler(CommandHandler("share", share))
	dp.add_handler(CommandHandler("checkout", checkout))
	dp.add_handler(CommandHandler("data_file", data_file))
	# remove this
	dp.add_error_handler(error)
	dp.add_handler(MessageHandler(Filters.text, messages))

	updater.start_polling(0.25)
	print("bot started ...")
	updater.idle()

main()
# my bot id = @money_management2_bot

"""
user_dict = {
	Where : str             (__Home__, trip, ...)
	State : int             (0, 1, ...)
	temp  : list            (amount, names, ...)
	_Event_name_ : dict     ("ali" : 0, "ahmad" : 500)
}
"""
""" ⛔️⭕✅🌀❌💳🤖📦🔰🆔❗️🛟💯⛺️🏕💸👥 🚀📃📋🏠👥"""
