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


def retrieve_information():
    import json
    with open("covid_info.json") as open_file:
        info = json.load(open_file)
    return info


def ask_possible_exposure():
    travel = get_valid_input(["n", "y"], input_question="Have you traveled internationally in the last 14 days, y/n")
    widespread = get_valid_input(["n", "y"], input_question="Is the virus wide spread in your area, y/n #idk")
    exposure = get_valid_input(["n", "y"], input_question="Have you been exposed to anyone who had the virus y/n")
    work_medical_facility = get_valid_input(["y", "n"], input_question="Have you worked or volunteered at a medical facility in the last 14 days, y/n")
    all_answers = [travel, widespread, exposure, work_medical_facility]
    exposures = []
    for y_n in all_answers:
        if y_n == "y":
            exposures.append(True)
        else:
            exposures.append(False)
    return exposures


def ask_following_from_list(my_list):
    i = 0
    response_list = []
    while i < len(my_list):
        print(my_list[i])
        response = get_valid_input(["n", "y"], input_question="Answer y/n")
        if response == "y":
            response_list.append(True)
        else:
            response_list.append(False)
        i += 1
    return response_list


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


def check_emergency_symptoms(retrieved_info):
    info = retrieved_info
    print("Do you have any of the following symptoms, y/n?")
    for emergency_symptom in info[4]["emergency_symptoms"]:
        print(emergency_symptom)
    e_symptom_respond = get_valid_input(["y", "n"])
    if e_symptom_respond == "y":
        print("CONTACT THE AUTHORITIES IMMEDIATELY")
    else:
        return True


def ask_all_questions(retrieved_info):
    info = retrieved_info
    print("\n", "Are you")
    age_range_value = choose_following_from_list(info[0]["age_range"])
    print("\n")
    exposures = ask_possible_exposure()
    print("\n", "Please respond whether you have")
    complication_values = ask_following_from_list(info[1]["complications"])
    print("\n", "Please respond if you have experienced")
    symptoms_values = ask_following_from_list(info[3]["symptoms"])
    return age_range_value, exposures, complication_values, symptoms_values


def evaluate_answer_amounts(exp, comp, y_n, symp):
    complication_amount = 0
    y_n_amount = 0
    symptom_amount = 0
    if exp == 3:
        complication_amount += 1
    for complication in comp:
        if complication == True:
            complication_amount += 1
    print(complication_amount)
    for y_n_question in y_n:
        if y_n_question == True:
            y_n_amount += 1
    print(y_n_amount)
    for symptom in symp:
        if symptom == True:
            symptom_amount += 1
    print(symptom_amount)
    return complication_amount, y_n_amount, symptom_amount


def evaluate_answers(comp_a, y_n_a, symp_a):
    if comp_a and y_n_a and symp_a == 0:
        print("You have have no complications, no exposure, and no symptoms.")
        print("There is no need to take a test at this point.")
        print("If in the near future you do not feel well, please revisit this feature.")
    if comp_a == 0 and y_n_a == 0 and symp_a > 0:
        print("You have no complications and no exposure, but you have", symp_a, "symptom(s)")
        if symp_a < 3:
            print("The chances of you having the virus is low, but if you feel doubtful take a test")
        else:
            print("You are likely to have the virus, you should take the test, and you may even recover at home if positive")
    if comp_a == 0 and y_n_a  > 0 and symp_a == 0:
        print("You have no complications and no symptoms, but possible exposure")
        print("The chances of you having the virus is very low")
        print("If you start to develop more than one symptom at any point, take a test and if positive you may even recover at home")
    if comp_a == 0 and y_n_a > 0 and symp_a > 0:
        print("You have possible exposure and", symp_a, "symptom(s)")
        print("You are likely to have the virus, you should take the test, and you may even recover at home if positive")
    if comp_a > 0 and y_n_a == 0 and symp_a == 0:
        print("You have no exposure or symptoms, and most probably do not have the virus")
        if comp_a == 1:
            print("Nevertheless, you have a health complication and you should be very careful ")
        else:
            print("Nevertheless, you have several health complication and must be EXTRA careful")
            print("SELF ISOLATE")
    if comp_a > 0 and y_n_a > 0 and symp_a == 0:
        print("You do not have any symptoms, but you have possible exposure and complication(s), you are encouraged to take a test")
        print("You should contact a doctor or the authorities if positive")
    if comp_a > 0 and y_n_a < 0 and symp_a > 0:
        print("You have complication(s) and", symp_a, "symptoms")
        print("You should take a test and contact a doctor or the authorities if positive")
    if comp_a > 0 and y_n_a > 0 and symp_a > 0:
        print("You have complication(s), exposure, and", symp_a, "symptoms")
        print("You should take a test and contact a doctor or the authorities if positive")


def organize_user_info(age, comp, y_n, symp,):
    info = retrieve_information()
    my_list_values = [comp, y_n, symp ]
    keys = ["complications", "exposure", "symptoms"]
    corresponding_lists = [[], [], []]

    if age == "3":
        corresponding_lists[0].append("Old age")
    info_index = 1
    key_index = 0
    my_list_index = 0
    for items in corresponding_lists:
        item_index = 0
        my_list = my_list_values[my_list_index]
        my_key = keys[key_index]
        for item in my_list:
            if item == True:
                items.append(info[info_index][my_key][item_index])
            item_index += 1
        if len(items) == 0:
            items.append("None")
        my_list_index += 1
        key_index += 1
        info_index += 1

    my_info = {
        "complications": corresponding_lists[0],
        "exposures": corresponding_lists[1],
        "symptoms": corresponding_lists[2],
        "evaluation": None,
        "recommendation": None
    }
    return my_info


def save_user_info(information, file_name="file"):
    import datetime
    now = datetime.datetime.now()
    date_time = str(now.strftime("%Y-%m-%d"))
    information["datetime"] = date_time
    my_file_name = ["(", date_time, ")", "-", file_name, ".json"]

    import json
    file = open("".join(my_file_name), "w")
    file.write(json.dumps(information, indent=2))
    file.close()


def main_covid_19_feature():
    info = retrieve_information()
    if check_emergency_symptoms(info):
        age, comp, y_n, symp = ask_all_questions(info)
        comp_a, y_n_a, symp_a = evaluate_answer_amounts(age, comp, y_n, symp)
        evaluate_answers(comp_a, y_n_a, symp_a)
        save_info = get_valid_input(["y", "n"], input_question="Would you like to save your data?")
        if save_info == "y":
            my_info = organize_user_info(age, comp, y_n, symp)
            save_user_info(my_info)






