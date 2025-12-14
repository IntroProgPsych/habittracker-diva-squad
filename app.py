#import all the modules you need, below this line


#write any functions you need, below this line

HABITS = ("sleep_routine", "physical_activity", "healthy_eatting", "mindfulness", "social_connection")

ITEMS = {
    HABITS[0]:{ 'score':0, "questions" : {1,2,3} },
    HABITS[1]:{ 'score':0, "questions" : {1,2,3} },
    HABITS[2]:{ 'score':0, "questions" : {1,2,3} },
    HABITS[3]:{ 'score':0, "questions" : {1,2,3} },
    HABITS[4]:{ 'score':0, "questions" : {1,2,3} },
}

def get_input_scores():
    for habit in ITEMS.keys():
        score = 0
        for q in ITEMS[habit]["questions"]:
            score += int ( input(f'{q}: ') )
        ITEMS[habit]['score']+=score

def validate_input(item: str):
    pass

#use the main() function for your program, define all other functions above main
def main ():
    #use print statements such as this one, to mark important points in the application, to help you with debugging
    print("Starting application...")
    get_input_scores()

#please do not change the lines below, they are needed for your tests to work properly
#write all your code in the current file, and all your tests in the tests.py file
if __name__ == "__main__":
    main()
