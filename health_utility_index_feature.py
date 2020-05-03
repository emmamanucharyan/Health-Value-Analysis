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


def retrieve_questions():
    import json
    with open('questions.json') as open_file:
        questions = json.load(open_file)
    return questions


def retrieve_answer_values():
    import json
    with open('answer_values.json') as open_file_1:
        answers = json.load(open_file_1)
    return answers


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


def calculate_health_index():
    questions = retrieve_questions()
    answers = retrieve_answer_values()
    health_index_sum = 1
    question_number = 0
    while question_number < 12:
        print()
        if questions[question_number]["Additional"] is not None:
            print(questions[question_number]["Additional"], "\n")
        print(questions[question_number]["Q"])
        user_answer = choose_following_from_list(questions[question_number]["An"])
        health_index_sum = health_index_sum - float(answers[question_number][user_answer])
        question_number += 1
    print("Your health utility index is", health_index_sum)
    return health_index_sum


def compare_index(index):
    percentile_health = 0
    health_index_sum = index
    if health_index_sum <= 0.43352:
        print("You are healthier than 1 percent of americans")
        percentile_health = 1
    if 0.43352 < health_index_sum <= 0.612233:
        print("You are healthier than 5 percent of americans")
        percentile_health = 5
    if 0.612233 < health_index_sum <= 0.705392:
        print("You are healthier than 10 percent of americans")
        percentile_health = 10
    if 0.705392 < health_index_sum <= 0.805017:
        print("You are healthier than 50 percent of americans")
        percentile_health = 50
    if 0.805017 < health_index_sum <= 0.916525:
        print("You are healthier than 75 percent of americans")
        percentile_health = 75
    if 0.916525 < health_index_sum <= 0.936914:
        print("You are healthier than 90 percent of americans")
        percentile_health = 90
    if 0.936914 < health_index_sum <= 0.98565:
        print("You are healthier than 95 percent of americans")
        percentile_health = 95
    if 0.98565 < health_index_sum <= 1:
        print("You are healthier than 99 percent of americans")
        percentile_health = 99
    return percentile_health


def compare_healthcare():
    percentile_care = 0
    print("\n")
    healthcare_input = input("Please input your annual healthcare spendings")
    while True:
        string_decimal = "." in healthcare_input
        if string_decimal == True:
            decimal_point_index = healthcare_input.find(".")
            input_after_decimal = healthcare_input[decimal_point_index + 1:]
            healthcare_input = healthcare_input[0:decimal_point_index]
        else:
            input_after_decimal = "0"
        if healthcare_input.isnumeric() and input_after_decimal.isnumeric():
            break
        else:
            healthcare_input = input("Invalid answer, please type a number")

    while True:
        if healthcare_input.isnumeric():
            healthcare = int(healthcare_input)

            if healthcare == 0:
                percentile_care = 10
                print("You spend as much as 10 percent of Americans")
            if 219 >= healthcare > 0:
                percentile_care = 25
                print("You spend more than 10 percent of Americans")
            if 1052 >= healthcare > 219:
                percentile_care = 50
                print("You spend more than 50 percent of Americans")
            if 3436 >= healthcare > 1052:
                percentile_care = 75
                print("You spend more than 50 percent of Americans")
            if 8510 >= healthcare > 3436:
                percentile_care = 90
                print("You spend more than 75 percent of Americans")
            if 14602 >= healthcare > 8510:
                percentile_care = 90
                print("You spend more than 90 percent of Americans")
            if 40862 >= healthcare > 14602:
                percentile_care = 95
                print("You spend more than 95 percent of Americans")
            if healthcare > 40862:
                percentile_care = 99
                print("You spend more than 99 percent of Americans")
            break
        else:
            healthcare_input = input("Invalid answer, type a number")
    return percentile_care


def save_data(name, index, p_health, p_care):
    import datetime
    now = datetime.datetime.now()

    saved_data = {
        "name": name,
        "index": index,
        "percentile for health": p_health,
        "percentile for healthcare": p_care,
        "datetime": now.strftime("%Y-%m-%d %H:%M:%S")
    }
    import json
    file_2 = open(name, "w")
    file_2.write(json.dumps(saved_data, indent=2))
    file_2.close()

    return saved_data


def main_health_index_feature():
    name = input("Please insert your name")
    print("Please answer the following questions")
    health_utility_index = calculate_health_index()
    percentile_health = compare_index(health_utility_index)
    percentile_care = compare_healthcare()
    if percentile_health >= percentile_care:
        print("\n", "Everything is fine, you healthcare works for you")
    else:
        print("\n", "NOT good, your spendings on healthcare exceed your level of health")

    save_info = get_valid_input(["y", "n"], input_question="Would you like to save your data, y/n?")
    if save_info == "y":
        save_data(name, health_utility_index, percentile_health, percentile_care)


