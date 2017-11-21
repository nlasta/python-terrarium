class Monk(object):
	"""
	A class that a Character can be.
	The Monk class can equip fists and other light equipment, but excels when it is unarmed.

	Attributes:
		element - An integer representing the element of the Monk, if any. Default is 1 (non-elemental).
			1: non-elemental
			2: fire
			3: ice
			4: lightning
		abilities - A list of strings that display the abilities available to the Monk. Default is "Punch".
	"""

	def __init__(self, element, abilities):
		""" Initializes a Monk object with default element and abilities."""
		self.element = 1
		self.abilities = ["Punch"]
		
		# DEBUGGING - print out Monk object's abilities; should just be Punch at this time. #
		print(abilities)