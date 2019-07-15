import datetime


# def update_time():
today    = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

today_str	 = ("start_date = " + str(yesterday)       + " 00:00:00\n")
tomorrow_str = ("end_date = "   + str(today)    + " 00:00:00\n")

new_cfg_file_text = ""
with open("config/config.cfg") as cfg_file:
	for line in cfg_file.readlines():
		if line.startswith("start_date"):
			new_cfg_file_text += today_str
		elif line.startswith("end_date"):
			new_cfg_file_text += tomorrow_str
		else:
			new_cfg_file_text += line
with open("config/config.cfg", 'w') as cfg_file:
	cfg_file.write(new_cfg_file_text)	

# start_date = '2019-07-04 00:00:00'
# end_date = '2019-07-05 00:00:00'
