# retrieve user input & validate it
def get_input(dict):
	tmp = None
	# keep asking until input is valid
	while (not tmp):
		# get input, strip spaces and convert to uppercase
		tmp = input().upper().strip()
		# if input isn't a valid product code
		if (not tmp in dict.keys()):
			# print error
			print("Please enter a valid product code.")
			# reset input to blank, so user is asked again
			tmp = None
	# return input
	return tmp

# print available options
def print_details(dict):
	# for every item
	for item in dict.keys():
		# display product code, price and description
		print("%s: $%.2f, %s" % (item, dict[item][0], dict[item][1]))

# print chosen option from dictionary and return cost
def print_chosen(dict, item):
	# print product code and description
	print("%s: %s" % (item, dict[item][1]))
	# return cost
	return dict[item][0]

# dictionaries of for items, prices and descriptions
phones_dict = {"BPCM": (29.99, "Compact"),
				"BPSH": (49.99, "Clam Shell"),
				"RPSH": (199.99, "RoboPhone – 5-inch screen and 64 GB memory"),
				"RPLL": (499.99, "RoboPhone – 6-inch screen and 256 GB memory"),
				"YPLS": (549.99, "Y-Phone Standard – 6-inch screen and 64 GB memory"),
				"YPLL": (649.99, "Y-Phone Deluxe – 6-inch screen and 256 GB memory")}

tablets_dict = {"RTMS": (149.99, "RoboTab – 8-inch screen and 64 GB memory"),
				"RTLM": (299.99, "RoboTab – 10-inch screen and 128 GB memory"),
				"YTLM": (499.99, "Y-Tab Standard – 10-inch screen and 128 GB memory"),
				"YTLL": (599.99, "Y-Tab Deluxe – 10-inch screen and 256 GB memory")}

# dictionary for all devices (phones and tablets)
devices_dict = {**phones_dict, **tablets_dict}

# dictionary for SIMs
sims_dict = {"SMNO": (0.00, "SIM Free (no SIM card purchased)"),
				"SMPG": (9.99, "Pay As You Go (SIM card purchased)")}

# dictionary for cases
case_dict = {"CSST": (0.00, "Standard"),
				"CSLX": (50.00, "Luxury")}

# dictionary for chargers
charger_dict = {"CGCR": (19.99, "Car"),
				"CGHM": (15.99, "Home")}

# total cost
total = 0
# total amount of money saved
saving = 0
# ensure user is asked for input until they don't want more devices
run = True
# total number of devices ordered
devices = 0

# run until user doesn't want any more devices
while run:
	# get chosen device
	print("Choose an option:")
	print_details(devices_dict)
	device = get_input(devices_dict)
	# increase number of devices ordered
	devices += 1

	# if phone chosen
	if (device in phones_dict.keys()):
		# get chosen SIM
		print("Choose an option:")
		print_details(sims_dict)
		sim_payg = get_input(sims_dict)

	# get chosen case
	print("Choose an option:")
	print_details(case_dict)
	case = get_input(case_dict)

	# get chosen charger(s)
	print("Which charger(s) would you like? Enter the codes for those you want with a space between them, or enter nothing to choose neither")
	print_details(charger_dict)
	# create array of chosen chargers
	chargers = input().upper().split(" ")
	# remove invalid product codes
	for item in chargers:
		if item not in charger_dict:
			chargers.remove(item)

	# if not first device, apply discount
	if (devices > 1):
		# add cost of device to total
		total += 0.9 * \
			print_chosen(devices_dict, device)
		# record discount applied
		saving += 0.1 * \
			print_chosen(devices_dict, device)
	# if first device, don't apply discount
	else:
		# add cost of device to total
		total += print_chosen(devices_dict, device)
	# if phone chosen, add cost of SIM to total
	if (device in phones_dict):
		total += print_chosen(sims_dict, sim_payg)
	# add cost of chosen case to total
	total += print_chosen(case_dict, case)
	# add cost of chosen chargers to total
	for charger in chargers:
		total += print_chosen(charger_dict, charger)
	# print subtotal
	print("Subtotal: $%.2f" % total)
	# ask if user want another device, and keep running if they do
	run = True if (input("Would you like another device (y/n)?").lower().strip()[0] == "y") else False

# print total cost and saving
print("Total: $%.2f\nSaving: $%.2f" % (total, saving))
