
def process(text: str, user_dict: dict, state: int):
	# =======================================================================
	if state == 2:
		if text not in user_dict and text != "__Home__":
			user_dict[text] = {}
			user_dict["State"] = 0
			return str("Event added successfully. ✅\n"
					 "🌀 Using the following commands, you can switch between events and view the available events:" +
					 "\n🔰 /go_to_event\n🔰 /all_event")
		else:
			return "⛔️ This name cannot be used.\n⭕️ Please enter another name:"

	# =======================================================================

	elif state == 3:
		if text in user_dict and text not in ["temp", "State", "Where", "__Home__"]:
			user_dict["Where"] = text
			user_dict["State"] = -1
			user_dict["temp"] = []
			return f"✅ You have entered event {text}.\n🌀 Please select a command from the menu:"
		else:
			return str("⛔️ The entered name is wrong.\n⭕️ Please enter another name or use the command below to view event names:\n" + 
					 "🔰 /all_event")

	# =======================================================================

	elif state == 5:
		if text == "exit":
			user_dict["State"] = -1
			event_name = user_dict["Where"]
			return f"✅ Back to event {event_name}.\n🌀 Please select a command from the menu:"
		else:
			event_name = user_dict["Where"]
			user_dict[event_name][text] = 0
			return f"✅ Name added seccessfully.\n🌀 Please enter a name or enter the 'exit' to exit:"

	# =======================================================================
	
	elif state == 6:
		user_dict["State"] = 6.1
		return "Please enter the transaction amount:"

	elif state == 6.1:
		user_dict["State"] = 6.2
		user_dict["temp"].append(int(float(text)))
		names = list(user_dict[user_dict["Where"]].keys())
		result = "Enter the names of the participants in this transaction:\n(Write each name on one line.)\n👥 The names of all the people in this event are:\n\n"
		for i in names:
			result += f"{i}\n"
		return result

	elif state == 6.2:
		user_dict["State"] = 6.3
		user_dict["temp"].append(text.split("\n"))
		return "Who paid for this transaction?"

	elif state == 6.3:
		user_dict["State"] = -1
		event_name = user_dict["Where"]
		user_dict[event_name][text] += user_dict["temp"][0]
		share = user_dict["temp"][0]/len(user_dict["temp"][1])
		for i in user_dict["temp"][1]:
			user_dict[event_name][i] -= share
		user_dict["temp"] = []
		return "✅ Transaction added successfully.\n🌀 Please select a command from the menu:"

	# =======================================================================

	elif state == 7:
		user_dict["State"] = 7.1
		user_dict["temp"].append(text)
		return "Who receives the money?"

	elif state == 7.1:
		user_dict["State"] = 7.2
		user_dict["temp"].append(text)
		return "How much is the deposit amount?"

	elif state == 7.2:
		user_dict["State"] = -1
		user_dict[user_dict["Where"]][user_dict["temp"][0]] += int(float(text))
		user_dict[user_dict["Where"]][user_dict["temp"][1]] -= int(float(text))
		user_dict["temp"] = []
		return "✅ Checkout was done successfully.\n🌀 Please select a command from the menu:"

	# =======================================================================

	else:
		return "Error:\n❌   Please enter a valid message."
