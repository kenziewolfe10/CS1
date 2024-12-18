import time
import random
possible_computer_actions = ["yes","no","maybe","undecided"]           #possible action to the users question
question_words = ["am", "will", "is", "do", "have", "can", "what"]     #list of words that the user can have as thier first word in thier question

while True:
    question = input("Ask a question: ")                               #tells user to ask a question
    first_word = question.split(" ")[0]                                #this splits the user input every space
    time.sleep(2)                                                      #pauses the code for 2 seconds
                                                   
    if "?" in question and first_word in question_words:               #if there is a question mark and the first word is in the list
        print(random.choice(possible_computer_actions))                #print an answer to the question
    else:                                                              #if they dont use a question mark or the frist word
        print("Please ask a question")                                 #print "please ask a question"
