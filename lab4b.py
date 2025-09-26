#!/usr/bin/env python3
# Author: Arib Noor
# Date: Sept 26 2025
# Purpose: Practice adding and removing elements in list.
# Usage: ./lab3b.py

# TO DO 1: Create variables mylist1, mylist2, and mylist.
mylist1 = [1,3,5]
mylist2 = [2,4,6]
mylist = mylist1 + mylist2
# TO DO 2: Append 7 in mylist.
mylist.append(7)
# TO DO 3: Insert 0 in mylist.
mylist.insert(0,0)
# TO DO 4: Pop element from index 2.
mylist.pop(2)
# TO DO 5: Print variable mylist.
print(mylist)
# TO DO 6: Find the index of the element 6.
print(mylist.index(6))