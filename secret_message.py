from os import listdir

def rename_files():
	#(1) get file names from a folder
	file_list = listdir(r"/home/alanmalbos/version-control/secret-message/prank_2")
	print file_list
	#(2) for each file, rename the name without numbers


rename_files()