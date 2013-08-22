'''
Created on Aug 22, 2013

@author: Zeus
'''

word=input("Enter word to check for palindrome \n")
word2=""
for c in reversed(word):
    word2+=c 
if word2==word:
    print(word + " is a palindrome \n")
else:
    print(word + " is not a palindrome \n")