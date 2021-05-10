import random



# add the user guess to guesses list, if already chosen ask user to pick again

def get_user_guess(guess_list):
    user_guess = None
    while user_guess == None:

        user_guess = input("Please enter your next guess: ").lower()

        if user_guess in guess_list:
            print(f"You already chose {user_guess}")
            user_guess= None
        elif len(user_guess) >1:
            print("Please choose a single letter")
            user_guess = None
        elif user_guess.isdigit():
            print("please choose a letter not a number")
            user_guess = None
        else:
            return user_guess

# show which letters are correct

def get_response(guess_list, randomly_selected_word):
    response = ""
    for letter in randomly_selected_word:
        if letter in guess_list:
            
            response = response + letter
           
        else:
            response = response + "*"
    
    
    return response


     
def play_the_game(words):
    random_word_index = int(random.random()*len(words))
    randomly_selected_word = words[random_word_index]
    guess_list = []
    lives = 7
    first_response = get_response(guess_list, randomly_selected_word)
    print(first_response)
    while True:
        guess = get_user_guess(guess_list)
        guess_list.append(guess)
        response = get_response(guess_list, randomly_selected_word)
        print(response)
        if guess not in randomly_selected_word:
            lives = lives - 1
            print(f"Lives left = {lives}")
        if lives <=0:
            print("you lose")
            return
        if response == randomly_selected_word:
            print("congratulations you win")
            return


        
if __name__ == "__main__":


    word_file = open("word_list.txt", "r")
    word_contents = word_file.readlines()
    word_list = []

    for word in word_contents:
        new_word =word.replace("\n", '')
        
        word_list.append(new_word)


    # words =["cat", "chicken", "apple", "clock"]
    play_the_game(word_list)
    
