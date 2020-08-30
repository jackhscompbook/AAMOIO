
# This is a collection of functions that I like to use.
# A_personlol's Mostly Useless Utilities (AMUU)
# By a_personlol#2828

import os
import json

# I like having a simple way to clear the console.
def clear():
	os.system('cls')

# I also like having functions for handeling JSON data.
def handleJson(self, mode, file):

	# Check if the file exists:
	if os.path.exists(file):
		print(f'File: {file} does not exist.')
		return 0

	# check for the mode passed in. r for read, w for write.
	if mode == 'r':
		with open(file, 'r') as f:
			return json.load(file)
	elif mode == 'w':
		with open(file, 'w') as f:
			json.dump(data, file)
			return 'File written.'
	else:
		print(f'Mode: {mode} does not exist.')


