# assignment
Notable Health non-web take home assignment

## How to run
Download the assignment.py file and data.txt file onto your computer. Cd into the folder in which the files were downloaded. Run the command:
python3 assgnment.py
This will output the formatted text onto the terminal

## Discription
assignment.py contains code which reads in the text data from data.py and formats it according to the specifications of the problem

## Notes
A lot of assumptions were made in regards to error handling and edge cases for this project, some of which are listed below
1. There is no functionality to end a list
2. A new list cannot be started after the first one
3. If list starts from number n, an empty numbered list uptill n is not added
4. List can only be started from numbers 1-9
5. A list item cannot be empty
  5a. No support for cases like "number one number next abcd"
  5b. An empty item cannot be at the end eg. "... number next"
6. If number next is stated before started a list i.e. saying number 1-9, it will not start a new list
