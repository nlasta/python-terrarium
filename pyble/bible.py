"""
bible.py
Prints out a passage of the Bible (ESV). 
For now, this prints out John 1:1-5.

Copyright (c) 2017 Nico Lasta. All rights reserved.
"""

# dependencies: nt.py, ot.py #
import nt

def bible():
	""" Prints out a passage that the user will pass in via input. For now, it will print out John 1:1-5."""

	# create a dictionary. from SW - "the key is the name of the book and the value is a dictionary of the verses"
	verses = { # key - reference, val - verse. eventually: key - book, val - dict(verses) #
		"John 1:1": "In the beginning was the Word, and the Word was with God, and the Word was God.",
		"John 1:2": "He was in the beginning with God.",
		"John 1:3": "All things were made through him, and without him was not any thing made that was made.",
		"John 1:4": "In him was life, and the life was the light of men.",
		"John 1:5": "The light shines in the darkness, and the darkness has not overcome it."
	}

	passage = " ".join(verse for book, verse in verses.items()) # str.join() = separator.join(str elements)

	# print out passage (in this case, John 1:1-5) #
	print(passage)
	print("d[verses] length:" len(verses)) # TODO remove

