word1 = input("Enter a word: ")
word2 = input("Enter a second word: ")

if len(word1) >= 3 and len(word2) >= 3:
    if word1[-3:].lower() == word2[-3:].lower():
        print("Those are rhyming words")
    elif word1[-2:].lower() == word2[-2:].lower():
        print("Those are almost rhyming words")
    else:
        print("Those are not rhyming words")
else:
    print("Words must have at least three characters to rhyme")