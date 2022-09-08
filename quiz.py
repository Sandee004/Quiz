print("Hello there....I'm Pydroid and I would host this quiz. The questions are coding/programming related.")
name = input("What's your name? ")
print("Alright " + name + " . Best of Luck.")

q1 = '''
    What does error 500 mean?
    a. Forbidden
    b. Timeout Error
    c. Service Unavailable
    d. Internal Sever Error
'''
print(q1)
answer1 = input("Answer: ")
if answer1 == "d":
    print("Correct")
elif answer1 == "a" or answer1 == "b" or answer1 == "c":
    print("Wrong")
else:
    print("Where did you see option " + answer1 + " ? Moving on")


q2 = '''
    Who invented/founded JavaScript?
    a. John Backus
    b. Jordan Walke
    c. Brendan Eich
    d. Rasmus Lerdorf
'''
print(q2)
answer2 = input("Answer: ")
if answer2 == "c":
    print("Correct")
elif answer2 == "a" or answer2 == "b" or answer2 == "d":
    print("Wrong")
else:
    print("Where did you see option " + answer2 + " ? Next")


q3 = '''
    Which is a compiled language
    a. C++
    b. PHP
    c. Python
    d. Ruby
'''
print(q3)
answer3 = input("Answer: ")
if answer3 == "a":
    print("Correct")
elif answer3 == "b" or answer3 == "c" or answer3 == "d":
    print("Wrong")
else:
    print("Where did you see option " + answer3 + " ? How???")


q4 = '''
    Is HTML and CSS a programming language?
    a. Yes
    b. No
    c. Maybe
    d. E no concern me
'''
print(q4)
answer4 = input("Answer: ")
if answer4 == "a":
    print("Correct")
elif answer4 == "b":
    print("You need to be wiped with cord")
elif answer4 == "c":
    print("Better be sure")
elif answer4 == "d":
    print("It must concern you!!")
else:
    print("Where did you see option " + answer4 + " ? Don't stress me")


q5 = '''
    What is FIFO?
    a. Fly In Fly Out
    b. For Instance, Formal Opinion
    c. First In First Out
    d. I don't know
'''
print(q5)
answer5 = input("Answer: ")
if answer5 == "c":
    print("Correct")
elif answer5 == "a" or answer5 == "b":
    print("Wrong")
elif answer5 == "d":
    print("Do research boss")
else:
    print("Where did you see option " + answer5 + " ?")


q6 = '''
    How can you detect the client's browser name?
    a. navigator.appName
    b. browser.name
    c. client.navName
    d. Ask the client
'''
print(q6)
answer6 = input("Answer: ")
if answer6 == "a":
    print("Correct")
elif answer6 == "b" or answer6 == "c" or answer6 == "d":
    print("Wrong")
else:
    print("Where did you see option " + answer6 + " ? Choose from a-d pls")



q7 = '''
    console.log("5" === 5);
    When we run this, the statement printed will be true despite having different data types("5" is a string while 5 is 
a number). This behaviour in JavaScript is  called?
    a. Type Equality
    b. Weak Typing
    c. Type Coercion
    d. Double Equality Check Effect
'''
print(q7)
answer7 = input("Answer: ")
print("No vex boss. I don't even know the answer. Do research and come and tell me. Thanks.")

print("Finished")
