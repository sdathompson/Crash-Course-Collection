# new_dict = {new_key:new_value for key,value in dict.items() if test}
# import random
#
# #TODO: Create a dictionary comprehension that creates random scores for all of the students
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
#
# students_score = {student:random.randint(0,100) for student in names}
#
# passed_students = {student:score for student,score in students_score.items() if score >= 50}
#
# print(students_score)
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
#
# print(result)


# TODO: You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
#
#
#
# To convert temp_c into temp_f use this formula:
#
# (temp_c * 9/5) + 32 = temp_f
#
#
#
# Celsius to Fahrenheit chart

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = {day:(temp_c * 9/5) + 32 for day, temp_c in weather_c.items()}
#
# print(weather_f)

#Looping through a dictionary:
# for (key, value) in student.dict.items(): key - Output: all keys in dictionary. value - Output: all values in dictionary

import pandas

student_dict = {
    "students": ["Aang", "Toph", "Azula"],
    "score": [78, 68, 198]
}

student_frame = pandas.DataFrame(student_dict)

# Loop through each of the row in Pandas

for (index, row) in student_frame.iterrows():
    if row.students == "Aang":
        print(row.score)