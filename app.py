#import all the modules you need, below this line


#write any functions you need, below this line

HABITS = ("SleepRoutine", "PhysicalActivity", "HealthyEating", "Mindfulness", "SocialConnection")

ITEMS = {
    HABITS[0]:{ 'score':0, "questions" : {"do you go to bed at a consistent hour?",
                                          "have you gotten more than 8 hours of sleep?",
                                          "have you felt rested after waking up?"} },
    HABITS[1]:{ 'score':0, "questions" : {"have you engaged in meaningful physical activity for an extended duration?(jogging, swimming, going to the gym, etc.)",
                                          "have you engaged in long relaxing walks?",
                                          "have you participated in group physical activites?(basketaball, voleyball, handball, etc.)"} },
    HABITS[2]:{ 'score':0, "questions" : {"do you eat at least one healthy meal?",
                                          "have you had at least 3 meals?",
                                          "have you drank at least 2 liters of water?"} },
    HABITS[3]:{ 'score':0, "questions" : {"do you practice mindfulness?",
                                          "do you practiced self-reflection?",
                                          "have you engaged in a relaxing activity for your mental-health?"} },
    HABITS[4]:{ 'score':0, "questions" : {"did you have deep and/or emotional conversations with people that you care about and feel close to?",
                                          "have you felt like you belong in your comunity?",
                                          "have you felt like you related to the people around you?"} },
}

def get_input_scores():
    for habit in ITEMS.keys():
        score = 0
        print(f"\n{'-'*5}{habit}{'-'*5}\n")
        for q in ITEMS[habit]["questions"]:
            nr = get_valid_input(q)
            score += nr
        ITEMS[habit]['score']+=score

def get_valid_input(question: str):
    while(1):
        try:
            item = input(f'How many days per week {question}\nanswer: ')
            item = int(item)
            if 0 > item or item > 7:
                print("Number must be between 0 and 7!")
                continue
            break
        except Exception as error:
            print(f"{type(error).__name__}: Please enter a number!")
    return item

def interpret_score(score):
    interpretation = None
    if score >= 12:
        interpretation = "High"
    elif score >= 6:
        interpretation = "Moderate"
    else:
        interpretation = "Low"
    return interpretation

def compute_category_scores():
    print('')
    for habit in HABITS:
        score = ITEMS[habit]['score']
        interpretation = interpret_score(score)
        print(f'{habit}: score -> {score} < {interpretation} adherence >')

#use the main() function for your program, define all other functions above main
def main ():
    #use print statements such as this one, to mark important points in the application, to help you with debugging
    get_input_scores()
    compute_category_scores()

#please do not change the lines below, they are needed for your tests to work properly
#write all your code in the current file, and all your tests in the tests.py file
if __name__ == "__main__":
    main()
