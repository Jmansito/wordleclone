import random


# Read the words.txt file and return a random word
def get_word():
    with open("words.txt", "r") as file:
        data = file.read()
        words = data.split()

    word_pos = random.randint(0, len(words) - 1)
    return words[word_pos]


def check_correct(guess, wordle):
    if guess == wordle:
        return True
    else:
        return False


# Check if the guess is 5 letters long
def check_five(guess):
    if len(guess) == 5:
        return True
    else:
        print("Word is not 5 letters long")
        return False


# Check if the guess is in the list of 5-letter words
def check_in_list(guess):
    file = open("words.txt")
    if guess in file.read():
        return True
    else:
        print("Not a word")
        return False


# Check for common letters
def check_common(guess, wordle):
    print("Your common letters are: ", ''.join(set(guess).intersection(wordle)))


# Check for matching positions
def check_position(guess, wordle):
    correct = ""
    for letter in range(wordle.__len__()):
        if guess[letter] == wordle[letter]:
            correct += wordle[letter]
    print("Letters in correct position: ", str(correct))


# Main driver
def main():
    win = False
    num_guesses = 0
    guess = ""
    board = ["- - - - -", "- - - - -", "- - - - -", "- - - - -", "- - - - -", "- - - - -"]
    # Call function to get the wordle
    wordle = get_word()
    # Test print to show answer
    print("The wordle is: ", wordle)

    while not win and num_guesses < 6:
        if num_guesses > 0:
            check_common(guess, wordle)
            check_position(guess, wordle)

        for num in range(6):
            print(board[num])

        guess = input("What is your guess?\n")

        check_five(guess)
        check_in_list(guess)

        if check_five and check_in_list:
            if check_correct(guess, wordle):
                print("You win!")
                win = True
            else:
                board[num_guesses] = guess
                num_guesses += 1
        else:
            break


if __name__ == "__main__":
    main()
