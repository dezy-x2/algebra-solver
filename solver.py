import re

equation = input("What is the equation that needs solving? \n>")

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def mult(a,b):
    return a*b

def divide(a,b):
    return a/b

oppositeDict = {
    "+": subtract,
    "-": add,
    "*": divide,
    "/": mult
}

def regexIt(adden):
    parts = []
    variable = "[a-z]"
    nums = "\d+"
    signs = "[\+-/\*]"

    parts.append(re.findall(variable, adden))
    parts.append(re.findall(nums, adden))
    parts.append(re.findall(signs, adden))

    final = {
        "variables": parts[0],
        "numbers": parts[1],
        "signs": parts[2]
    }

    return final

def makeListNums(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])

def breakDownEquation(equation):
    equate = None
    result = None
    brokenList = equation.split("=")

    if len(brokenList[0]) > len(brokenList[1]):
        equate = 0
        result = 1
    else:
        result = 0
        equate = 1

    brokenDict = regexIt(brokenList[equate])
    brokenDict["answer"] = int(brokenList[result])
    
    makeListNums(brokenDict["numbers"])
    
    return brokenDict

def solveEquation(equation):
    obj = breakDownEquation(equation)

    return oppositeDict[obj["signs"][0]](obj["answer"], obj["numbers"][0])

print(solveEquation(equation)) 