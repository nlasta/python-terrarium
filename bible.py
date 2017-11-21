"""
bible.py
Prints out a passage of the Bible (ESV). 
For now, this prints out John 1:1-5.

Copyright (c) 2017 Nico Lasta. All rights reserved.
"""

def bible():
	verses = { # key - reference, val - verse #
		"John 1:1": "In the beginning was the Word, and the Word was with God, and the Word was God.",
		"John 1:2": "He was in the beginning with God.",
		"John 1:3": "All things were made through him, and without him was not any thing made that was made.",
		"John 1:4": "In him was life, and the life was the light of men.",
		"John 1:5": "The light shines in the darkness, and the darkness has not overcome it."
	}

	passage = " ".join(verse for reference, verse in verses.items()) # TODO - look up how str.join() works!!!

	# print out passage (in this case, John 1:1-5)
	print(passage)
