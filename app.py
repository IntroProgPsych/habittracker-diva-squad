#import all the modules you need, below this line


#write any functions you need, below this line

HABITS = ("SleepRoutine", "PhysicalActivity", "HealthyEating", "Mindfulness", "SocialConnection")

ITEMS = {
    HABITS[0]:{ 'score':0, "questions" : {"How many days per week do you go to bed at a consistent hour?",2,3} },
    HABITS[1]:{ 'score':0, "questions" : {"How many days per week do you exercise for at least 20 minutes?",2,3} },
    HABITS[2]:{ 'score':0, "questions" : {"How many days per week do you eat at least one healthy meal?",2,3} },
    HABITS[3]:{ 'score':0, "questions" : {"How many days per week do you practice mindfulness?",2,3} },
    HABITS[4]:{ 'score':0, "questions" : {"How many days per week do you spend meaningful time with others?",2,3} },
}

def get_input_scores():
    for habit in ITEMS.keys():
        score = 0
        for q in ITEMS[habit]["questions"]:
            nr = get_valid_input(q)
            score += nr
        ITEMS[habit]['score']+=score

def get_valid_input(question: str):
    while(1):
        item = input(f'{question}: ')
        if item.isdigit():
            item = int(item)
            if 0 > item or item > 7:
                print("Number must be between 0 and 7!")
            else:
                break
        else:
            print("Please enter a number!")
    return item

#use the main() function for your program, define all other functions above main
def main ():
    #use print statements such as this one, to mark important points in the application, to help you with debugging
    print("Starting application...")
    get_input_scores()

#please do not change the lines below, they are needed for your tests to work properly
#write all your code in the current file, and all your tests in the tests.py file
if __name__ == "__main__":
    main()
