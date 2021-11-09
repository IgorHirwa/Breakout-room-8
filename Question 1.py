#this is the improved ALU hangman That allows uses functions to execute every task and

# I have started off by storing the answers in a dictionary of itself

#this is a dictionary that  holds the questions and their correct answers
# ex: C is the value associated to the key "When was ALU founded ?" among the multiple choices

questions = {
 "When was ALU founded ?": "C",
 "Who is the CEO of ALU ? ": "A",
 "Where are ALU campuses ? ": "D",
 "How many campuses does ALU have ? ": "A",
"What is the name of ALU Rwandas Dean ?": "C",
"Who is in charge of Student Life ?": "D",
"What is the name of our Lab ?": "C",
"How many students do we have in Year 2 CS ?": "D",
"How many degrees does ALU offer ?": "B",
"Where are the headquarters of ALU ?": "C"
}

# for the multiple choices , i have made a list of lists. the big list 'options' holds small lists
#that will be displayed as possible choices of the player. each letter corresponding to a possible answer
options = [["A.2000" , "B.2005" , "C.2015" , "D.2020"] ,
           ["A:Fred swaniker" , "B:H.E Jacob Zuma" , "C:H.E Paul kagame" , "D:H.E Paul Magufuli"],
           ["A.Rwanda" , "B.Mauritius" , "C.Kenya" , "D.Option A and B"] ,
           ["A.2" , "B.4" , "C.6" ,"D.8"] ,
           ["A.Fred Swaniker" ,"B.Mrs Mimi Mutoni" , "C.Dr Gaidi Faraj" , "D.Sila Ogidi"] ,
           ["A.Fred Swaniker" , "B.Mrs Mimi Mutoni" , "C.Dr Gaidi Faraj" , "D.Sila Ogidi"] ,
           ["A.ALU LAB" , "B.LETS LAB" , "C.FABLAB" , "D.LAB1"] ,
           ["A.81" , "B.52" , "C.100" , "D.137"] ,
           ["A.2" , "B.8" , "C.6" , "D.4"],
           ["A.Rwanda" , "B.Benin" , "C.Mauritius" , "D.Option A and C"]
           ]


# chech_answer is the function that will check if the input are correct or not
def check_answer(answer, guess): # new parameters answers and guess will hold for me the arguments "questions.get(key)"and "guess"

    if answer == guess:  # uses if statement to check the "answer" parameter is equal to the ""guess
        print("CORRECT!")   # the computer outputs "wrong"
        return 1
    else:
        print("WRONG!")     # if the answer paramenter is not equal to the guess, it then outputs 'wrong'
        return 0

# this is the function to putput the score after the all the answers are recieved.
#it has as arduments the correct_guesses (as the correct answers) and guesses list containing answers from the  users
def print_score(correct_guesses, guesses):
    print("-------------------------------------")
    print("THE RESULTS ARE AS FOLLOWS: ")
    print("-------------------------------------")

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ") # this line will for every i in the now full list of answers, display one by one with a space btn
    print()

    score = int((correct_guesses/len(questions))*100)           # calculate the percentage
    losses=10-correct_guesses                                   # make another variable losses to hold the number of losses
    print("you have got",correct_guesses,"correct answers")     # prints the  number of correct guesses
    print("and",losses,"incorrect answers")                     # prints the number of incorrect answers
    print("Your score is: "+str(score)+"%")                     # and finally a score in percentage


# this is the function that will be the main body of the code.
def new_game():

    guesses = []              # this is an empty list for now that will hold the answers being input by the user
    correct_guesses = 0
    question_num = 1          # this is the current question number whick will represent the question we are on.

    for key in questions:     # this is addressing every key(in my case question) from the dictionary.
        print("-------------------------")
        print(key)            # here the program prints the very key this loop is currently on(the question we are at)
        for i in options[question_num-1]: # to get the first index to be zero we have to subtract 1 from the initial value 1
            print(i)
        guess = input("Enter (A, B, C, or D): ")  # the strings input may not be accepted because the input function is case sensitive
        guess = guess.upper()                     # hence making it upper case to deal with the same format
        guesses.append(guess)                     # the uppercase guess entered by the player is added to the initially empty list and as the loop goes on,
        # the list will grow.

        correct_guesses += check_answer(questions.get(key), guess) # here we call the check_answer function and pass "questions.get(key),
        # and  guess into the function check_answer
        question_num += 1 # here is where we increment the question_num count to move to the next iteration

    print_score(correct_guesses, guesses) # here we are also calling print_score and passing correct_guesses, guesses as it's arguments

# Here i called the new game function
new_game()

#if no it prints a goodbye message
print("Thank you for Playing, Have a nice day!")