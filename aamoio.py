
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

		self.evilNames = ['None']

	def addCol(self, name):
		
		os.chdir(self.home)

		# Check if the collection exists
		if os.path.exists(name):
			print('This collection already exists.')
			return 0
		elif name in self.evilNames:
			print('Forbidden Name.')
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
			# Remove the collection if it does
			shutil.rmtree(name)
			if name == self.currentCollection:
				self.currentCollection == None
			return 1

	def copyCol(self, source, dest):

		os.chdir(self.home)

		if not os.path.exists(source):
			print('Source does not exist.')
		elif os.path.exists(dest):
			print('Dest already exists.')
		else:
			shutil.copytree(os.path.join(self.home, source), os.path.join(self.home, dest) )
			print('Done!')

	def addChunk(self, name):

		if self.currentCollection == None:
			print('Not in a collection.')
			return 0

		os.chdir(self.currentCollection)

		if os.path.exists(os.path.join(f'{name}.chunk')):
			print('This chunk already exists.')	
			return 0
		else:
			handleJson('w+', {}, f'{name}.chunk')
			self.currentChunk = name
			return 1

	def removeChunk(self, name):

		if self.currentCollection == None:
			pass
			



	def promt(self):

		while True:

			# I make sure we're in the home directory after the user enters a command so that way adding collections and chunks is easier.
			os.chdir(self.home)



			command = input(f'AAMOIO:{self.currentCollection}:{self.currentChunk}-$').split(' ')
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
 |  collection                   |  Prints the current collection, if it exists. If not, it prints None. (Alt. pwco)                      |
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
						self.currentCollection = command[1]
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

			elif command[0] == 'cpco' or command[0] == 'copycollection':
				print('')
				print('Attempting to copy collection.')
				try:
					if self.copyCol(command[1], command[2]):
						print(f'Success! Collection {command[1]} copied to {command[2]}.')
				except IndexError:
					print('SOURCE or DEST missing.')

			elif command[0] == 'pwco' or command == 'collection':
				print('')
				print(self.currentCollection)

			elif command[0] == 'cco' or command[0] == 'changeCollection':

				print('')

				try:

					if not os.path.exists(command[1]):
						print('New collection does not exist.')
					elif command[1] == 'None':
						self.currentCollection = None
					else:
						self.currentCollection = command[1]

					print('Done!')
				except IndexError:
					print('No new collection specified.')

			elif command[0] == 'ach' or command[0] == 'addchunk':
				
				print('')
				print('Attempting to create chunk.')
				try:
					if self.addChunk(command[1]):
						print('Done!')
				except IndexError:
					print('No name specified.')

			elif command[0] == '':
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
		input('\tPress enter to continue...')
		clear()
		self.promt()




if __name__ == '__main__':

	aa = aamoio('X:\\Data\\Projects\\OSINT_Profiler\\')
	aa.startup()

