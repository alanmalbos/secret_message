import os

def rename_files():

	#(1) get file names from a folder
	file_list = os.listdir(r"/home/alanmalbos/version-control/secret-message/prank_2")
	print file_list

	# get a working the actual directory
	save_path = os.getcwd()
	print("Current Working Directory: " + save_path)

	# change a working directory to do the rename
	os.chdir(r"/home/alanmalbos/version-control/secret-message/prank_2")

	#(2) for each file, rename the name without numbers
	for file_name in file_list:
		print("Old name - " + file_name)
		os.rename(file_name, file_name.translate(None, "0123456789"))
		print("New name - " + file_name.translate(None, "0123456789"))

	#(3) check the file names again to verify the change
	file_list = os.listdir(r"/home/alanmalbos/version-control/secret-message/prank_2")
	print file_list

	# turn back the working directory
	os.chdir(save_path)

rename_files()