import Constant as keys
import Resp as R
from telegram.ext import *
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM, CallbackQuery

# ======================================================================
def start_command(update, context):
	update.message.reply_text("Hello\n Welcome to my Bot\n")


def help_command(update, context):
	update.message.reply_text("Whats happand my frind?!\nIf you have questions about the operation of the robot, you can read the description file.")


def new_event(update, context):
	update.message.reply_text("To create a new event, first choose a name:")


def message_handler(update, context):
    data = context.user_data
    # data["last_command"] = "message"
    text = str(update.message.text)
    result = R.responses(text, state)
    update.message.reply_text(result)


# ======================================================================
def main():
	# creat base bot
	updater = Updater(keys.API_K, use_context=True)
	dp = updater.dispatcher

	# add handlers
	dp.add_handler(CommandHandler("start", start_command))
	dp.add_handler(CommandHandler("help", help_command))


	# start bot
	updater.start_polling(0.5)
	updater.idle()


# ======================================================================
if __name__ == "__main__":
	main()
