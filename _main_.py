def retrieve_questions():
    import json
    with open('questions.json') as open_file:
        questions = json.load(open_file)
    return questions


my_questions = retrieve_questions()


def retrieve_answer_values():
    import json
    with open('answer_values.json') as open_file_1:
        answers = json.load(open_file_1)
    return answers


my_answers = retrieve_answer_values()


class Question:
    objects = []
    info = []
    questions = []
    answers = []
    values = []

    def __init__(self, info, question, answer, value):
        self.info = info
        self.question = question
        self.answer = answer
        self.value = value
        Question.objects.append(self)
        Question.info.append(self.info)
        Question.questions.append(self.question)
        Question.answers.append(self.answer)
        Question.values.append(self.value)

    def return_info(self):
        return self.info

    def return_question(self):
        return self.question

    def return_answers(self):
        return self.answer

    def return_value(self):
        return self.value

    @classmethod
    def get_valid_input(cls, answers, input_question=""):
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

    @classmethod
    def choose_following_from_list(cls, my_list):
        i = 0
        j = 1
        number_of_questions = []
        while i < len(my_list):
            print(j, ")", my_list[i])
            number_of_questions.append(str(j))
            i += 1
            j += 1
        response = Question.get_valid_input(number_of_questions)
        return response


class HUI(Question):
    health_index_sum = 1
    percentile_health = 0
    healthcare = 0
    percentile_care = 0

    @classmethod
    def ask_and_calculate_index(cls):

        question_number = 0
        while question_number < len(HUI.objects):
            if HUI.info is not None:
                print(HUI.info[question_number], "\n")
            print(HUI.questions[question_number])
            user_input = Question.choose_following_from_list(Question.answers[question_number])
            print(user_input)
            value = HUI.values[question_number][user_input]
            HUI.health_index_sum = HUI.health_index_sum - float(value)
            question_number += 1

    @classmethod
    def determine_index_percentile(cls):
        health_index_sum = HUI.health_index_sum
        if health_index_sum <= 0.43352:
            print("You are healthier than 1 percent of americans")
            HUI.percentile_health = 1
        if 0.43352 < health_index_sum <= 0.612233:
            print("You are healthier than 5 percent of americans")
            HUI.percentile_health = 5
        if 0.612233 < health_index_sum <= 0.705392:
            print("You are healthier than 10 percent of americans")
            HUI.percentile_health = 10
        if 0.705392 < health_index_sum <= 0.805017:
            print("You are healthier than 50 percent of americans")
            HUI.percentile_health = 50
        if 0.805017 < health_index_sum <= 0.916525:
            print("You are healthier than 75 percent of americans")
            HUI.percentile_health = 75
        if 0.916525 < health_index_sum <= 0.936914:
            print("You are healthier than 90 percent of americans")
            HUI.percentile_health = 90
        if 0.936914 < health_index_sum <= 0.98565:
            print("You are healthier than 95 percent of americans")
            HUI.percentile_health = 95
        if 0.98565 < health_index_sum <= 1:
            print("You are healthier than 99 percent of americans")
            HUI.percentile_health = 99

    @classmethod
    def compare_healthcare(cls):
        percentile_care = 0
        print("\n")
        healthcare_input = input("Please input your annual healthcare spendings($)")
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

    @classmethod
    def compare_percentiles(cls):
        if HUI.percentile_health >= HUI.percentile_care:
            print("\n", "Everything is fine, you healthcare works for you")
        else:
            print("\n", "NOT good, your spendings on healthcare exceed your level of health")


Q1HUI = HUI(my_questions[0]["Additional"], my_questions[0]["Q"], my_questions[0]["An"], my_answers[0])
Q2HUI = HUI(my_questions[1]["Additional"], my_questions[1]["Q"], my_questions[1]["An"], my_answers[1])
Q3HUI = HUI(my_questions[2]["Additional"], my_questions[2]["Q"], my_questions[2]["An"], my_answers[2])
Q4HUI = HUI(my_questions[3]["Additional"], my_questions[3]["Q"], my_questions[3]["An"], my_answers[3])
Q5HUI = HUI(my_questions[4]["Additional"], my_questions[4]["Q"], my_questions[4]["An"], my_answers[4])
Q6HUI = HUI(my_questions[5]["Additional"], my_questions[5]["Q"], my_questions[5]["An"], my_answers[5])
Q7HUI = HUI(my_questions[6]["Additional"], my_questions[6]["Q"], my_questions[6]["An"], my_answers[6])
Q8HUI = HUI(my_questions[7]["Additional"], my_questions[7]["Q"], my_questions[7]["An"], my_answers[7])
Q9HUI = HUI(my_questions[8]["Additional"], my_questions[8]["Q"], my_questions[8]["An"], my_answers[8])
Q10HUI = HUI(my_questions[9]["Additional"], my_questions[9]["Q"], my_questions[9]["An"], my_answers[9])
Q11HUI = HUI(my_questions[10]["Additional"], my_questions[10]["Q"], my_questions[10]["An"], my_answers[10])
Q12HUI = HUI(my_questions[11]["Additional"], my_questions[11]["Q"], my_questions[11]["An"], my_answers[11])


class User:
    users = []

    def __init__(self, name, password, index, index_percentile, healthcare, healthcare_percentile):
        self.name = name
        self.password = password
        self.index = index
        self.index_percentile = index_percentile
        self.healthcare = healthcare
        self.healthcare_percentile = healthcare_percentile
        User.users.append(self)
        print(len(User.users))

    @classmethod
    def user_signup(cls):
        number_of_users = 0
        print("Select one")
        user_input = Question.choose_following_from_list(["New User"])
        if user_input == "1":
            sign_up = Question.get_valid_input(["y", "n"], "Would you like to create an account? y/n")
            if sign_up == "n":
                return None, None
            if sign_up == "y":
                user_name = input("Please insert a username")
                password = input("Please set a password")
                number_of_users += 1
        return user_name, password

    def set_user_info(self):
        self.index = HUI.health_index_sum
        self.healthcare = HUI.healthcare
        self.index_percentile = HUI.percentile_health
        self.healthcare_percentile = HUI.percentile_care

    def return_index(self):
        return self.index

    def return_index_percentile(self):
        return self.index_percentile

    def return_healthcare(self):
        return self.healthcare

    def return_healthcare_percentile(self):
        return self.healthcare_percentile

    def display_user_info(self):
        print(self.name, "- Info")
        print("Index :", self.index)
        print("Percentile for Index :", self.index_percentile)
        print("Percentile for Healthcare Expenses :", self.healthcare_percentile)


def main_HUI_feature():
    print("Welcome to my app")
    my_user_name, my_password = User.user_signup()
    ask_for_HUI = Question.get_valid_input(["y", "n"], input_question="Would you like to know your health utility index   y/n")
    if ask_for_HUI == "y":
        HUI.ask_and_calculate_index()
        print(HUI.health_index_sum)
        HUI.determine_index_percentile()
        HUI.compare_healthcare()
        HUI.compare_percentiles()
        user1 = User(my_user_name, my_password, HUI.health_index_sum, HUI.percentile_health, HUI.healthcare,
                     HUI.percentile_care)
        user1.display_user_info()
    print("Thank you, see you soon!")


main_HUI_feature()
