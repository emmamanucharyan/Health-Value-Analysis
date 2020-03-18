name=input("Enter your name")
Questions=[
{   "Additional": "",
      "Q": " In general, would you say your health is:",
      "An": "1)Excellent 2)Very good, 3)Good,4)Fair,5)Poor"},
{   "Additional":"The following questions are about activities you might do during a typical day. Does your health now limit you in these activities? If so, how much?",
      "Q":
         "      Moderate activities, such as moving a table, pushing a vacuum cleaner, bowling, or playing golf",
   "An":"1)Yes, limited a lot, 2)Yes, limited a little 3)No, not limited at all "},

{   "Additional" : "",
      "Q": "Climbing several flights of stairs ",
       "An":"1)Yes, limited a lot,2)Yes, limited a little,3)No, not limited at all"},
{"Additional": "During the past 4 weeks, how much of the time have you had any of the following problems with your work or other regular daily activities as a result of your physical health?",
     "Q": "     Accomplished less than you would like ",
     "An": "1)All of the time,2)Most of the time,3)Some of the time,4)A little of the time,5)None of the time"},
{"Additional": "",
     "Q": "Were limited in the kind of work or other activities",
     "An": "1)All of the time,2)Most of the time,3)Some of the time,4)A little of the time,5)None of the time"},
{"Additional": "During the past 4 weeks, how much of the time have you had any of the following problems with your work or other regular daily activities as a result of any emotional problems (such as feeling depressed or anxious)?",
     "Q": "     Accomplished less than you would like",
     "An": "1)All of the time,2)Most of the time,3)Some of the time,4)A little of the time,5)None of the time "},
{"Additional": "",
     "Q": " Did work or other activities less carefully than usual",
     "An": "1)All of the time,2)Most of the time,3)Some of the time,4)A little of the time,5)None of the time"},
{"Additional": "",
     "Q": "During the past 4 weeks, how much did pain interfere with your normal work (including both work outside the home and housework)?",
     "An": "1)Not at all,2)A little bit,3)Moderately,4)Quite a bit,5)Extremely"},
{"Additional": "These questions are about how you feel and how things have been with you during the past 4 weeks. For each question, please give the one answer that comes closest to the way you have been feeling.",
     "Q": "     How much of the time during the past 4 weeks:Have you felt calm and peaceful?",
     "An": "1)All of the time,2)Most of the time,3)Some of the time,4)A little of the time,5)None of the time" },
{"Additional": "",
     "Q": " How much of the time during the past 4 weeks:Did you have a lot of energy?",
     "An": "1)All of the time,2)Most of the time,3)Some of the time,4)A little of the time,5)None of the time"},
{"Additional": "",
     "Q": "How much of the time during the past 4 weeks:Have you felt downhearted and depressed?",
     "An": "1)All of the time,2)Most of the time,3)Some of the time,4)A little of the time,5)None of the time"},
{"Additional": "",
     "Q": "During the past 4 weeks, how much of the time has your physical health or emotional problems interfered with your social activities (like visiting friends, relatives, etc.)?",
     "An": "1)All of the time, 2)Most of the time, 3)Some of the time, 4)A little of the time, 5)None of the time"},


]
Answers=[ {
  "1": float(0),
  "2": float(0.01),
  "3": float(0.03),
  "4": float(0.05),
  "5": float(0.07)
} ,
{
  "1" : float(0.1),
  "2" : float(0.05),
  "3" : float(0),

},
{
  "1" : float(0.1),
  "2" : float(0.05),
  "3" : float(0),

},
{
  "1" : float(0.14),
  "2" : float(0.03),
  "3" : float(0.16),
  "4" : float(0.05),
  "5" : float(0.09)
},
{
  "1" : float(0.14),
  "2" : float(0.03),
  "3" : float(0.16),
  "4" : float(0.05),
  "5" : float(0.09)
},
{
  "1" : float(0.14),
  "2" : float(0.03),
  "3" : float(0.16),
  "4" : float(0.05),
  "5" : float(0.09)
},
{
  "1" : float(0.14),
  "2" : float(0.03),
  "3" : float(0.16),
  "4" : float(0.05),
  "5" : float(0.09)
},
{
  "1" : float(0.14),
  "2" : float(0.03),
  "3" : float(0.16),
  "4" : float(0.05),
  "5" : float(0.09)
},
{
  "1" : float(0.14),
  "2" : float(0.03),
  "3" : float(0.16),
  "4" : float(0.05),
  "5" : float(0.09)
},
{
  "1" : float(0.14),
  "2" : float(0.03),
  "3" : float(0.16),
  "4" : float(0.05),
  "5" : float(0.09)
},
{
  "1" : float(0.14),
  "2" : float(0.03),
  "3" : float(0.16),
  "4" : float(0.05),
  "5" : float(0.09)
},
{
  "1" : float(0.14),
  "2" : float(0.03),
  "3" : float(0.16),
  "4" : float(0.05),
  "5" : float(0.09)
},

]
sum=1
i=0
while i<3:
 print(Questions[i]["Additional"])
 print(Questions[i]["Q"])
 print(Questions[i]["An"])
 answer=input("Please insert your answer")
 sum=sum-float(Answers[i][answer])
 i += 1
