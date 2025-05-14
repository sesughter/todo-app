# python guessing game
import random

word_bank = ["word", "play", "sing", "cry"]
random_Word = random.choice(word_bank)
user_char_list = []
print(random_Word)
count = 0

while count < len(random_Word) + 2:
    user_char = input("enter a character")
    print("-" * len(random_Word))

    if user_char in random_Word:
        for char in user_char:
            if user_char == char:
                print(char, "is in word, good guess")
                user_char_list.append(char)
            else:
                print("not in word, try again")
    else:
        print("not in word")
        count = count + 1
        continue

    user_string = "".join(user_char_list)
    print(user_string)
