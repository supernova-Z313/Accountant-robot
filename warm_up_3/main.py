import respons as R
from telegram.ext import *

# start
def S(update, context):
	update.message.reply_text("Salam\nbe robot hesabdar khosh amadid.💐\nbaray daryaft komak dastor /help ro ejra konid.🆘")

# help
def H(update, context):
	update.message.reply_text("🆘ma dastorat zir ra darim. az anha estefade kon.\n")

# afzodan roydad
def Event(update, context):
	update.message.reply_text("🎯baray sakht yek roydad yek payam be shekl zir ersal konid:📝\n\nbesaz: (esm roydad)")

# add member
def AM(update, context):
	update.message.reply_text("🎯baray afzodan ozve be yek roydad payame be shekl zir ersal konid:📝\n\nafzodan: (nam roydad) (nam ozve) (nam ozve) ...")

# afzodan trakonesh
def AT(update, context):
	update.message.reply_text("🎯baray afzodan tarakonesh yak payam be shekl zir ersal konid:📝\n\nanjamebde: (nam roydad) (nam tarakonesh) (mablagh trakonesh) (nam afrad mosharekat konande) (nam kharidar)")

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
	d.add_handler(MessageHandler(Filters.text, messages))


	u.start_polling(0.5)
	print("test")
	u.idle()


if __name__=="__main__":
	main()
