
# THIS IS AAMIO, FORMERLY KNOWN AS PROSINT (ONLY BY MYSELF LOL). 
# SINCE PROSINT'S CODE LOOKS LIKE IT WAS WRITTEN BY A 3 YEAR OLD METH ADDICT, 
# I'VE DECIDED TO REWRITE IT.

import sys
import os
import json
import shutil

from AMUU import *

class aamoio():

	def __init__(self, home):

		# This attribute stores the home directory of the program
		self.home = home

		# This attribute stores the current working collection
		self.currentCollection = None

		# This attribute stores the current working chunk
		self.currentChunk = None

	def addCol(self, name):
		
		os.chdir(self.home)

		# Check if the collection exists
		if os.path.exists(name):
			print('This collection already exists.')
			return 0
		else:
			# Create the new collection if it doesn't
			os.mkdir(name)
			return 1

	def removeCol(self, name):
		
		os.chdir(self.home)

		# Check if the collection doesn't exist
		if not os.path.exists(name):
			print('This collection does not exist.')
			return 0
		else:
			# Create the new collection if it does
			shutil.rmtree(name)
			if name == self.currentCollection:
				self.currentCollection == None
			return 1


	def promt(self):

		while True:

			# I make sure we're in the home directory after the user enters a command so that way adding collections and chunks is easier.
			os.chdir(self.home)

			command = input(f'AAMIO:{self.currentCollection}:{self.currentChunk}-$').split(' ')
			command[0] = command[0].lower()

			if command[0] == 'help':
				print('''				
-|----------------------[AAMOIO HELP MANUAL]----------------------------------------------------------------------------------------------|-
 |                               |                                                                                                        |
 |-----------------------[GENERAL COMMANDS]-----------------------------------------------------------------------------------------------|
 |                               |                                                                                                        |
 |  help                         |  Displays this menu.                                                                                   |
 |  exit                         |  Exits the program.                                                                                    |
 |                               |                                                                                                        |
 |----------------------[COLLECTION COMMANDS]---------------------------------------------------------------------------------------------|
 |                               |                                                                                                        |
 |  addCol [NAME]                |  Makes a collection called [NAME] (Alt. aCo). No spaces are allowed.                                   |
 |  removeCol [NAME]             |  Deletes a collection called name, if it exists (Alt. rmCo).                                           |
 |  lstcols                      |  Lists all collections (Alt. lCo).                                                                     |
 |  copyCol [SOURCE] [DEST]      |  Copies [SOURCE] to [DEST] (Alt. cpCo)                                                                 |
 |  collection                   |  Prints the current collection, if it exists. If not, it prints None.                                  |
 |  changeCollection [NEW]       |  Changes from the current collection to [NEW]. If [NEW] doesn't exist, returns error (Alt. cCo)        |
 |                               |                                                                                                        |
 |------------------------[CHUNK COMMANDS]------------------------------------------------------------------------------------------------|
 |                               |                                                                                                        |
 |  addChunk [NAME]              |  Makes a chunk called [NAME] (Alt. aCh).                                                               |
 |  removeChunk [NAME]           |  Removes the chunk called [NAME] (Alt. rmCh)                                                           |
 |  lstChunks                    |  Lists all chunks in the current collection (Alt. chunks).                                             |
 |  copyChunk [SOURCE] [DEST]    |  Copies [SOURCE] to [DEST] (Alt. cpCh)                                                                 |
 |  chunk                        |  Prints the current working chunk.                                                                     |
 |  changeChunk [NEW]            |  Changes from the current chunk to [NEW]. If [NEW] doesn't exist, returns error (Alt. cCh)             |
 |                               |                                                                                                        |
 |----------------------[ATTRIBUTE COMMANDS]----------------------------------------------------------------------------------------------|
 |                               |                                                                                                        |
 |  addAttribute [NAME] <INFO>   |  Adds an attribute to the current chunk. No spaces are allowed in [NAME].                              |
 |  editAttribute [NAME] [INFO]  |  Changes the value of an attribute (Alt. eA).                                                          |
 |  removeAttribute [NAME]       |  Removes an attriute from the current chunk (Alt. rmA).                                                |
 |  lstAttributes                |  Lists all the attributes (and their values) in the current chunk (Alt. attributes)                    |
 |                               |                                                                                                        |	
-|----------------------------------------------------------------------------------------------------------------------------------------|-
				''')

			elif command[0] == 'exit':
				print('')
				print('Exiting...')
				break

			elif command[0] == 'cls':
				clear()
				print('')

			elif command[0] == 'd00d':
				print('')
				print('You fucking aamoio.\nhttps://discordapp.com/channels/572004140587417610/630884961141915678/738089093115936903')

			elif command[0] == 'aco' or command[0] == 'addcol':
				print('')
				print('Attempting to create collection.')
				try:				
					if self.addCol(command[1]):
						print(f'Success! Collection {command[1]} exists now!')
				except IndexError:
					print('No name specified.')

			elif command[0] == 'rmco' or command[0] == 'removecol':
				print('')
				print('Attempting to remove collection.')
				try:
					if self.removeCol(command[1]):
						print(f'Success! Collection {command[1]} is gone!')
				except IndexError:
					print('No name specified.')

			elif command[0] == 'lco' or command[0] == 'lstcols':
				print('')
				print('Collections:\n')
				for i in os.scandir(self.home):
					if os.path.isdir(i.name) and i.name != '__pycache__':
						print(f'\t{i.name}')

			elif command[0] == '' or command[0] == ' ':
				print('')

			else:
				print('')
				print(f'{command[0]} Is an Invalid Command')

			print('')

	def startup(self):
		clear()
		print(
'''
	Welcome to...
	     ___           ___      .___  ___.   ______    __    ______   
	    /   \\         /   \\     |   \\/   |  /  __  \\  |  |  /  __  \\  
	   /  ^  \\       /  ^  \\    |  \\  /  | |  |  |  | |  | |  |  |  | 
	  /  /_\\  \\     /  /_\\  \\   |  |\\/|  | |  |  |  | |  | |  |  |  | 
	 /  _____  \\   /  _____  \\  |  |  |  | |  `--'  | |  | |  `--'  | 
	/__/     \\__\\ /__/     \\__\\ |__|  |__|  \\______/  |__|  \\______/ 

	or...

	A_personlol's Amazing       Magical     OSINT     Info  Organizer
''')
		input('	Press enter to continue...')
		clear()
		self.promt()




if __name__ == '__main__':

	aa = aamoio('.')
	aa.startup()

