#Hangman game
import string


def play_hangman():
    word_to_guess = "hello"
    letters_in_the_word = set(word_to_guess)
    alphabets = set(string.ascii_lowercase)
    letters_used_by_the_user = set() #empty set to store letters used by the guesser
    number_of_guesses = 7

    while len(letters_in_the_word) > 0 and number_of_guesses >0 :
        print("Number of guesses left : "," ",number_of_guesses)
        print("Letters you have used : ", " ".join(letters_used_by_the_user))

        #print the word
        word = [letter if letter in letters_used_by_the_user else "-" for letter in word_to_guess ]
        print("The word is " , " " .join(word))

        #take user input for letter
        user_input_letter = input("Enter the letter to guess : " ).lower()
        #check if the letter is in aplhabets and the used letter
        if user_input_letter in alphabets - letters_used_by_the_user :
            letters_used_by_the_user.add(user_input_letter)
            #check if the letter is in the word
            if user_input_letter in letters_in_the_word:
                letters_in_the_word.remove(user_input_letter)
                print("")
            else:
                number_of_guesses = number_of_guesses-1
                print("The letter you used is not in the word.")

        elif user_input_letter in letters_used_by_the_user:
            print("Already used that letter.")
        else:
            print("Invalid letter")

    if number_of_guesses ==0 :
        print("Game over sorry. ", "The word is ","".join(word_to_guess))
    else:
        print("Yay you won!!!")

play_hangman()



