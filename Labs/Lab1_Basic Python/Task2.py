
list2=[]
def print_student(myDict):
   for key in myDict.keys():
       print(key, "=", myDict[key])

def average(list):
    l = len(list)
    sum=0
    for i in list:
        sum= sum+ int(i)
    avg= sum/l
    return avg

def get_average_of_student(dict):
    list1=[]
    list2=[]
    list1= dict["HomeWork marks"]
    list2 = dict["quizMarks"]
    avg1= average(list1)
    avg2= average(list2)
    myTuple= (avg1, avg2)
    return myTuple

def weighted_average(myTuple, projectMarks):
    woh= (25/100)* myTuple[0]
    woq= (40/100)* myTuple[1]
    fp =  (35/100)* projectMarks
    return (woh+woq+fp)/3

def get_letter_grade(marks):
    if(marks>=80 and marks<=100):
        return "A"
    elif(marks>=70 and marks <=79):
        return "B"
    elif (marks >= 60 and marks <= 69):
        return "C"
    elif (marks >= 50 and marks <= 59):
        return "D"
    else:
        return "F"


myList=[]
hwMarksList = ["10", "20", "30", "40"]
quizList = ["20", "30", "30", "40"]
myDict1 = {"Name": "Sama", "HomeWork marks": hwMarksList, "quizMarks": quizList, "ProjectMarks": "90"}
myDict2 = {"Name": "Ayesha", "HomeWork marks": hwMarksList, "quizMarks": quizList, "ProjectMarks": "80"}
myDict3 = {"Name": "Isha", "HomeWork marks": hwMarksList, "quizMarks": quizList, "ProjectMarks": "70"}
myList.append(myDict1)
myList.append(myDict2)
myList.append(myDict3)

print_student(myDict1)
print ("---------------------")
print_student(myDict2)
print ("---------------------")
print_student(myDict3)
print("------------------------")
a = average(hwMarksList)
print("Average: ", a)
b= get_average_of_student(myDict1)
print("Average marks in tuple: ", b)
print("------------------------")
c = weighted_average(b,90)
print("Weighted average: ",c)
print("------------------------")
d= get_letter_grade(c)
print("Grade is: ",d)