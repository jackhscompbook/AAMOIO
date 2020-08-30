import sys
import os
import json

class AAMOIO():

	def __init__(self, rootDir):
		# define an init function which defines all the variables we need.

		self.root = rootDir
		self.chunks = []
		self.currentCollection = None
		self.currentChunk = None
		self.history = True
		self.help = '''
-|----------------------[AAMOIO HELP MANUAL]----------------------------------------------------------------------------------------------|-
 |						         |                                                                                                        |
 |-----------------------[GENERAL COMMANDS]-----------------------------------------------------------------------------------------------|
 |                               |																										  |
 |	help                         |  Displays this menu.																					  |
 |  exit                         |  Exits the program.                																	  |
 | 					             |	 																									  |
 |----------------------[COLLECTION COMMANDS]---------------------------------------------------------------------------------------------|
 |                               |																										  |
 |  addCol [NAME]                |  Makes a collection called [NAME] (Alt. aCo).														  |
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


		'''

	def cls(self):
		# Yes I wrote a function to save four characters of typing. sue me.

		os.system('cls')

	def handleJson(self, file, mode, file=None):
		# I also made a nice function in order to handle json data cause I need to do that.

		# check if there's no file specified.
		if file == None:
			return 'No file returned'

		# check for the mode passed in. r for read, w for write. I use with statements to open and close the files.
		if mode == 'r':
			with open(file, 'r') as f:
				return json.load(file)
		elif mode == 'w':
			with open(file, 'w') as f:
				json.dump(data, file)

	def returnCoList(self):

		return [i.name for i in os.scandir(self.root) if i.is_dir()]

	def returnChList(self):

		return [i.name for i in os.scandir(f'{self.root}\\{self.currentCollection}') if i.name[-6:] == '.chunk']

	def help(self):
		# Do I really need a comment for this one lol.

		print(self.help)

	def addCollection(self, name):
		# This function creates a new collection in the root directory specified by the user.

		# We change the working directory of the program to the root directory specified.
		os.chdir(self.root)

		print(f'Making collection {name}...')

		# Try to create a new directory with the name specified. Also, set the current collection to the name of the new collection.
		try:
			os.mkdir(f'.\\{name}\\')
			self.currentCollection = name
			print(f'\tCollection was created with name {name}.')

		# If the file exists already, it raises a FileExistsError, which we catch here.
		except FileExistsError:

			print(f'\t{name} is already a collection.')

			# This for loop was prolly not the best way to iterate through numbers until it works, but I'm too lazy to rewrite lol.
			# This for loop iterates from up to 100000, appending the number to the name specified until the file is allowed to be created.
			for i in range(100000)
				try:
					os.mkdir(f'.\\{name}_{i}\\')
				except FileExistsError:
					continue
				self.currentCollection = f'{name}_{i}'
				print(f'\tCollection was created with name {name}_{i}.')

		# Change into the collection. 
		os.chdir(f'.\\{self.currentCollection}')

	def removeCollection(self, name):
		# This one removes a collection.

		# Change to the root directory
		os.chdir(self.root)

		# Check if the user wants to remove the collection and if the collection exists.
		# This code runs the delete command on the file (Windows only)
		# If you want to use this on linux I assume you're technical enough to change it for yourself.
		if name in self.returnCoList():
			if input(f'Are you sure you want to remove {name} forever [Y/N]?').lower() != 'y':
				return 0
			os.system(f'rd /S /Q .\\{name}\\')
		else:
			print(f'Collection {name} does not exist')

	def listCollections(self):
		# This function lists the collections.

		os.chdir(self.root)

		print('Collections:')
		for i in self.returnCoList():
			print(f'\t{i}')

	def copyCollection(self, source, dest):

		os.chdir(self.root)
		try:
			os.system(f'xcopy /E {source} .\\{dest}\\')
		except FileExistsError:
			print(f'{source} does not exist.')

	def currentCollection(self):

		print(self.currentCollection)

	def changeCollection(self, new):

		if new in self.returnCoList():
			self.currentCollection = new
			os.chdir(f'..\\{new}')

	def addChunk(self, name):

		os.chdir(f'{self.root}\\{self.currentCollection}')

		print('Making chunk...')

		if os.path.isfile(f'.\\{name}.chunk'):

			i = 1
			
			while os.path.isfile(f'{name}_{i}.chunk'):
				i += 1 

			with open(f'{name}_{i}.chunk', 'w+') as f:
					f.write('{}')
				self.currentChunk = f'{name}_{i}.chunk'
				print(f'Chunk made with name {name}_{i}.chunk')

		else:

			with open(f'{name}.chunk', 'w+') as f:
					f.write('{}')
				self.currentChunk = f'{name}.chunk'
				print(f'Chunk made with name {name}.chunk')

	def removeChunk(self, name):

		os.chdir(f'{self.root}\\{self.currentCollection}')

		if name in self.returnChList():			
			if input(f'Are you sure you want to remove {name} forever [Y/N]?').lower() != 'y':
				return 0
			os.system(f'del /F /Q {name}.chunk')
		else:
			print(f'{name} does not exist as a chunk.')

	def listChunks(self, collection):

		print(f'Chunks in collection {collection}:')
		for i in self.returnChList():
			print(f'\t{i}')

	def copyChunk(self, source, dest):

		if dest in self.returnChList():
			if input(f'{dest} already exists, do you want to overwrite it [y/n]?\n').lower() != 'y':
				return 0
		os.system(f'xcopy {source} {dest} /Y')

	def makeAttribute(self, chunk, name):

		self.returnChList()
		if chunk not in self.chunkList:
			print('invalid chunk')
		pass

	def editAttribute(self, chunk, attribute='all'):

		pass

	def readArrtibutes(self, chunk, attribute='all'):

		pass

	def terminal(self):

		while True:
			
			if not self.history:
				self.cls()

			command = input('-AAMOIO-$').lower()

			if command == 'exit':
				print('Exiting...')
				break

			elif command.startswith('cl'):
				self.cls()

			elif command == 'help':
				print(self.help)

			elif command == 'history':
				self.history = not self.history



	def startUp(self):

		self.cls()
		print( 
'''
     ___           ___      .___  ___.   ______    __    ______   
    /   \\         /   \\     |   \\/   |  /  __  \\  |  |  /  __  \\  
   /  ^  \\       /  ^  \\    |  \\  /  | |  |  |  | |  | |  |  |  | 
  /  /_\\  \\     /  /_\\  \\   |  |\\/|  | |  |  |  | |  | |  |  |  | 
 /  _____  \\   /  _____  \\  |  |  |  | |  `--'  | |  | |  `--'  | 
/__/     \\__\\ /__/     \\__\\ |__|  |__|  \\______/  |__|  \\______/ 
A_personlol's Amazing       Magical     OSINT     Info  Organizer

'''
			)


