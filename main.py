name = input("Please enter your name")

import json
with open('Questions.json') as open_file:
    Questions = json.load(open_file)

import json
with open('Answers.json') as open_file_1:
    Answers = json.load(open_file_1)

sum = 1
question_number = 0
while question_number < 12:
    print(Questions[question_number]["Additional"])
    print(Questions[question_number]["Q"])
    print(Questions[question_number]["An"])
    answer = input("Please insert your answer")
    sum = sum - float(Answers[question_number][answer])
    question_number += 1
print("Your health utility index is" sum)

percentile_health = 0
if sum <= 0.43352:
    print("You are healthier than 1 percent of americans")
    percentile_health = 1
if sum > 0.43352 and sum <= 0.612233:
    print("You are healthier than 5 percent of americans")
    percentile_health = 5
if sum > 0.612233 and sum <= 0.705392:
    print("You are healthier than 10 percent of americans")
    percentile_health = 10
if sum > 0.705392 and sum <= 0.805017:
    print("You are healthier than 50 percent of americans")
    percentile_health = 50
if sum > 0.805017 and sum <= 0.916525:
    print("You are healthier than 75 percent of americans")
    percentile_health = 75
if sum > 0.916525 and sum <= 0.936914:
    print("You are healthier than 90 percent of americans")
    percentile_health = 90
if sum > 0.936914 and sum <= 0.98565:
    print("You are healthier than 95 percent of americans")
    percentile_health = 95
if sum > 0.98565 and sum <= 1:
    print("You are healthier than 99 percent of americans")
    percentile_health = 99

Care = input("Would you like to see how your health is compared to money spent on healthcare, yes or no?")
percentile_care = 0
if Care == "no":
    print("Thank you for using this application")
else:
    healthcare = float(input("Please input your annual healthcare spendings"))
    if healthcare == 0:
        percentile_care = 10
        print("you spend as much as 10 percent of Americans")
    if healthcare <= 219 and sum > 0:
        percentile_care = 25
        print("you spend more than 10 percent of Americans")
    if healthcare <= 1052 and healthcare > 219:
        percentile_care = 50
        print("you spend more than 50 percent of Americans")
    if healthcare <= 3436 and healthcare > 1052:
        percentile_care = 75
        print("you spend more than 50 percent of Americans")
    if healthcare <= 8510 and healthcare > 3436:
        percentile_care = 90
        print("you spend more than 75 percent of Americans")
    if healthcare <= 14602 and healthcare > 8510:
        percentile_care = 90
        print("you spend more than 90 percent of Americans")
    if healthcare <= 40862 and healthcare > 14602:
        percentile_care = 95
        print("you spend more than 95 percent of Americans")
    if healthcare > 40862:
        percentile_care = 99
        print("you spend more than 99 percent of Americans")

    if percentile_health >= percentile_care:
        print("Everything is fine, you healthcare works for you")
    if percentile_health < percentile_care:
        print("NOT good, your spendings on healthcare exceed your level of health")

    savedata = input("would you like to save your data, yes or no?")

    import datetime
    now = datetime.datetime.now()

    saved_data = {
        "name": name,
        "index": sum,
        "percentile for health": percentile_health,
        "percentile for healthcare" : percentile_care,
        "datetime": now.strftime("%Y-%m-%d %H:%M:%S")
    }
    if savedata == "yes":
        print(saved_data)
        file_2 = open(name,"w")
        file_2.write(json.dumps(saved_data))
        file_2.close()

    subscription = input("Do you wish to subscribe, yes or no?")
    if subscription == "no":
        print("Thank you for using this application")
    else:
        print("thank you for subscribing")
        print("You will be asked to enter your informtion in order to have a better understanding of your health quality")
        user_info = {
            "name": name,
            "gender": input("type your gender"),
            "age": int(input("enter your age")),
            #"education_level": ,
            #"social_class": ,
            "height": float(input("enter your height in meters")),
            "weight": float(input("enter your weight in kilograms")),
            "chronic diseases": input("enter your chronic diseases, if you do not have any enter 'none'")
         }
        Name = name,"info"
        Name_1 = str(Name)
        BMI = user_info["weight"]/user_info["height"]**2
        user_info["BMI"] = BMI
        user_info["datetime"] = now.strftime("%Y-%m-%d %H:%M:%S")

        import json
        file_3 = open(Name_1,"w")
        file_3.write(json.dumps(user_info))
        file_3.close()
