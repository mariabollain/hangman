import random

words = ["python", "java", "swift", "javascript"]
print("H A N G M A N")

i = 0
wins = 0
losses = 0

while True:
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if choice == "exit":
        break
    elif choice == "results":
        print(f"You won: {wins} times.")
        print(f"You lost: {losses} times.")
    elif choice == "play":
        word = random.choice(words)
        hidden_word = "-" * len(word)
        word_list = list(word)
        hidden_word_list = list(hidden_word)
        used_letters = []

        while i < 8:
            print(hidden_word)
            letter = input("Input a letter: ")

            if len(letter) != 1:
                print("Please, input a single letter.")
            elif not (letter.isalpha() and letter.islower()):
                print("Please, enter a lowercase letter from the English alphabet.")
            elif letter in used_letters:
                print("You've already guessed this letter.")
            else:
                if letter in word:
                    for ind in range(len(word)):
                        if word_list[ind] == letter:
                            hidden_word_list[ind] = letter
                            hidden_word = "".join(hidden_word_list)
                else:
                    print("That letter doesn't appear in the word.")
                    i += 1
            used_letters.append(letter)
            print()
            if hidden_word == word:
                break

        if hidden_word == word:
            print(f"You guessed the word {hidden_word}!\nYou survived!")
            wins += 1
        else:
            print("You lost!")
            losses += 1
    else:
        choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')