import random                                                        #import random library
def print_colored_text(text, color_name):                            #create a new function called "print_colored_text" with paraments (text, color_name)
    colors = {                                                       #creat a dictionary called colors
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',                                          #Reset to default
    }
    color_code = colors.get(color_name.lower(), '\033[37m')          #create variable "color_code" that gets ansi code from color dictionary using color_name and defalts to white
    print(f"{color_code}{text}\033[0m") 

name = input("What is your name? ")                                  #asks user "what is your name?" and assigns answer to name variable
print(f"Hello {name}")                                               #print "hello 'name'" the goal is to type the color of the text and not the text written                                              
colors = ['black', 'red', 'green', 'magenta', 'cyan', 'white']       #creates list called colors
correct, rounds = 0,0                                                #creates variable 'rounds' and "correct' and sets both o 0

while True:                                                          #forver loop
    text_color = random.choice(colors)                               #creates variable "text_color" and picks random from colors list
    print_color = random.choice(colors)                              #creates variable "print_color" and picks random from colors list
    print_colored_text(text_color,print_color)                       #runs print_colored_text with (text_color, print_color)

    user_color = input ("Quick, enter color of the text: ")          #prompts user with "quick, enter color of the text" and assigns answer to user_color variable
    
    if user_color == print_color:                                    #if user_color is print_color
        print("You got it.")                                         #say, "you got it."
        correct += 1                                                 #add 1 to correct round
    else:                                                            #if not
        print("incorrect")                                           #print wrong
    
    rounds += 1                                                      #adds 1 to round
    play_again = input(f"{name} you got {correct} out of {rounds}. Play again? ")  #tells user "'name' you got 'correct' out of 'round' play again? and assigns to play_again"
    
    if play_again == "no":                                           #if play_again is no,
        print("Bye!")                                                #print bye
        break                                                        #break forever loop