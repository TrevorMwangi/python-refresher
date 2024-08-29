import string

def is_pangram(sentence):
    sentence = sentence.lower()
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in sentence:
            return False
        return True
    
sentence = input("Enter your sentence here: ")
print(is_pangram(sentence))
        