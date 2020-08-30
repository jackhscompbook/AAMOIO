
# THIS IS AAMIO, FORMERLY KNOWN AS PROSINT (ONLY BY MYSELF LOL). 
# SINCE PROSINT'S CODE LOOKS LIKE IT WAS WRITTEN BY A 3 YEAR OLD METH ADDICT, 
# I'VE DECIDED TO REWRITE IT.

import sys
import os
import json

from AMUU import *

class aamio():

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

		# Create the new collection
		os.mkdir(name)


	def promt(self):

		while True:
			os.chdir(self.home)

			command = input(f'AAMIO:{self.currentCollection}:{self.currentChunk}-$').split(' ')
			command[0] = command[0].lower()

			if command[0] == 'help':
				print('''				
-|----------------------[AAMOIO HELP MANUAL]----------------------------------------------------------------------------------------------|-
 |						         |                                                                                                        |
 |-----------------------[GENERAL COMMANDS]-----------------------------------------------------------------------------------------------|
 |                               |																										  |
 |	help                         |  Displays this menu.																					  |
 |  exit                         |  Exits the program.                																	  |
 | 					             |	 																									  |
 |----------------------[COLLECTION COMMANDS]---------------------------------------------------------------------------------------------|
 |                               |																										  |
 |  addCol [NAME]                |  Makes a collection called [NAME] (Alt. aCo). No spaces are allowed.									  |
 |  removeCol [NAME]             |  Deletes a collection called name, if it exists (Alt. rmCo).											  |
 |  lstcols                      |  Lists all collections (Alt. collections).															  |
 |  copyCol [SOURCE] [DEST]      |  Copies [SOURCE] to [DEST] (Alt. cpCo)																  |
 |  collection                   |  Prints the current collection, if it exists. If not, it prints None.                                  |
 |  changeCollection [NEW]       |  Changes from the current collection to [NEW]. If [NEW] doesn't exist, returns error (Alt. cCo)		  |
 |                               |																										  |
 |------------------------[CHUNK COMMANDS]------------------------------------------------------------------------------------------------|
 |                               |																										  |
 |  addChunk [NAME]              |  Makes a chunk called [NAME] (Alt. aCh).																  |
 |  removeChunk [NAME] 	         |  Removes the chunk called [NAME]	(Alt. rmCh)															  |
 |  lstChunks                    |  Lists all chunks in the current collection (Alt. chunks).											  |
 |  copyChunk [SOURCE] [DEST]    |  Copies [SOURCE] to [DEST] (Alt. cpCh)                                                                 |
 |  chunk                        |  Prints the current working chunk.																	  |
 | 	changeChunk [NEW]            |  Changes from the current chunk to [NEW]. If [NEW] doesn't exist, returns error (Alt. cCh)             |
 |	                             |																										  |
 |----------------------[ATTRIBUTE COMMANDS]----------------------------------------------------------------------------------------------|
 |                               |																										  |
 |  addAttribute [NAME] <INFO>   |  Adds an attribute to the current chunk. No spaces are allowed in [NAME].                              |
 |  editAttribute [NAME] [INFO]  |  Changes the value of an attribute (Alt. eA).														  |
 |  removeAttribute [NAME]       |  Removes an attriute from the current chunk (Alt. rmA).												  |
 |  lstAttributes                |  Lists all the attributes (and their values) in the current chunk (Alt. attributes)                    |
 |                               |																										  |	
-|----------------------------------------------------------------------------------------------------------------------------------------|-
				''')

			elif command[0] == 'exit':
				print('Exiting...')
				break

			elif command[0] == 'cls':
				clear()

			elif command[0] == 'aCo' or command[0] == 'addCol':
				print(f'Creating collection {command[1]}.')				
				self.addCol(command[1])




