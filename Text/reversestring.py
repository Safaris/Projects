'''
Created on Aug 22, 2013

@author: Zeus
'''
word = input("Enter the word to reverse \n")
word2=""
for c in reversed(word):
    word2+= c
print(word2)