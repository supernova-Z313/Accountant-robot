def answers(text, data):
	payam_list = text.split()
	if payam_list[0]=="besaz:":
		data[payam_list[1]] = {"history_of_T": []}
		return f"💼roydad {payam_list[1]} ba movafagiyat sakhte shod.✅"

	if payam_list[0]=="afzodan:":
		for i in range(2, len(payam_list)):
			data[payam_list[1]][payam_list[i]] = 0
		return f"💼be roydad {payam_list[1]} aza ezafe shod.✅"

	if payam_list[0]=="anjambde:":
		# 0:anjambde - 1:esmroydad - 2:esmtrakonesh - 3:mablagh - 4_n:esmafrad - n-1:kharidar
		if len(data[payam_list[1]])<2:
			return "❌lotfa ebteda chand oze be in roydad ezafe konid.❌"
		else:
			data[payam_list[1]]["history_of_T"].append(payam_list[2])
			for i in range(4, len(payam_list)-1):
				data[payam_list[1]][payam_list[i]] -= int(int(payam_list[3])/(len(payam_list)-5))
			data[payam_list[1]][payam_list[len(payam_list)-1]] += int(payam_list[3])
			return f"💼be roydad {payam_list[1]} trakonesh {payam_list[2]} ezafe shod.✅"

	if payam_list[0]=="tasviyekon:":
		if len(data[payam_list[1]])<2:
			return "❌lotfa ebteda chand oze be in roydad ezafe konid.❌"
		else:
			data[payam_list[1]][payam_list[2]] += int(payam_list[4])
			data[payam_list[1]][payam_list[3]] -= int(payam_list[4])
			return "💼tasviye hessab ba movafagiyat anjam shod.✅"

	if payam_list[0]=="vaziat:":
		natige = "📈📈📈📈📈📈📈📈📈📈📈\n"
		for i in data[payam_list[1]]:
			if i != "history_of_T":
				natige += f"{i} = {data[payam_list[1]][i]}\n"
		return natige

	if payam_list[0]=="ersal:":
		natige = "0hessab ha\n"
		for i in data[payam_list[1]]:
			if i != "history_of_T":
				natige += f"{i} = {data[payam_list[1]][i]}\n"
		return f"{natige}"

	if payam_list[0]=="hazf:":
		data[payam_list[1]].pop(payam_list[2])
		return "👤karbar hazf shod.✅"

	if payam_list[0]=="tarikhche:":
		natige = "Tarikhche tarakonesh ha:🗂\n"
		for i in data[payam_list[1]]["history_of_T"]:
			natige += f"{i}\n"
		return natige

	return "❌ nafahmidam az /help komak begir ❌"
