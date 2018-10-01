from os import listdir
from os import rename

def rename_files():

	#(1) get file names from a folder
	file_list = listdir(r"/home/alanmalbos/version-control/secret-message/prank_2")
	print file_list

	#(2) for each file, rename the name without numbers
	for file_name in file_list:
		rename(file_name, file_name.translate(None, "0123456789"))

	#(3) check the file names again to verify the change
	file_list = listdir(r"/home/alanmalbos/version-control/secret-message/prank_2")
	print file_list
rename_files()