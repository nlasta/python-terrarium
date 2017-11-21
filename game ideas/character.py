class Character(object):
	"""
	This is your character. It is your basic character; nothing fancy.

	Attributes:
		name - Your character's name.
	"""

	def __init__(self, name=""):
		""" Initializes a Character with a name. If name is empty (default), ask for the name."""
		self.name = name
		if (name == ""):
			name = input('Hello there, traveler! What is your name?')
		else:
			name = name

		# TODO - move this to whatever the Main script will be. #
		""" Greet the user and introduces the Hub."""
		print("Nice to meet you, " + name + "! Welcome to the Hub!")
		print("The Hub is a place where travelers, such as yourself, can find shelter and comfort. ")

