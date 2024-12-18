import time
import datetime
def print_colored_text(text, color_name):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',                                              # Reset to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m')              # Default to white if color not found
    print(f"{color_code}{text}\033[0m")                                  # Print text with color and reset

print_colored_text ("ALARM", 'red')                                      #the computer displays "alarm" in red text
current_time = datetime.datetime(2024, 10, 23, 6, 30, 0)                 #the current time is 6:30 and the date is 10/23/2024
print(current_time.strftime("%H:%M:%S"))                                 #prints the current time
time.sleep(4)                                                            #pauses code for 4 seconds
print ()                                                                 
while True:                                                              #forever loop
    snooze = str.lower(input("Snooze? y/n: "))                           #asked the user if they want to press snooze or not. It also allows them to use upper and lower case.
    if snooze == "y":                                                    #if they say yes to snooze
        print_colored_text("Sleep for 5 more minutes", 'blue')           #it prints "sleep for 5 more minutes" in blue text
        time.sleep(5)                                                    #pauses code for 5 seconds
        current_time += datetime.timedelta (minutes=5)                   #add 5 minutes to the time
        print(current_time.strftime("%H:%M:%S"))                         #prints the current time
    elif snooze == "n":                                                  #if they say no to snooze
        print_colored_text("Get up", 'red')                              #print "get up" in red text
        time.sleep(1)                                                    #pauses code for 1 second
        current_time += datetime.timedelta (minutes=1)                   #adds 1 minute to the time
        print_colored_text("Brush hair", 'green')                        #prints the current time
        time.sleep(1)                                                    #pauses code for 1 second
        current_time += datetime.timedelta (minutes=1)                   #adds 1 minute to the time
        print_colored_text("Brush my teeth", 'magenta')                  #prints "brush my teeth" in magenta text
        time.sleep(1)                                                    #pauses code for 1 second
        current_time += datetime.timedelta (minutes=3)                   #adds 3 minutes to the time
        break                                                            #stops forever loop
    else:                                                                #anything other than y or n
        print("Invalid response")                                        #print "invalid response"
print(current_time.strftime("%H:%M:%S"))                                 #prints current time

while True:                                                              #forever loop
    weather = str.lower(input("Is it cold? y/n: "))                      #asks the user "is it cold?"
    if weather == "y":                                                   #if the weather is cold
        print_colored_text("Wear a sweater", 'blue')                     #print "wear a sweater" in blue
        time.sleep(1)                                                    #pauses code for 1 second
        current_time += datetime.timedelta (minutes=2)                   #adds 2 minutes to the time
        print(current_time.strftime("%H:%M:%S"))                         #prints current time
        break                                                            #stops forever loop
    elif weather == "n":                                                 #if the weather is hot
        print_colored_text("wear a shirt", 'magenta')                    #print "wear a shirt" in magenta
        time.sleep(1)                                                    #pauses code for 1 second
        current_time += datetime.timedelta (minutes=2)                   #adds 2 mins to time
        print(current_time.strftime("%H:%M:%S"))                         #prints current time
        break                                                            #stops forever loop
    else:                                                                #anything other than y or n
        print("Invalid response")                                        #print "invalid response"
        print(current_time.strftime("%H:%M:%S"))                         #prints current time

while True:                                                              #forever loop
    makeup = str.lower(input("Put on makeup?"))                          #asks the user "put on makeup?"
    current_time += datetime.timedelta (minutes=5)                       #adds 5 mins to time
    if makeup == "y":                                                    #if they say yes to makeup
        print_colored_text("go to desk and put on makeup", 'green')      #print "go to desk and put on makeup" in green text
        time.sleep(1)                                                    #go to desk and put on makeup
        current_time += datetime.timedelta (minutes=5)                   #adds 5 mins to time
        print(current_time.strftime("%H:%M:%S"))                         #prints current time
        break                                                            #stops forever loop
    elif makeup == "n":                                                  #if they say no to makeup
        print_colored_text("go downstairs", 'green')                     #print "go downstairs" in green
        time.sleep(1)                                                    #go to desk and put on makeup
        current_time += datetime.timedelta (minutes=1)                   #adds 1 min to time
        print(current_time.strftime("%H:%M:%S"))                         #prints current time
        break                                                            #stops forever loop
    else:                                                                #anything other than y or n
        print("Invalid response")                                        #print "invalid response"
        print(current_time.strftime("%H:%M:%S"))                         #prints current time

while True:                                                              #forever loop
    breakfast = str.lower(input("Do we have waffles?"))                  #ask the user "do we have waffles?"
    if breakfast == "y":                                                 #if the user says yes
        print_colored_text("eat waffles", 'cyan')                        #print "eat waffles" in cyan
        time.sleep(1)                                                    #pauses code for 1 second
        current_time += datetime.timedelta (minutes=10)                  #adds 10 minutes to the time
        print(current_time.strftime("%H:%M:%S"))                         #prints current time
        break                                                            #stops forever loop
    elif breakfast == "n":                                               #if the user says no
        print_colored_text("eat cereal", 'green')                        #print "eat cereal" in green
        time.sleep(1)                                                    #pauses code for 1 second
        current_time += datetime.timedelta (minutes=10)                  #add 10 minutes to the time
        print(current_time.strftime("%H:%M:%S"))                         #prints current time
        break                                                            #stops forever loop
    else:                                                                #anything other than y or n
        print("Invalid response")                                        #print "invalid response"
        print(current_time.strftime("%H:%M:%S"))                         #prints current time

while True:                                                              #forever loop
    volleyball = str.lower(input("Volleyball? y/n: "))                   #asks the user "volleyball?"
    if volleyball == "y":                                                #if they say yes
        print_colored_text("grab volleyball bag", 'red')                 #print "grab volleyball bag" in red
        time.sleep(1)                                                    #pauses code for 1 second
        print_colored_text("pack up school bag", 'cyan')                 #print "pack up school bag" in cyan
        time.sleep(1)                                                    #pauses code for 1 seocnd
        print_colored_text("go to school", 'red')                        #print "go to school" in red
        current_time += datetime.timedelta (minutes=5)                   #adds 5 minutes to the time
        print(current_time.strftime("%H:%M:%S"))                         #prints current tim
        break                                                            #stops forever loop
    elif volleyball == "n":                                              #if they say n to volleyball
        print_colored_text("pack up school bag", 'white')                #print "pack up school bag" in white
        time.sleep(1)                                                    #pauses code for 1 second
        print_colored_text("go to school", 'blue')                       #print " go to school" in blue
        current_time += datetime.timedelta (minutes=5)                   #adds 5 mins to time
        print(current_time.strftime("%H:%M:%S"))                         #prints current tim
        break                                                            #stops forever loop
    else:                                                                #anything other than y or n
        print("Invalid response")                                        #print "invalid response"
        print(current_time.strftime("%H:%M:%S"))                         #prints current time