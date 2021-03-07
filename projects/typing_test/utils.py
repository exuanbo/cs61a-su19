from math import sqrt
import string

############################################################################################
# Important: Read over the information in the "Appendix: Utility Functions" in the Project #
# Project Specification in order to better understand how to use the functions below.      #
############################################################################################

###############################
# Submitting design questions #
###############################

passphrase = '*** PASSPHRASE HERE ***'

def check_passphrase(p):
    """
    You do not need to understand this code. This will only
    be used to ensure you have entered the correct passphrase.
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()

#################
# Reading files #
#################

def close(file):
	"""Closes the file object passed in. """
	file.close()

def readable(file):
	"""Return True if this file can be read from. """
	return file.readable()

def readline(file):
	"""
	Return the first unread line from this file, 
	or the empty string if all lines are read.
	"""
	return file.readline()

def readlines(file):
	"""
	Return all unread lines in a list.
	"""
	return file.readlines()


############################
# String utility functions #
############################

def lower(s):
	"""Return a copy of string s with all letters converted to lowercase."""
	return s.lower()


def split(s, sep=None):
	"""
	Returns a list of words contained in s, which are
	sequences of characters separated by a string sep.

	By default, this splits on whitespace (spaces, tabs, etc.)
	but by defining a different sep, you can split on arbitrary
	characters.
	"""
	return s.split(sep)

def strip(s, chars=None):
	"""
	Return a version of s with characters in chars removed
	from the start and end.

	By default, removes whitespace characters.
	"""
	return s.strip(chars)


#########################################
# Functions relating to keyboard layout #
#########################################

KEY_LAYOUT = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
			  ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
			  ["z", "x", "c", "v", "b", "n", "m"]]

def distance(p1, p2):
	"""Return the Euclidean distance between two points

	The Euclidean distance between two points, (x1, y1) and (x2, y2)
	is the square root of (x1 - x2) ** 2 + (y1 - y2) ** 2

	>>> distance((0, 1), (1, 1))
	1
	>>> distance((1, 1), (1, 1))
	0
	>>> round(distance((4, 0), (0, 4)), 3)
	5.657
	"""
	return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def get_key_distances():
	"""Return a new dictionary mapping key pairs to distances.

	Each key of the dictionary is a tuple of two
	letters as strings, and each value is the euclidean distance
	between the two letters on a standard QWERTY keyboard normalized
	such that the greatest distance is 2.0

	The scaling is constant, so a pair of keys that are twice
	as far have a distance value that is twice as great

	>>> distances = get_key_distances()
	>>> distances["a", "a"]
	0.0
	>>> distances["a", "d"] # 2.0 / 9
	2.0
	>>> distances["d", "a"]
	2.0
	"""
	key_distance = {}

	def compute_pairwise_distances(i, j, d):
		for x in range(len(KEY_LAYOUT)):
			for y in range(len(KEY_LAYOUT[x])):
				l1 = KEY_LAYOUT[i][j]
				l2 = KEY_LAYOUT[x][y]
				d[l1, l2] = distance((i, j), (x, y))

	for i in range(len(KEY_LAYOUT)):
		for j in range(len(KEY_LAYOUT[i])):
			compute_pairwise_distances(i, j, key_distance)

	max_value = max(key_distance.values())
	return {key : value * 2 / max_value for key, value in key_distance.items()}

