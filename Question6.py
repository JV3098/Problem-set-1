def pig(word):
    for i in range(len(word)):
        if word[i].lower() in "aeiou":
            return word[i: ] + word[i: ] + "ay"
            
word = input("Enter the word 1: ")
print(f"{word} --> {pig(word)}")
word = input("\nEnter the word 2: ")
print(f"{word} --> {pig(word)}")

    