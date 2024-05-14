# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion

# Any code taken from other sources is referenced within my code solution

# Student ID:20220944
#westminster ID:w2052104
# Date:12.10.2023

#(https://mcsp.wartburg.edu/zelle/python/)    ***refernces for graphics.python
#(https://www.w3schools.com/python/gloss_python_while.asp) *** while loops
#(https://www.w3schools.com/python/python_tuples.asp) *** tuples
#(https://www.w3schools.com/python/python_dictionaries.asp)**dictionary
#(https://www.w3schools.com/python/python_functions.asp)**function

from graphics import *

result_outcome = {
    "progress": 0,
    "trailer": 0,
    "retriever": 0,
    "exclude": 0
}

progression_data = {'progress': [], 'trailer': [], 'retriever': [], 'exclude': []}

def get_credit_input(credit_type):
    valid_credits = [0, 20, 40, 60, 80, 100, 120]
    while True:
        credit_input = input(f"Please enter the {credit_type.upper()} credits: ")
        if not credit_input.isdigit():
            print(f"Error: Integer required for {credit_type.upper()} credits.")
            continue
        credits = int(credit_input)
        if credits not in valid_credits:
            print(f"Error: {credit_type.upper()} credits out of range.")
            continue
        return credits

def get_inputs():
    pass_credits = get_credit_input("pass")
    defer_credits = get_credit_input("defer")
    fail_credits = get_credit_input("fail")

    total_credits = pass_credits + defer_credits + fail_credits
    if total_credits != 120:
        print("Error: Total credits do not sum up to 120")
        return get_inputs()

    return pass_credits, defer_credits, fail_credits



def predict_outcome(pass_credits, fail_credits):
    if pass_credits == 120:
        return 'progress'
    elif pass_credits == 100:
        return 'trailer'
    elif fail_credits >= 80:
        return 'exclude'
    else:
        return 'retriever'

#https://www.youtube.com/watch?v=R39vTAj1u_8&list=PLmzkEJ1Zz_uZ5nvTOLaGHfinCzEVEVBlz&index=1 basics of the grpahics.py

def histogram(result_outcome):
    window = GraphWin("Histogram", 700, 500)
    window.setBackground(color_rgb(237, 242, 236))

    progress = result_outcome["progress"]
    trailer = result_outcome["trailer"]
    retriever = result_outcome["retriever"]
    excluded = result_outcome["exclude"]
    
#https://www.youtube.com/watch?v=nYhxBVDW7sM&list=PLmzkEJ1Zz_uZ5nvTOLaGHfinCzEVEVBlz&index=2 shapes and primitive shapes
    totalOutcomes = progress + trailer + retriever + excluded
    # Set bar width to 110 units to leave space for labels
    bar1 = Rectangle(Point(110, 350), Point(220, 350 - 15 * progress))
    bar2 = Rectangle(Point(230, 350), Point(340, 350 - 15 * trailer))
    bar3 = Rectangle(Point(360, 350), Point(470, 350 - 15 * retriever))
    bar4 = Rectangle(Point(490, 350), Point(600, 350 - 15 * excluded))


    bar1.draw(window)
    bar1.setFill(color_rgb(174, 248, 161))
    bar2.draw(window)
    bar2.setFill(color_rgb(160, 198, 137))
    bar3.draw(window)
    bar3.setFill(color_rgb(167, 188, 119))
    bar4.draw(window)
    bar4.setFill(color_rgb(210, 182, 181))
#https: // www.youtube.com / watch?v = IpiVXHcSBSw & list = PLmzkEJ1Zz_uZ5nvTOLaGHfinCzEVEVBlz & index = 3 text lines etc
    tex1 = Text(Point(163, 370), "Progress")
    tex2 = Text(Point(288, 370), "Trailer")
    tex3 = Text(Point(415, 370), "Retriever")
    tex4 = Text(Point(545, 370), "Excluded")

    line1 = Line(Point(80, 350), Point(640, 350))
    line1.draw(window)



    titleText = Text(Point(220, 40), "Credits Histogram")
    # Calculating total outcomes for labeling histogram
    outcomeText = Text(Point(220, 420), str(totalOutcomes) + " outcome(s) in total.")

    progText1 = Text(Point(163, 350 - 50 * progress), str(progress))
    progText2 = Text(Point(288, 350 - 50 * trailer), str(trailer))
    progText3 = Text(Point(415, 350 - 50 * retriever), str(retriever))
    progText4 = Text(Point(545, 350 - 50 * excluded), str(excluded))

    tex1.draw(window)
    tex1.setFill((color_rgb(123, 134, 149)))
    tex1.setStyle("bold")

    tex2.draw(window)
    tex2.setFill((color_rgb(123, 134, 149)))
    tex2.setStyle("bold")

    tex3.draw(window)
    tex3.setFill((color_rgb(123, 134, 149)))
    tex3.setStyle("bold")

    tex4.draw(window)
    tex4.setFill((color_rgb(123, 134, 149)))
    tex4.setStyle("bold")

    titleText.draw(window)
    titleText.setFill(color_rgb(100, 100, 100))
    titleText.setSize(17)
    titleText.setStyle("bold")

    outcomeText.draw(window)
    outcomeText.setSize(15)
    outcomeText.setFill((color_rgb(123, 134, 149)))
    outcomeText.setStyle("bold")

    if progress >= 1:
        progText1.draw(window)
    if trailer >= 1:
        progText2.draw(window)
    if retriever >= 1:
        progText3.draw(window)
    if excluded >= 1:
        progText4.draw(window)

    window.getMouse()
    window.close()

# Writing outcomes to txt file
def write_to_file(progression_data):
    with open('outcome_credits.txt', 'w') as file:
        for outcome, credits in progression_data.items():
            for pass_creds, defer_creds, fail_creds in credits:
                file.write(f'{outcome}: pass {pass_creds}, defer {defer_creds}, fail {fail_creds}\n')

def print_outcomes_and_credits():
    with open('outcome_credits.txt', 'r') as file:
        print(file.read())

user_role = ""
while user_role not in ['staff', 'student']:
    user_role = input("Are you a staff member or a student? Enter 'staff' or 'student': ").lower()
    if user_role not in ['staff', 'student']:
        print("Error: Invalid role entered. Please enter 'staff' or 'student'.")

while True:
    pass_creds, defer_creds, fail_creds = get_inputs()
    outcome = predict_outcome(pass_creds, fail_creds)
    result_outcome[outcome] += 1

    print(f"The outcome for these credits is: {outcome}")

    progression_data[outcome].append((pass_creds, defer_creds, fail_creds))

    if user_role == 'student':
        break  # Students can only enter data once

    if input("Would you like to enter another set of data? Enter 'y' for yes or 'q' to quit and view histogram : ").lower() == 'q':
        break

if user_role == 'staff':
    histogram(result_outcome)  # Only staff members can access the graph option

write_to_file(progression_data)
print_outcomes_and_credits()
