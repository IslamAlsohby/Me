from time import time

def typingErrors (prompt, user_input):

    #split the given prompt and user input into lists of words
    prompt_words = prompt.split()
    user_words = user_input.split()

    #initialize a variable to count errors
    errors = 0

    #compare each pair of x (prompt wor) and y (user word)
    for prompt_word, user_word in zip(prompt_words, user_words):
        if prompt_word != user_word:
            errors += 1


    #claculate the absolute difference in the number of words between prompt and user input        
    errors += abs(len(prompt_words) - len(user_words))
    

    #return the total count of errors
    return errors


def typingSpeed(iprompt, stime, etime):

    #split the given input prompt int a list of words
    words = iprompt.split()


    #calculate the total number of words in the input prompt
    twords = len(words)

    
    #calculate the typing speed in word per minute
    speed = ( twords / ( stime - etime ) ) * 60

    #return the speed
    return speed


def timeElapsed(stime, etime):


    #clculate the elapsed time 
    elapsed_time = stime - etime

    #round the elapsed time to two decimal places
    rounded_elapsed_time = round(elapsed_time, 2)

    #return the rounded elapsed time
    return rounded_elapsed_time


def typingGrades(errors):

    if errors == 0:
        return "Expert typist"
    elif errors <= 5:
        return "Advanced typist"
    elif errors <= 10:
        return "Intermediate Typist"
    else:
        return "Begginer Typist" 


if __name__ == '__main__':
    prompt = "Hi, my name is Aman Kharwal, I am a coding instructor."
    print("Type this:- '", prompt, "'")

    # Listening to input ENTER
    input("Press ENTER when you are ready!")

    # Recording time for input
    stime = time()
    iprompt = input()
    etime = time()

    # Calculate all the information returned from functions
    time_elapsed = timeElapsed(stime, etime)
    speed = typingSpeed(iprompt, stime, etime)
    errors = typingErrors(prompt, iprompt)

    # Displaying typing performance
    print("\nTyping Performance:")
    print("Total Time elapsed: ", time_elapsed, "s")
    print("Your Average Typing Speed: ", speed, "words/minute")
    print("Total Errors: ", errors)
    print("Typist Grade: ", typingGrades(errors))


    # Ask user if they want to retry
    retry = input("Do you want to retry? (yes/no): ").lower()
    if retry == "yes":
        # Retry the typing prompt
        stime = time()
        iprompt = input("Retry: ")
        etime = time()
        errors = typingErrors(prompt, iprompt)
        
        # Displaying performance after retry
        print("\nTyping Performance (Retry):")
        print("Total Time elapsed: ", timeElapsed(stime, etime), "s")
        print("Your Average Typing Speed: ", typingSpeed(iprompt, stime, etime), "words/minute")
        print("Total Errors: ", errors)
        print("Typist Grade: ", typingGrades(errors))
    else:
        print("Thanks for playing!")