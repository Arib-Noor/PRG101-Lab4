#!/usr/bin/env python3
# Author: Arib Noor
# Date: Sept 26 2025
# Purpose: Practice slicing on lists.
# Usage: ./lab3d.py
"""
Fill in the required feilds in the comment section.
Create a list variable and call it words.
Write a while loop, in which you ask the user to enter a word or press Q to quit. Save the word in the list words or break the loop when user enters Q or q.
Print number of elements in the list words using len() function.
Create a new list and call it someWords.
Assign the elements present at index 0 till 3 to the list someWords from words. Do this only if the number of elements in words is more than 3.
Print if the list words and the list someWords are equal?
Print the list words.
Print the list someWords
"""
# TO DO 1: Create variable words.
words = []
# TO DO 2: Write a while loop.
while True:
    word = input("Enter a word, or enter q to quit")
    if word == "q":
        break
    words.append(word)
    # TO DO 3: Print number of elements in the list.
    print(len(words))
    # TO DO 4: Create variable someWords.
    someWords = []
    # TO DO 6: Update someWords.
    for w in words:
        if len(words) > 3:
            someWords = words[0:3]
    print(words == someWords)
    # TO DO 7: Print variable Words.
    print(words)
    # TO DO 8: Print variable someWords.
    print(someWords)
