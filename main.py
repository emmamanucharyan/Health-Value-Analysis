from health_utility_index_feature import main_health_index_feature
from Covid_19_feature import main_covid_19_feature
import os


def display_list_dic_value(current_value, step=0):
    if type(current_value) == list:
        for item in current_value:
            display_list_dic_value(item, step+1)
            print("\n", end="")
        print("\n", end="")
    elif type(current_value) == dict:
        for key in current_value:
            print("\n", "\t"*step, key, ": ", end="")
            display_list_dic_value(current_value[key], step+1)
    else:
        print(current_value, end="")


def retrieve_info():
    my_files = []
    arr = os.listdir('/Users/arm/Desktop/Intro to Programming/Health-Value-Analysis-master')
    for file in arr:
        if os.stat(file).st_size < 1000:
                import json
                with open(file) as open_file_0:
                    json_file = json.load(open_file_0)
                my_files.append(json_file)
    return my_files


def get_valid_input(answers, input_question=""):
    print(input_question)
    input_variable = input("Please insert your answer>>>").lower()
    valid_answer = False
    while True:
        answer_values = len(answers)
        i = 0
        while i < answer_values:
            if input_variable == answers[i]:
                valid_answer = True
                break
            else:
                i += 1
        if valid_answer == True:
            break
        print("Invalid answer, please type one of the following")
        for answer in answers:
            print(answer, "\t\t", end="")
        input_variable = input("").lower()
    final_answer = input_variable
    return final_answer


def choose_following_from_list(my_list):
    i = 0
    j = 1
    number_of_questions = []
    while i < len(my_list):
        print(j, ")", my_list[i])
        number_of_questions.append(str(j))
        i += 1
        j += 1
    response = get_valid_input(number_of_questions)
    return response


def main():
    print("Welcome to my app")
    options = [
        "Check your health utility index",
        "Evaluate corona virus symptoms",
        "View previously saved info "
        ]
    while True:
        print("From the following, would you like to")
        feature_option = choose_following_from_list(options)
        if feature_option == "1":
            main_health_index_feature()
        if feature_option == "2":
            main_covid_19_feature()
        if feature_option == "3":
            my_info = retrieve_info()
            display_list_dic_value(my_info)
            if len(my_info) == 0:
                print("You have no saved data")
        continue_app = get_valid_input(["no", "yes"], input_question="Would you like to return to the main menu, yes or no")
        if continue_app == "no":
            break
    print("Thank you for using the app, see you soon.")


main()

