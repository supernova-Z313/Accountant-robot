from telegram.ext import *
from telegram import KeyboardButton, ReplyKeyboardMarkup
import requests as R

# ===============================================================

button_1 = [[KeyboardButton("/show_favorite_list"), KeyboardButton("/search_film")]]
mk_button_1 = ReplyKeyboardMarkup(button_1, one_time_keyboard=True)

# ===============================================================
def start(update, context):
	data = context.user_data
	update.message.reply_text("Hello💐\nWelcome to my film bot.🎬\nIf you need help use /help command.❔", reply_markup=mk_button_1, quote=True)
	data["command"] = 0
	data["favorites"] = []

# ===============================================================
def help_m(update, context):
	data = context.user_data
	update.message.reply_text("❗️Oh you need help.You can see description of each command on readme file:\n\n", reply_markup=mk_button_1, quote=True)
	data["command"] = 1
	# 🔰

# ===============================================================
def favorite_list(update, context):
	data = context.user_data
	if len(data["favorites"]) == 0:
		update.message.reply_text("❌You have not added a movie to this list yet.\n⭕️Please add a video first with the help of the command below.\n/search_film", reply_markup=mk_button_1, quote=True)
	else:
		temp = "🔱List of your favorite films:\n"
		for i in data["favorites"]:
			temp += f"{i}\n"
		temp += "\n🗂 If you want to save this list for yourself, use /send_favorite command.\n"
		update.message.reply_text(temp, reply_markup=mk_button_1, quote=True)
	data["command"] = 2

# ===============================================================
def send_favorite_list(update, context):
	if len(data["favorites"]) == 0:
		update.message.reply_text("❌You have not added a movie to this list yet.\n⭕️Please add a video first with the help of the command below.\n/search_film", reply_markup=mk_button_1, quote=True)
	else:
		temp = "List of your favorite films:\n"
		for i in data["favorites"]:
			temp += f"{i}\n"
		with open("favorites.txt", "a+") as f:
			f.write(temp)
			update.message.reply_document(f, reply_markup=mk_button_1, quote=True)
	data["command"] = 3

# ===============================================================
def search_film(update, context):
	data = context.user_data
	temp = R.get("https://moviesapi.ir/api/v1/genres")
	if temp.status_code == 200:
		temp = temp.json()
		temp2 = []
		for i in temp:
			temp2.append(i["name"])
		text = "🌐Please choose one of the genres below:\n"
		for i in temp2:
			text += f"💠 {i}\n"
		update.message.reply_text(text, quote=True)
		data["all_g"] = temp2
	data["command"] = 4

# ===============================================================
def messages(update, context):
	data = context.user_data
	text = str(update.message.text)
	if data['command'] == 4:
		if text in data["all_g"]:
			data["genr"] = text
			update.message.reply_text("The genre was successfully selected.✅", quote=True)
			genr_id = data["all_g"].index(text)
			temp = R.get(f"https://moviesapi.ir/api/v1/genres/{genr_id}/movies")
			if temp.status_code == 200:
				data["films"] = temp.json()["data"]
				temp_text = "🎬 Choose one of the movies below:\n"
				for i in temp.json()["data"]:
					name = i["title"]
					temp_text += f"🔹 {name}\n"
				update.message.reply_text(temp_text, quote=True)
				data["command"] = 5
		else:
			update.message.reply_text("⛔️ Input is invalid. Try again.")

	elif data['command'] == 5:
		names = []
		for i in data["films"]:
			names.append(i["title"])
		if text in names:
			temp_text = ""
			for i in data["films"]:
				if i["title"] == text:
					temp_text += "🌀 Title: " + i["title"] + "\n"
					temp_text += "💠 Year: " + i["year"] + "\n"
					temp_text += "🏳️ Country: " + i["country"] + "\n"
					temp_text += "Ⓜ️ IMDB rating: " + i["imdb_rating"] + "\n"
					temp_text += "✴️ Genres: " + i["genres"][0] + "\n"
					data["last seens film"]  = i["title"]
					break
			temp_text += "\nIf you want this movie to be added to the list of your favorite movies, enter the number 1."
			data["command"] = 6
			update.message.reply_text(temp_text, reply_markup=mk_button_1, quote=True)
		else:
			update.message.reply_text("⛔️ Input is invalid. Try again.", quote=True)

	elif data["command"] == 6:
		if text == "1":
			print(data)
			print()
			data["favorites"].append(data["last seens film"])
			update.message.reply_text("Film added to favorites movies.✅", quote=True)
		else:
			update.message.reply_text("⛔️ Input is invalid. Try again.", quote=True)

	else:
		update.message.reply_text("❌ I did not understand you. Try again.", reply_markup=mk_button_1, quote=True)

# ===============================================================
def error(update, context):
	print(f"Update {update} ==> {context.error}")


# ===============================================================
def main():
	# FILM API : https://moviesapi.ir/
	# Bot = @file_yab_proj_bot
	API_Key = "5649478905:AAHuQd2099P3sEt-4OiwcLGX7leaetORytU"
	updater = Updater(API_Key, use_context=True)
	d = updater.dispatcher

	d.add_handler(CommandHandler("start", start))
	d.add_handler(CommandHandler("help", help_m))
	d.add_handler(CommandHandler("show_favorite_list", favorite_list))
	d.add_handler(CommandHandler("search_film", search_film))
	d.add_handler(CommandHandler("send_favorite", send_favorite_list))

	d.add_handler(MessageHandler(Filters.text, messages))
	d.add_error_handler(error)

	updater.start_polling(0.5)
	print("Bot started...")
	updater.idle()


# ===============================================================
if __name__=="__main__":
	main()
