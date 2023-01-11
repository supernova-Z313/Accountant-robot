def responses(text, state, user_data, **args):
	if state == 2:
		if text not in user_data:
			user_data[text] = {}
			user_data["last_command"] = 0
			user_data["events"].append(text)
			return "The desired event was created."
		else:
			return "There is an event with this name. Please enter another name:"

	# ----------------------------------------------------------------------------
	elif state == 3:
		if text in user_data:
			user_data["last_command"] = 0
			user_data["Head"] = text
			return "You have successfully entered the event."
		else:
			return "The entered name is not correct. Please try again:"

	# ----------------------------------------------------------------------------
	elif state == 4:
		print(user_data[user_data["Head"]])
		if text == "exit":
			user_data["last_command"] = 3
			head = user_data["Head"]
			return f"Back to event {head}"
		elif text in user_data[user_data["Head"]]:
			return "This name already exists.\nPlease enter another name or type \"exit\" to exit:"
		else:
			user_data[user_data["Head"]][text] = 0
			return "User added seccessfully. \nPlease enter another name or type \"exit\" to exit:"

	# ----------------------------------------------------------------------------
	elif state == 5:
		if text == "exit":
			user_data["last_command"] = 3
			head = user_data["Head"]
			return f"Back to event {head}"
		else:
			user_data["last_command"] = 5.1
			return "Please enter the transaction amount:"


	# ----------------------------------------------------------------------------
	elif state == 5.1:
		if text == "exit":
			user_data["last_command"] = 3
			head = user_data["Head"]
			return f"Back to event {head}"
		else:
			user_data["amount"] = float(text)
			user_data["last_command"] = 5.2
			# cheak
			names = list(user_data[user_data["Head"]].keys())
			return f"Please enter the names of the participants in this transaction, separated by a '-'.\nNames of all members:\n{names}"


	# ----------------------------------------------------------------------------
	elif state == 5.2:
		if text == "exit":
			user_data["last_command"] = 3
			head = user_data["Head"]
			return f"Back to event {head}"
		else:
			user_data["last_command"] = 5.3
			user_data["Users"] = text.split("-")
			return "Please enter the name of the buyer of this transaction:"


	# ----------------------------------------------------------------------------
	elif state == 5.3:
		if text == "exit":
			user_data["last_command"] = 3
			head = user_data["Head"]
			return f"Back to event {head}"
		else:
			user_data["last_command"] = 3
			share = user_data["amount"]/len(user_data["Users"])
			user_data[user_data["Head"]][text] += user_data["amount"]
			for i in user_data["Users"]:
				user_data[user_data["Head"]][i] -= share
			user_data["amount"] = 0
			user_data["Users"] = []
			return "The transaction was added successfully."


	# ----------------------------------------------------------------------------
	else:
		return "We could not understand your message."