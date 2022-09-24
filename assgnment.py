import numpy
from pathlib import Path


input = Path('data.txt').read_text()
numberList = {
"one": 1, 
"two": 2, 
"three": 3, 
"four": 4, 
"five": 5, 
"six": 6,
"seven": 7,
"eight": 8,
"nine": 9}
# Text parser which takes in doctor's clinical note as input and 
# reformats it to include numbered lists.
# Notes
#1. There is no functionality to end a list
#2. A new list cannot be started after the first one
#3. If list starts from number n, an empty numbered list uptill n is not added
#4. List can only be started from numbers 1-9
#5. A list item cannot be empty
#  5a. No support for cases like "number one number next abcd"
#  5b. An empty item cannot be at the end eg. "... number next"
#6.If number next is stated before started a list i.e. saying number 1-9, it will not start a new list


def TextParser(input):
	outputText = ""
	words = input.split()
	index = 0
	currentNumber = 0
	listStarted = False
	# Iterates through each word in the list
	while index < len(words):
		# If "number" is encountered, checks the next two values to decide if a new item in a numbered list is being added
		if words[index].lower() == "number" and index < len(words) - 2:
			number = words[index + 1].lower()
			if number == "next" and listStarted:
				currentNumber += 1
				firstWord = words[index + 2].capitalize()
				outputText += "\n" + str(currentNumber) + ". " + firstWord + " "
				index += 2
			elif not listStarted and number in numberList:
				currentNumber = numberList[number]
				firstWord = words[index + 2].capitalize()
				outputText += "\n" + str(currentNumber) + ". " + firstWord + " "
				index += 2
				listStarted = True
			# If a new item is not added in the list, treats the word as normal input
			else:
				outputText += words[index] + " "
		else:
			outputText += words[index] + " "
		index += 1

	return outputText

print(TextParser(input))