print(sum)
percentile_health=0
if sum<0:
  print("Your condition is worse then death")

if sum >=0 and sum < 0.1:
  print("You are healthier than 1 percent of americans")
  percentile_health = float(1)
if sum >= 0.1 and sum < 0.3:
  print("You are healthier than 25 percent of americans")
  percentile_health = float(25)
if sum >= 0.3 and sum < 0.5:
  print("You are healthier than 50 percent of americans")
  percentile_health = float(50)
if sum >= 0.5 and sum < 0.7:
  print("You are healthier than 75 percent of americans")
  percentile_health = float(75)
if sum >= 0.7 and sum < 0.8:
   print("You are healthier than 90 percent of americans")
   percentile_health = float(90)
if sum >= 0.8 and sum < 0.9:
    print("You are healthier than 95 percent of americans")
if sum >= 0.9 and sum < 1:
    print("You are healthier than 99 percent of americans")
    percentile_health = float(99)
if sum == 1:
    print("You are healthier than 99.9 percent of americans")
    percentile_health = float(99.9)



Care=input("Would you like to see how your health is compared to money spent on healthcare, yes or no?")
percentile_care=0
if Care == "yes":
   healthcare=float(input("please input your annual healthcare spendings"))
   if healthcare <= float(1234) :
       percentile_care_care = float(1)
       print("you spend more than 1 percent of Americans")
   if healthcare <= float(2345) and healthcare > float(1234):
       percentile_care_care = float(25)
       print("you spend more than 25 percent of Americans")
   if healthcare <= float(3456) and healthcare > float(2345):
      percentile_care = float(50)
      print("you spend more than 50 percent of Americans")
   if healthcare <= float(4567) and healthcare > float(3456):
       percentile_care = float(75)
       print("you spend more than 75 percent of Americans")
   if healthcare <= float(5678) and healthcare > float(4567):
       percentile_care = float(90)
       print("you spend more than 90 percent of Americans")
   if healthcare <= float(6789) and healthcare > float(5678):
       percentile_care = float(95)
       print("you spend more than 95 percent of Americans")
   if healthcare <= float(7890) and healthcare > float(6789):
       percentile_care = float(99)
       print("you spend more than 99 percent of Americans")
else:
     print("thank you for using this application ")
     #END APPLICATION

if percentile_health >= percentile_care:
    print("Everything is fine, you healthcare works for you")
if percentile_health < percentile_care:
    print("NOT good, your spendings on healthcare exceed your level of health, we strongly recommend subscribing to get in contact with a proffesional ")


savedata=input("would you like to save your data, Yes or No")
#date= link with clock
import datetime


now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))



if savedata =="Yes":
 saved_data = {
 "name" : name,
 "index": sum,
 "percentile for health": percentile_health,
  "percentile for healthcare" : percentile_care,
 "datetime": now.strftime("%Y-%m-%d %H:%M:%S")

    }
 print(saved_data)

subscription=input("Do you wish to subscribe, yes or no ?")
if subscription == "no":
    print("Thank you for using this application")
else:
    print("thank you for subscribing")