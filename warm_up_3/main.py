import respons as R
from telegram.ext import *

# start
def S(update, context):
	update.message.reply_text("Salam\nbe robot hesabdar khosh amadid.💐\nbaray daryaft komak dastor /help ro ejra konid.🆘")

# help
def H(update, context):
	update.message.reply_text("🆘as dastorat zir be tartib estefade kon ta nahve karkard bot ro befahmi:\n🔹/start\n🔹/help\n🔹/Event🔹\n🔹/AM\n🔹/AT\n🔹/TH\n🔹/SS\n🔹/CK\n")

# afzodan roydad
def Event(update, context):
	update.message.reply_text("🎯baray sakht yek roydad yek payam be shekl zir ersal konid:📝\n\nbesaz: (esm roydad)")

# add member
def AM(update, context):
	update.message.reply_text("🎯baray afzodan ozve be yek roydad payame be shekl zir ersal konid:📝\n\nafzodan: (nam roydad) (nam ozve) (nam ozve) ...")

# afzodan trakonesh
def AT(update, context):
	update.message.reply_text("🎯baray afzodan tarakonesh yak payam be shekl zir ersal konid:📝\n\nanjambde: (nam roydad) (nam tarakonesh) (mablagh trakonesh) (nam afrad mosharekat konande) (nam kharidar)")

# tasviye hesab
def TH(update, context):
	update.message.reply_text("🎯baray tasviye hesab yek payam be shekl zir ejra konid:📝\n\ntasviyekon: (nam roydad) (nam pardakht konande) (nam daryaft konande) (mablagh)")

# namayesh vaziat hesab ha
def SS(update, context):
	update.message.reply_text("🎯baray namayesh hessab ha yek payam be shekl zir ersal konid:📝\n\nvaziat: (nam roydad)")

# chap khoroji
def CK(update, context):
	update.message.reply_text("🎯baray ersal vaziat ha yek payam be shekl zir ersal konid:📝\n\nersal: (nam roydad)")

# emtiyazi: hazf fard
def RM(update, context):
	update.message.reply_text("🎯baray hazf yek ozve az roydad yek payam be shekl zir ersal konid:📝\n\nhazf: (nam roydad) (nam ozve)")

# emtiyazi: tarikhche trakonesh
def HT(update, context):
	update.message.reply_text("🎯baray namayesh tarikhche trakonesh yek payam be shekl zir ersal konid:📝\n\ntarikhche: (nam roydad)")

# modiriyat payam ha
def messages(update, context):
	text=str(update.message.text)
	data=context.user_data
	a = R.answers(text, data)
	if a[0]=="0":
		a=a[1:]
		f = open("data.txt", "w")
		f.truncate(0)
		f.write(a)
		f.close()
		chat_id = update.message.chat_id
		context.bot.send_document(chat_id, open("data.txt", "r"))
	else:
		update.message.reply_text(a)

def main():
	TELEGRAM_BOT_TOKEN = "5708690460:AAG7uUAWYQBhwx-eEM1iVttZDKrBnKRjsLY"
	u = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
	d = u.dispatcher

	d.add_handler(CommandHandler("start", S))
	d.add_handler(CommandHandler("help", H))
	d.add_handler(CommandHandler("Event", Event))
	d.add_handler(CommandHandler("AM", AM))
	d.add_handler(CommandHandler("AT", AT))
	d.add_handler(CommandHandler("TH", TH))
	d.add_handler(CommandHandler("SS", SS))
	d.add_handler(CommandHandler("CK", CK))
	d.add_handler(CommandHandler("RM", RM))
	d.add_handler(CommandHandler("HT", HT))
	d.add_handler(MessageHandler(Filters.text, messages))


	u.start_polling(0.5)
	print("test")
	u.idle()


if __name__=="__main__":
	main()
